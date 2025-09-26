#!/usr/bin/env python3
"""
Pregnancy 7-day Meal Planner with expanded food DB and CSV export.

- Each food entry contains: name, kcal, protein_g, carbs_g, fat_g, iron_mg, calcium_mg, folate_ug
- Countries included: india, usa, generic (veg + nonveg each)
- Generates 7-day varied plan and optionally writes CSV.

NOT MEDICAL ADVICE. Values are approximate.
"""

import random
import csv
import textwrap
from datetime import datetime

# ---------------------------
# Expanded Food Database (approximate per-serving values)
# Note: Values are illustrative estimates for common portions.
# You can extend / refine these numbers using local food composition tables.
# ---------------------------

FOOD_DB = {
    "india": {
        "veg": [
            # name, kcal, protein_g, carbs_g, fat_g, iron_mg, calcium_mg, folate_ug
            ("Idli (2 medium)", 120, 4.0, 22.0, 1.0, 0.8, 10, 8),
            ("Dosa (1 medium) + sambar", 280, 7.0, 35.0, 8.0, 2.0, 40, 25),
            ("Poha (1 cup)", 250, 6.0, 45.0, 6.0, 1.2, 20, 30),
            ("Upma (1 cup)", 240, 6.0, 40.0, 6.0, 1.2, 20, 18),
            ("Chapati (2) + dal (1 cup)", 450, 15.0, 60.0, 10.0, 4.0, 80, 80),
            ("Palak paneer (1 cup)", 350, 18.0, 10.0, 22.0, 3.5, 250, 80),
            ("Paneer bhurji (100g)", 300, 18.0, 6.0, 22.0, 0.2, 200, 20),
            ("Curd (1 cup)", 150, 8.0, 11.0, 7.0, 0.1, 250, 20),
            ("Mixed nuts (30g)", 180, 6.0, 8.0, 16.0, 1.5, 40, 30),
            ("Sprouted moong salad (1 cup)", 150, 8.0, 20.0, 1.5, 2.5, 30, 40),
            ("Ragi porridge (1 cup)", 220, 6.0, 46.0, 2.0, 2.3, 40, 18),
            ("Chickpea salad (1 cup)", 290, 12.0, 45.0, 6.0, 4.7, 80, 61),
            ("Oats (1 cup cooked) + milk", 220, 10.0, 32.0, 6.0, 1.8, 250, 20),
            ("Fruit + peanut butter (1 tbsp PB)", 200, 6.0, 25.0, 8.0, 0.6, 20, 15),
            ("Masala omelette (veg style - paneer/tofu)", 250, 14.0, 6.0, 18.0, 1.0, 80, 30),
            ("Vegetable pulao (1 plate)", 420, 8.0, 70.0, 10.0, 1.5, 40, 35),
            ("Rajma (1 cup)", 240, 15.0, 40.0, 2.0, 5.2, 80, 120),
            ("Sambar (1 bowl) + brown rice", 360, 10.0, 60.0, 6.0, 3.0, 60, 70),
            ("Besan chilla (2)", 300, 15.0, 28.0, 10.0, 2.5, 50, 40),
            ("Aloo paratha (1) + curd", 400, 9.0, 55.0, 14.0, 1.5, 150, 25),
            ("Moong dal khichdi (1 bowl)", 320, 12.0, 52.0, 6.0, 2.8, 50, 60),
            ("Masala dosa + chutney", 320, 6.0, 50.0, 10.0, 1.4, 30, 20),
            ("Paneer tikka (100g)", 260, 18.0, 6.0, 18.0, 0.4, 160, 25),
            ("Fruit salad + yogurt", 180, 6.0, 30.0, 3.0, 0.6, 150, 12),
            ("Sattu drink (1 glass)", 180, 10.0, 20.0, 6.0, 2.5, 40, 30),
            ("Idiyappam + coconut milk (1 serving)", 300, 6.0, 52.0, 8.0, 0.8, 30, 10),
            ("Vegetable wrap (whole wheat)", 350, 12.0, 45.0, 12.0, 2.0, 80, 40),
            ("Khichdi with vegetables", 300, 12.0, 48.0, 5.0, 2.0, 50, 50),
            ("Lassi (1 glass, sweet)", 180, 6.0, 30.0, 5.0, 0.2, 150, 10),
            ("Methi thepla + curd", 380, 8.0, 50.0, 14.0, 2.0, 80, 40),
            ("Poached pear + low-fat yogurt", 160, 6.0, 28.0, 1.5, 0.4, 120, 10),
            ("Vegetable curry + 1 roti", 320, 8.0, 40.0, 12.0, 2.0, 60, 30),
            ("Murmura chaat + peanuts", 220, 6.0, 28.0, 10.0, 1.8, 40, 12),
            ("Masala oats", 240, 9.0, 35.0, 7.0, 1.5, 40, 15),
            ("Banana + almond butter", 230, 6.0, 30.0, 10.0, 0.7, 40, 15),
            ("Sweet potato (100g) + curd", 200, 4.0, 40.0, 0.5, 0.8, 30, 12),
            ("Mixed vegetable curry (1 cup) + rice", 380, 8.0, 60.0, 10.0, 2.0, 60, 35),
            ("Idli upma combo", 300, 8.0, 52.0, 7.0, 1.0, 30, 20),
            ("Mango shake with milk (1 glass)", 260, 8.0, 45.0, 6.0, 0.4, 200, 25),
        ],
        "nonveg": [
            ("Boiled egg (1 large)", 78, 6.0, 0.6, 5.3, 0.6, 25, 24),
            ("Egg bhurji (2 eggs)", 160, 12.0, 2.0, 12.0, 1.2, 40, 30),
            ("Grilled chicken (100g)", 165, 31.0, 0.0, 3.6, 0.9, 15, 6),
            ("Fish curry (100g fish portion)", 220, 22.0, 4.0, 12.0, 1.0, 20, 10),
            ("Chicken biryani (1 plate)", 550, 25.0, 65.0, 18.0, 2.0, 40, 30),
            ("Prawn curry (100g)", 150, 24.0, 2.0, 3.5, 1.8, 70, 20),
            ("Egg dosa", 330, 14.0, 40.0, 12.0, 1.0, 40, 20),
            ("Chicken stew + rice", 420, 28.0, 50.0, 12.0, 1.5, 40, 15),
            ("Keema curry (100g)", 300, 20.0, 5.0, 20.0, 2.1, 30, 12),
            ("Fish fry + salad", 320, 22.0, 10.0, 18.0, 1.2, 40, 8),
            ("Egg curry + roti", 380, 18.0, 30.0, 20.0, 2.0, 60, 30),
            ("Chicken kebab (3 pcs)", 280, 30.0, 5.0, 15.0, 1.0, 20, 8),
            ("Tandoori chicken (100g)", 220, 28.0, 2.0, 10.0, 0.8, 20, 5),
            ("Fish biryani (1 plate)", 520, 24.0, 65.0, 16.0, 2.0, 50, 30),
            ("Egg sandwich", 320, 15.0, 30.0, 14.0, 1.5, 80, 20),
            ("Mutton curry (100g)", 330, 25.0, 2.0, 22.0, 2.5, 20, 8),
            ("Chicken salad (bowl)", 350, 30.0, 10.0, 18.0, 1.2, 40, 20),
            ("Fish soup + toast", 240, 20.0, 20.0, 8.0, 1.0, 30, 10),
            ("Egg bhurji wrap", 380, 20.0, 28.0, 18.0, 1.5, 60, 25),
            ("Grilled fish (100g)", 200, 22.0, 0.0, 11.0, 0.5, 15, 5),
            ("Prawn pulao", 450, 20.0, 60.0, 12.0, 1.6, 40, 20),
            ("Chicken curry + chapati", 480, 28.0, 50.0, 18.0, 1.8, 60, 30),
            ("Egg & veg fried rice", 420, 18.0, 58.0, 12.0, 1.4, 50, 20),
            ("Fish + steamed veg", 300, 28.0, 12.0, 12.0, 1.0, 60, 12),
            ("Chicken sandwich", 380, 26.0, 34.0, 14.0, 1.0, 80, 25),
            ("Egg white omelette with veggies", 140, 18.0, 4.0, 5.0, 0.6, 30, 20),
            ("Grilled prawn skewer", 160, 20.0, 2.0, 6.0, 1.5, 20, 8),
            ("Fish curry + rice", 500, 24.0, 68.0, 16.0, 1.8, 50, 22),
            ("Chicken pulao", 480, 26.0, 60.0, 14.0, 1.5, 50, 25),
            ("Egg paratha", 430, 16.0, 48.0, 18.0, 1.4, 80, 30),
            ("Mutton biryani (small)", 600, 28.0, 70.0, 24.0, 2.8, 40, 30),
            ("Tuna sandwich (canned tuna)", 350, 28.0, 30.0, 10.0, 1.2, 100, 15),
            ("Chicken fried rice", 520, 24.0, 70.0, 18.0, 1.6, 60, 20),
            ("Fish cutlet + salad", 310, 22.0, 20.0, 14.0, 1.0, 40, 10),
            ("Egg kebab", 220, 14.0, 6.0, 16.0, 1.0, 60, 15),
            ("Grilled chicken wrap", 420, 30.0, 40.0, 14.0, 1.2, 80, 20),
            ("Shrimp salad", 260, 24.0, 6.0, 12.0, 1.6, 50, 12),
        ]
    },
    "usa": {
        "veg": [
            ("Greek yogurt (1 cup)", 130, 17.0, 10.0, 0.7, 0.1, 150.0, 25),
            ("Oatmeal (1 cup cooked) + milk", 220, 10.0, 34.0, 6.0, 1.5, 250.0, 30),
            ("Peanut butter sandwich", 350, 15.0, 34.0, 18.0, 1.8, 40.0, 30),
            ("Lentil soup (1.5 cups)", 300, 18.0, 40.0, 4.0, 6.6, 60.0, 180),
            ("Quinoa salad (1 cup)", 222, 8.0, 39.0, 3.6, 2.8, 31.0, 42),
            ("Tofu stir-fry (150g tofu)", 220, 16.0, 10.0, 14.0, 3.6, 350.0, 60),
            ("Cottage cheese (1 cup)", 220, 28.0, 6.0, 10.0, 0.2, 138.0, 37),
            ("Smoothie with protein powder", 300, 20.0, 30.0, 6.0, 1.5, 200.0, 50),
            ("Hummus + pita", 300, 12.0, 35.0, 12.0, 2.4, 50.0, 60),
            ("Mixed nuts (30g)", 180, 6.0, 8.0, 16.0, 1.1, 30.0, 10),
            ("Avocado toast (1 slice)", 240, 6.0, 28.0, 12.0, 0.8, 10.0, 20),
            ("Black bean burrito", 420, 20.0, 55.0, 12.0, 3.6, 80.0, 120),
            ("Veggie burger (patty)", 300, 18.0, 30.0, 12.0, 3.0, 100.0, 60),
            ("Chia pudding (1 cup)", 250, 8.0, 20.0, 12.0, 2.0, 180.0, 40),
            ("Spinach salad with seeds", 200, 6.0, 12.0, 14.0, 2.7, 80.0, 60),
            ("Bean chili (1 bowl)", 380, 24.0, 45.0, 8.0, 4.5, 100.0, 150),
            ("Tofu scramble", 260, 18.0, 10.0, 16.0, 3.2, 200.0, 50),
            ("Veggie pasta (1 plate)", 520, 18.0, 80.0, 12.0, 2.5, 60.0, 40),
            ("Couscous salad", 320, 9.0, 58.0, 6.0, 1.6, 30.0, 25),
            ("Greek salad + chickpeas", 340, 14.0, 30.0, 18.0, 3.0, 100.0, 70),
            ("Whole grain cereal + milk", 260, 8.0, 50.0, 4.0, 2.0, 200.0, 80),
            ("Veggie omelette (egg subs)", 200, 15.0, 4.0, 12.0, 1.2, 100.0, 25),
            ("Peanut butter banana smoothie", 330, 12.0, 40.0, 12.0, 1.6, 40.0, 30),
            ("Stuffed bell peppers (rice + beans)", 380, 14.0, 60.0, 10.0, 3.0, 60.0, 70),
            ("Falafel + salad", 420, 18.0, 45.0, 18.0, 2.5, 80.0, 50),
            ("Veg sushi rolls (6 pcs)", 250, 6.0, 50.0, 4.0, 1.0, 20.0, 25),
            ("Protein pancake (1 serving)", 320, 20.0, 35.0, 8.0, 1.5, 150.0, 40),
            ("Lentil salad (1 cup)", 300, 16.0, 40.0, 6.0, 4.5, 60.0, 150),
            ("Edamame (1 cup)", 190, 17.0, 15.0, 8.0, 3.5, 98.0, 120),
            ("Tomato soup + grilled cheese (veg)", 380, 14.0, 40.0, 18.0, 1.8, 200.0, 30),
        ],
        "nonveg": [
            ("Scrambled eggs (2)", 160, 12.0, 2.0, 10.0, 1.2, 50.0, 90),
            ("Turkey sandwich", 350, 25.0, 34.0, 10.0, 1.4, 50.0, 30),
            ("Grilled salmon (100g)", 206, 22.0, 0.0, 12.0, 0.3, 9.0, 10),
            ("Chicken salad", 400, 30.0, 10.0, 20.0, 1.5, 50.0, 20),
            ("Beef chili (1 bowl)", 380, 24.0, 30.0, 18.0, 3.0, 60.0, 40),
            ("Tuna salad (1 can tuna)", 200, 30.0, 0.0, 7.0, 1.0, 10.0, 5),
            ("Grilled chicken breast (100g)", 165, 31.0, 0.0, 3.6, 1.0, 15.0, 6),
            ("Shrimp stir-fry", 220, 24.0, 12.0, 6.0, 1.6, 70.0, 20),
            ("Egg & avocado bagel", 420, 18.0, 45.0, 18.0, 2.0, 80.0, 50),
            ("Chicken wrap", 420, 26.0, 40.0, 14.0, 1.2, 80.0, 20),
            ("Salmon sushi (8 pcs)", 360, 18.0, 50.0, 8.0, 1.0, 30.0, 15),
            ("Turkey chili (bowl)", 380, 28.0, 35.0, 10.0, 3.0, 60.0, 30),
            ("Fish tacos (2)", 430, 22.0, 40.0, 18.0, 1.8, 80.0, 20),
            ("Grilled steak (120g)", 285, 25.0, 0.0, 18.0, 2.6, 12.0, 8),
            ("Tuna sandwich", 350, 28.0, 34.0, 12.0, 1.2, 60.0, 20),
            ("Chicken curry + rice", 520, 28.0, 60.0, 18.0, 1.8, 60.0, 25),
            ("Egg salad", 300, 18.0, 6.0, 22.0, 1.6, 100.0, 60),
            ("BBQ chicken (thigh)", 260, 24.0, 0.0, 16.0, 1.0, 20.0, 10),
            ("Fish & chips (small)", 650, 30.0, 70.0, 30.0, 2.5, 40.0, 15),
            ("Chicken noodle soup", 260, 16.0, 30.0, 6.0, 1.2, 40.0, 10),
            ("Sardines (100g)", 208, 24.0, 0.0, 11.5, 2.9, 382.0, 30),
            ("Pulled pork sandwich", 520, 28.0, 60.0, 20.0, 1.5, 40.0, 10),
            ("Egg burrito", 420, 20.0, 42.0, 18.0, 1.6, 120.0, 50),
            ("Grilled mahi-mahi (100g)", 134, 22.0, 0.0, 3.0, 0.3, 10.0, 7),
            ("Chicken quesadilla", 480, 30.0, 40.0, 20.0, 1.8, 60.0, 20),
            ("Salmon salad bowl", 420, 30.0, 20.0, 20.0, 1.2, 40.0, 10),
            ("Tuna steak (150g)", 220, 46.0, 0.0, 2.0, 1.0, 10.0, 5),
            ("Egg & cheese sandwich", 360, 18.0, 30.0, 16.0, 1.2, 120.0, 30),
        ]
    },
    "generic": {
        "veg": [
            ("Oats + milk", 220, 10.0, 32.0, 6.0, 1.8, 250.0, 20),
            ("Bean stew (1 cup)", 300, 16.0, 40.0, 4.0, 4.5, 60.0, 120),
            ("Tofu dish (150g)", 220, 16.0, 10.0, 14.0, 3.6, 350.0, 50),
            ("Rice + dal (1 plate)", 450, 12.0, 60.0, 8.0, 3.0, 60.0, 50),
            ("Salad with chickpeas", 350, 12.0, 40.0, 12.0, 3.5, 80.0, 60),
            ("Yogurt + fruit", 180, 8.0, 28.0, 3.0, 0.6, 150.0, 10),
            ("Wholegrain sandwich + veggies", 320, 12.0, 40.0, 10.0, 2.0, 80.0, 40),
            ("Quinoa bowl", 350, 12.0, 50.0, 10.0, 3.0, 40.0, 30),
            ("Lentil curry", 320, 18.0, 45.0, 6.0, 5.0, 80.0, 140),
            ("Cottage cheese + fruit", 220, 28.0, 14.0, 10.0, 0.2, 138.0, 30),
            ("Hummus + veg sticks", 250, 10.0, 30.0, 10.0, 2.4, 50.0, 40),
            ("Vegetable stew", 260, 8.0, 40.0, 8.0, 2.0, 60.0, 30),
        ],
        "nonveg": [
            ("Eggs (2)", 160, 12.0, 2.0, 10.0, 1.2, 100.0, 90),
            ("Grilled chicken (100g)", 165, 31.0, 0.0, 3.6, 1.0, 15.0, 6),
            ("Fish (100g)", 200, 22.0, 0.0, 11.0, 0.5, 15.0, 8),
            ("Rice + chicken curry", 500, 28.0, 60.0, 18.0, 1.8, 60.0, 25),
            ("Tuna sandwich", 350, 28.0, 34.0, 12.0, 1.2, 60.0, 20),
            ("Shrimp pasta", 420, 24.0, 50.0, 12.0, 1.6, 40.0, 15),
            ("Chicken salad", 400, 30.0, 12.0, 18.0, 1.5, 50.0, 20),
            ("Beef stew (small)", 380, 28.0, 18.0, 18.0, 3.0, 40.0, 15),
            ("Grilled fish + veg", 300, 28.0, 12.0, 12.0, 1.0, 60.0, 12),
            ("Chicken wrap", 420, 26.0, 40.0, 14.0, 1.2, 80.0, 20),
        ]
    }
}

