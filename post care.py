from datetime import datetime, timedelta
from tabulate import tabulate

def validate_date(last_period_date):
    try:
        return datetime.strptime(last_period_date, "%Y-%m-%d")
    except ValueError:
        return None

def calc_period_dates(last_period_date, cycle_length, number_of_periods):
    return [last_period_date + timedelta(days=cycle_length * i) for i in range(number_of_periods)]

def calc_fertility(period_dates, cycle_length):
    ovulation_dates = [date + timedelta(days=(cycle_length - 14)) for date in period_dates]
    fertility_windows = [(ovulation - timedelta(days=5), ovulation + timedelta(days=1)) for ovulation in ovulation_dates]
    return ovulation_dates, fertility_windows

def display_data(period_dates, ovulation_dates, fertility_windows):
    period_table = [[f"Cycle {i+1}", date.strftime('%Y-%m-%d'), ovulation_dates[i].strftime('%Y-%m-%d'),
                     fertility_windows[i][0].strftime('%Y-%m-%d'), fertility_windows[i][1].strftime('%Y-%m-%d')]
                    for i, date in enumerate(period_dates)]
    print("\nYour predicted menstruation, ovulation, and fertile windows are:")
    print(tabulate(period_table, headers=["Cycle", "Period", "Ovulation Date", "Fertile Start", "Fertile End"], tablefmt="grid"))

def display_ovulation(period_dates, ovulation_dates):
    ovulation_table = [[f"Cycle {i+1}", period_dates[i].strftime('%Y-%m-%d'), ovulation_dates[i].strftime('%Y-%m-%d')]
                       for i in range(len(ovulation_dates))]
    print("\nYour predicted menstruation and ovulation dates are:")
    print(tabulate(ovulation_table, headers=["Cycle", "Menstruation Start Date", "Ovulation Date"], tablefmt="grid"))

def display_best_dates_for_pregnancy(fertility_windows):
    best_dates_table = [[f"Cycle {i+1}", ", ".join((fertility_windows[i][0] + timedelta(days=j)).strftime('%Y-%m-%d')
                         for j in range((fertility_windows[i][1] - fertility_windows[i][0]).days))]
                        for i in range(len(fertility_windows))]
    print("\nThe best dates for intercourse to increase the chance of pregnancy are:")
    print(tabulate(best_dates_table, headers=["Cycle", "Best Dates"], tablefmt="grid"))

def period_tracker():
    print("""
    ======================================================================================================
                            Welcome to the Period Tracker Program!
            This app helps you track your menstrual cycles, ovulation dates, and fertility windows.
                                Let's get started! <3
    ======================================================================================================
    """)

    while True:
        last_period_date = None
        while not last_period_date:
            last_period_date = validate_date(input('Enter the date of your last period [YYYY-MM-DD]: '))
            if not last_period_date:
                print('Invalid input. Please try again.')

        cycle_length = None
        while cycle_length is None:
            try:
                cycle_length = int(input('Enter your average cycle length in days (21-35): '))
                if cycle_length < 21 or cycle_length > 35:
                    print('Cycle length should be between 21 and 35 days.')
                    cycle_length = None
            except ValueError:
                print('Invalid input. Please enter a valid number.')

        number_of_periods = None
        while number_of_periods is None:
            try:
                number_of_periods = int(input('Enter the number of future periods to calculate (1-12): '))
                if not (1 <= number_of_periods <= 12):
                    print('Number of periods must be between 1 and 12.')
                    number_of_periods = None
            except ValueError:
                print('Invalid input. Please enter a valid number.')

        period_dates = calc_period_dates(last_period_date, cycle_length, number_of_periods)
        ovulation_dates, fertility_windows = calc_fertility(period_dates, cycle_length)

        sexually_active = input('Are you sexually active? [y/n]: ').strip().lower()
        if sexually_active == 'y':
            planning_pregnancy = input('Are you planning to get pregnant? [y/n]: ').strip().lower()
            display_data(period_dates, ovulation_dates, fertility_windows)
            if planning_pregnancy == 'y':
                display_best_dates_for_pregnancy(fertility_windows)
        else:
            display_ovulation(period_dates, ovulation_dates)

        if input("Do you want to run the program again? (y/n): ").strip().lower() != 'y':
            break

if __name__ == "__main__":
    period_tracker()
