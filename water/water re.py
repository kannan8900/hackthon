yfrom plyer import notification
import time
import math
from datetime import datetime, timedelta

# ================= Configuration =================
daily_goal_glasses = 10           # User should drink at least 10 glasses
glass_size_liters = 0.25          # 1 glass = 250 ml
interval_seconds = 10             # Reminder every 10 seconds (for testing)

# Track glasses drunk
glasses_drunk = 0

def send_hydration_notification(remaining_glasses, remaining_liters, custom_message=None):
    """Send notification with hydration details"""
    message = (custom_message if custom_message 
               else f"💧 Time to drink water!\n"
                    f"Remaining: {remaining_glasses} glasses ({remaining_liters:.2f} L)")
    notification.notify(
        title="Hydration Reminder",
        message=message,
        timeout=10
    )

print("💧 Hydration Reminder Started!")
print(f"Goal: {daily_goal_glasses} glasses ({daily_goal_glasses * glass_size_liters:.2f} L).\n")

# ================= Start reminders =================
while glasses_drunk < daily_goal_glasses:
    remaining_glasses = daily_goal_glasses - glasses_drunk
    remaining_liters = remaining_glasses * glass_size_liters

    # 1️⃣ Send reminder
    send_hydration_notification(remaining_glasses, remaining_liters)

    # 2️⃣ Ask user input (y/n)
    try:
        user_input = input(f"Did you drink a glass of water? (y/n) Remaining: {remaining_glasses}: ").strip().lower()
        if user_input == 'y':
            glasses_drunk += 1
            print(f"✅ Logged: You drank 1 glass. Total so far: {glasses_drunk}/{daily_goal_glasses}")
        elif user_input == 'n':
            print("⚠️ Skipped. Don’t forget to drink water!")
        else:
            print("❌ Invalid input, skipping this reminder.")
    except:
        print("❌ Invalid input, skipping this reminder.")

    # 3️⃣ Print updated status
    remaining_glasses = daily_goal_glasses - glasses_drunk
    remaining_liters = remaining_glasses * glass_size_liters
    print(f"✅ Updated: {glasses_drunk} glasses drank. {remaining_glasses} glasses ({remaining_liters:.2f} L) remaining for today.\n")

    # 4️⃣ Goal check
    if glasses_drunk >= daily_goal_glasses:
        notification.notify(
            title="Hydration Reminder",
            message="🎉 You have reached your daily water goal! Stay hydrated.",
            timeout=10
        )
        print("🎉 Congratulations! You have reached your daily water goal!")
        break

    # 5️⃣ Wait until next reminder
    print(f"⏰ Next reminder in {interval_seconds} seconds...")
    time.sleep(interval_seconds)