MEAL_SLOTS = ["Breakfast", "Lunch", "Snack", "Dinner"]

# ---------------------------
# Helper / Core functions
# ---------------------------

def get_user_input():
    print(textwrap.dedent("""
    Pregnancy 7-day Meal Planner (expanded)
    Please answer the prompts below. Press Enter to accept defaults.
    """))
    country = input("Country (India / USA / Generic) [default: India]: ").strip().lower() or "india"
    if country not in FOOD_DB:
        print("Country not available in DB — using 'generic'.")
        country = "generic"
    trimester = input("Trimester? (1 / 2 / 3) [default: 2]: ").strip()
    if trimester not in ("1", "2", "3"):
        trimester = "2"
    pref = input("Dietary preference? (veg / nonveg) [default: veg]: ").strip().lower() or "veg"
    if pref not in ("veg","nonveg"):
        pref = "veg"
    weight_input = input("Optional - pre-pregnancy weight in kg (press Enter to skip): ").strip()
    try:
        weight = float(weight_input) if weight_input else None
    except:
        weight = None
    export_csv = input("Export plan to CSV? (y/n) [default: y]: ").strip().lower() or "y"
    export_csv = export_csv.startswith("y")
    seed_input = input("Optional - random seed for reproducible plans (press Enter to skip): ").strip()
    seed = int(seed_input) if seed_input.isdigit() else None
    return country, int(trimester), pref, weight, export_csv, seed

