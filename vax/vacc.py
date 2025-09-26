import datetime
from datetime import timedelta
import re

def parse_age(age):
    """Parse age strings like '6 weeks', '9-12 months', or 'at birth' and return a timedelta."""
    age = age.lower().replace("at birth", "0 days")  
    numbers = re.findall(r'\d+', age)  
    
    if not numbers:
        return timedelta(days=0)  
    
    num = numbers[0]
    if "-" in num:  
        num = num.split("-")[0]
    num = int(num)
    if "week" in age:
        return timedelta(weeks=num)
    elif "month" in age:
        return timedelta(days=num * 30)  
    elif "year" in age:
        return timedelta(days=num * 365)  
    else:
        return timedelta(days=num)  

def get_vaccine_schedule(birth_date):
    vaccines = [
        ("Bacillus Calmette Guerin (BCG)", "At Birth"),
        ("Oral Polio Vaccine (OPV) - 0", "At Birth"),
        ("Hepatitis B birth dose", "At Birth"),
        ("Oral Polio Vaccine (OPV) - 1", "6 weeks"),
        ("Pentavalent - 1", "6 weeks"),
        ("Rotavirus Vaccine (RVV) - 1", "6 weeks"),
        ("Pneumococcal Conjugate Vaccine (PCV) - 1", "6 weeks"),
        ("Inactivated Polio Vaccine (fIPV) - 1", "6 weeks"),
        ("Pentavalent - 2", "10 weeks"),
        ("Oral Polio Vaccine (OPV) - 2", "10 weeks"),
        ("Rotavirus Vaccine (RVV) - 2", "10 weeks"),
        ("Pentavalent - 3", "14 weeks"),
        ("Oral Polio Vaccine (OPV) - 3", "14 weeks"),
        ("Rotavirus Vaccine (RVV) - 3", "14 weeks"),
        ("Pneumococcal Conjugate Vaccine (PCV) - 2", "14 weeks"),
        ("Inactivated Polio Vaccine (fIPV) - 2", "14 weeks"),
        ("Measles & Rubella (MR) - 1", "9-12 months"),
        ("Japanese Encephalitis (JE-1)", "9-12 months"),
        ("Pneumococcal Conjugate Vaccine - Booster", "9-12 months"),
        ("Measles & Rubella (MR) - 2", "16-24 months"),
        ("Japanese Encephalitis (JE-2)", "16-24 months"),
        ("Diphtheria Pertussis & Tetanus (DPT) - Booster 1", "16-24 months"),
        ("Oral Polio Vaccine – Booster", "16-24 months"),
        ("Diphtheria Pertussis & Tetanus (DPT) - Booster 2", "5-6 years"),
        ("Tetanus & adult Diphtheria (Td)", "10 years"),
        ("Tetanus & adult Diphtheria (Td)", "16 years")
    ]
    
    schedule = []
    for vaccine, age in vaccines:
        vaccine_date = birth_date + parse_age(age)
        schedule.append((vaccine, vaccine_date.strftime('%Y-%m-%d')))
    
    return schedule

def main():
    birth_date_str = input("Enter child's birth date (YYYY-MM-DD): ")
    birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d")
    
    schedule = get_vaccine_schedule(birth_date)
    print("\nVaccine Schedule:")
    for vaccine, date in schedule:
        print(f"{date}: {vaccine}")

if __name__ == "__main__":
    main()