def nutrient_targets(trimester, weight=None):
    """
    Returns target dict (approximate) for pregnancy:
    - protein_g (use 1.1 g/kg if weight provided, else ~71 g/day)
    - calories_kcal baseline 1800 + trimester extra (2: +340, 3: +450)
    - iron_mg ~27 mg/day, folate_ug ~600, calcium_mg ~1000
    """
    if weight and weight > 0:
        protein_target = round(1.1 * weight, 1)
    else:
        protein_target = 71.0
    extra = 0
    if trimester == 2:
        extra = 340
    elif trimester == 3:
        extra = 450
    calorie_target = 1800 + extra
    return {
        "protein_g": protein_target,
        "calories_kcal": calorie_target,
        "iron_mg": 27.0,
        "folate_ug": 600.0,
        "calcium_mg": 1000.0
    }

def pick_varied_meal(country, pref, used_names):
    pool = FOOD_DB[country][pref]
    # prefer items not recently used
    choices = [item for item in pool if item[0] not in used_names]
    if not choices:
        choices = pool[:]
    choice = random.choice(choices)
    used_names.add(choice[0])
    return choice

def build_week_plan(country, trimester, pref, targets, seed=None):
    if seed is not None:
        random.seed(seed)
    week = []
    # attempt to ensure variety across days
    global_used = set()
    for d in range(7):
        day_plan = []
        used_today = set()
        # breakfast, lunch, snack, dinner
        for slot in MEAL_SLOTS:
            item = pick_varied_meal(country, pref, global_used)
            # occasionally mix two items for lunch/dinner to reach nutrient targets
            if slot in ("Lunch", "Dinner") and random.random() < 0.28:
                second = pick_varied_meal(country, pref, global_used)
                name = f"{item[0]} + {second[0]}"
                kcal = item[1] + second[1]
                protein_g = item[2] + second[2]
                carbs_g = item[3] + second[3]
                fat_g = item[4] + second[4]
                iron_mg = item[5] + second[5]
                calcium_mg = item[6] + second[6]
                folate_ug = item[7] + second[7]
            else:
                name, kcal, protein_g, carbs_g, fat_g, iron_mg, calcium_mg, folate_ug = item
            day_plan.append({
                "day": d+1,
                "slot": slot,
                "food": name,
                "kcal": kcal,
                "protein_g": protein_g,
                "carbs_g": carbs_g,
                "fat_g": fat_g,
                "iron_mg": iron_mg,
                "calcium_mg": calcium_mg,
                "folate_ug": folate_ug
            })
        # small shuffle to avoid same pattern every day
        random.shuffle(day_plan)
        week.append(day_plan)
    return week

def summarize_day(day_entries):
    totals = {
        "kcal": 0.0,
        "protein_g": 0.0,
        "carbs_g": 0.0,
        "fat_g": 0.0,
        "iron_mg": 0.0,
        "calcium_mg": 0.0,
        "folate_ug": 0.0
    }
    for e in day_entries:
        totals["kcal"] += e["kcal"]
        totals["protein_g"] += e["protein_g"]
        totals["carbs_g"] += e["carbs_g"]
        totals["fat_g"] += e["fat_g"]
        totals["iron_mg"] += e["iron_mg"]
        totals["calcium_mg"] += e["calcium_mg"]
        totals["folate_ug"] += e["folate_ug"]
    # round for neatness
    for k in totals:
        totals[k] = round(totals[k], 1)
    return totals

def print_weekly_plan(week, targets):
    print("\n" + "="*70)
    print("7-Day Pregnancy Meal Plan — Approximate nutrient breakdown per meal & per day")
    print(f"Targets: Protein ≈ {targets['protein_g']} g/day, Calories ≈ {targets['calories_kcal']} kcal/day, "
          f"Iron ≈ {targets['iron_mg']} mg/day, Folate ≈ {targets['folate_ug']} µg/day, Calcium ≈ {targets['calcium_mg']} mg/day")
    print("="*70 + "\n")
    for i, day in enumerate(week, start=1):
        print(f"Day {i}:")
        totals = summarize_day(day)
        # print meals sorted by slot for readability
        for e in sorted(day, key=lambda x: MEAL_SLOTS.index(x["slot"])):
            print(f"  {e['slot']}: {e['food']}")
            print(f"     -> {e['kcal']} kcal | P: {e['protein_g']} g | C: {e['carbs_g']} g | F: {e['fat_g']} g | "
                  f"Iron: {e['iron_mg']} mg | Ca: {e['calcium_mg']} mg | Folate: {e['folate_ug']} µg")
        print(f"  => Daily totals: {totals['kcal']} kcal | P: {totals['protein_g']} g | C: {totals['carbs_g']} g | F: {totals['fat_g']} g")
        print(f"                 Iron: {totals['iron_mg']} mg | Ca: {totals['calcium_mg']} mg | Folate: {totals['folate_ug']} µg")
        # quick advice
        notes = []
        if totals['protein_g'] < targets['protein_g']:
            need = round(targets['protein_g'] - totals['protein_g'], 1)
            notes.append(f"Protein shortfall ≈ {need} g (add a protein snack: yogurt, boiled eggs, or nuts).")
        if totals['kcal'] < targets['calories_kcal']:
            needc = int(targets['calories_kcal'] - totals['kcal'])
            notes.append(f"Calories short by ≈ {needc} kcal (add healthy snack or slightly larger portions).")
        if totals['iron_mg'] < targets['iron_mg']:
            needi = round(targets['iron_mg'] - totals['iron_mg'], 1)
            notes.append(f"Iron shortfall ≈ {needi} mg — consider iron-rich snack or supplement after consulting provider.")
        if totals['folate_ug'] < targets['folate_ug']:
            needf = int(targets['folate_ug'] - totals['folate_ug'])
            notes.append(f"Folate shortfall ≈ {needf} µg — eat leafy greens, beans, or fortified cereal.")
        if totals['calcium_mg'] < targets['calcium_mg']:
            needca = int(targets['calcium_mg'] - totals['calcium_mg'])
            notes.append(f"Calcium shortfall ≈ {needca} mg — add dairy or calcium-fortified foods.")
        if notes:
            print("  >> Suggestions: " + " ".join(notes))
        else:
            print("  >> Nutrient targets for the day are reasonably met.")
        print("-"*70)

def export_csv(week, targets, filename=None):
    if filename is None:
        filename = f"meal_plan_week_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    header = ["Day", "Slot", "Food", "Calories_kcal", "Protein_g", "Carbs_g", "Fat_g", "Iron_mg", "Calcium_mg", "Folate_ug"]
    rows = []
    for day_entries in week:
        for e in sorted(day_entries, key=lambda x: MEAL_SLOTS.index(x["slot"])):
            rows.append([
                e["day"],
                e["slot"],
                e["food"],
                e["kcal"],
                e["protein_g"],
                e["carbs_g"],
                e["fat_g"],
                e["iron_mg"],
                e["calcium_mg"],
                e["folate_ug"]
            ])
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["# Generated on", datetime.now().isoformat()])
        writer.writerow([])
        writer.writerow(["Targets",
                         f"Protein_g={targets['protein_g']}",
                         f"Calories_kcal={targets['calories_kcal']}",
                         f"Iron_mg={targets['iron_mg']}",
                         f"Folate_ug={targets['folate_ug']}",
                         f"Calcium_mg={targets['calcium_mg']}"])
        writer.writerow([])
        writer.writerow(header)
        writer.writerows(rows)
    return filename

# ---------------------------
# Main
# ---------------------------

def main():
    country, trimester, pref, weight, export_csv_choice, seed = get_user_input()
    targets = nutrient_targets(trimester, weight)
    week = build_week_plan(country, trimester, pref, targets, seed=seed)
    print_weekly_plan(week, targets)
    if export_csv_choice:
        fname = export_csv(week, targets, filename="meal_plan_week.csv")
        print(f"\nCSV exported: {fname} (open with Excel / Google Sheets).")
    print("\nReminder: This tool provides approximate nutrient estimates for educational planning.")
    print("For personalized pregnancy nutrition (supplements, iron dosing, gestational diabetes, allergies), consult a healthcare provider or registered dietitian.")

if __name__ == "__main__":
    main()