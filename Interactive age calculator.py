"""Interactive age calculator

Features:
- Accept birthdate (YYYY-MM-DD) or age (years, optional months/days)
- Validate inputs with helpful error messages
- Show exact breakdown: years, months, days, hours, minutes, seconds
- Show totals (days, hours, minutes, seconds)
- Optionally list leap years between birth year and now
- Repeat or exit
"""

from datetime import datetime, timedelta
import calendar
import re
import sys

DATE_RE = re.compile(r"^(\d{4})[-/](\d{1,2})[-/](\d{1,2})$")


def parse_birthdate(s: str) -> datetime:
    """Parse a date string (YYYY-MM-DD or YYYY/MM/DD) and return a datetime at midnight."""
     m = DATE_RE.match(s.strip())
    if not m:
        raise ValueError("Date must be in YYYY-MM-DD or YYYY/MM/DD format")
    year, month, day = map(int, m.groups())
    return datetime(year, month, day)


def add_months(dt: datetime, months: int) -> datetime:
    """Add (or subtract if months < 0) whole months to a datetime, clipping day to end of month when needed."""
    year = dt.year + (months // 12)
    month = dt.month + (months % 12)
    if month > 12:
        year += 1
        month -= 12
    if month < 1:
        year -= 1
        month += 12
    day = dt.day
    max_day = calendar.monthrange(year, month)[1]
    if day > max_day:
        day = max_day
    return dt.replace(year=year, month=month, day=day)


def compute_age(birth: datetime, now: datetime = None) -> dict:
    now = now or datetime.now()
    if birth > now:
        raise ValueError("Birthdate is in the future")
    delta = now - birth
    total_seconds = int(delta.total_seconds())
    total_days = delta.days

    # years
    years = now.year - birth.year
    try:
        last_anniv = birth.replace(year=birth.year + years)
    except ValueError:
        # handle Feb 29 -> Feb 28 on non-leap
        last_anniv = birth.replace(year=birth.year + years, day=28)
    if last_anniv > now:
        years -= 1
        try:
            last_anniv = birth.replace(year=birth.year + years)
        except ValueError:
            last_anniv = birth.replace(year=birth.year + years, day=28)

    # months (remainder after whole years)
    months_total = (now.year - birth.year) * 12 + now.month - birth.month
    if now.day < birth.day:
        months_total -= 1
    months = months_total % 12

    # compute last month anniversary for days remainder
    months_since_birth = years * 12 + months
    month_anniv = add_months(birth, months_since_birth)
    days = (now.date() - month_anniv.date()).days

    # time of day remainder
    seconds_in_day = total_seconds - (total_days * 86400)
    hours = seconds_in_day // 3600   
    minutes = (seconds_in_day % 3600) // 60
    seconds = seconds_in_day % 60

    return {
        'years': years,
        'months': months,  
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'total_days': total_days,
        'total_seconds': total_seconds,
        'months_total': months_total,
    }


def plural(n, singular, plural_form=None):
    if n == 1:
        return f"{n} {singular}"
    return f"{n} {plural_form or singular + 's'}"


def list_leap_years(start_year: int, end_year: int):
    return [y for y in range(start_year, end_year + 1) if calendar.isleap(y)]


def input_int(prompt: str, min_val=None, max_val=None, allow_empty=False):
    while True:
        s = input(prompt).strip()
        if allow_empty and s == '':
            return None
        try:
            n = int(s)
            if min_val is not None and n < min_val:
                print(f"Please enter a value >= {min_val}")
                continue
            if max_val is not None and n > max_val:
                print(f"Please enter a value <= {max_val}")
                continue
            return n
        except ValueError:
            print("Please enter a valid integer.")


def show_age_summary(name: str, birth: datetime, now: datetime = None):
    now = now or datetime.now()
    age = compute_age(birth, now)
    print('\n' + '=' * 40)
    print(f"Hello, {name}! Here's a detailed breakdown of your age (as of {now.strftime('%Y-%m-%d %H:%M:%S')}):")
    print('-' * 40)
    print(f"Age: {plural(age['years'], 'year')}, {plural(age['months'], 'month')}, {plural(age['days'], 'day')}, {plural(age['hours'], 'hour')}, {plural(age['minutes'], 'minute')}, {plural(age['seconds'], 'second')}")
    print(f"Total: {plural(age['total_days'], 'day')} ({age['total_seconds']} seconds)")
    print('-' * 40)
    # Leap years info
    leaps = list_leap_years(birth.year, now.year)
    print(f"Leap years between {birth.year} and {now.year} ({len(leaps)}): {', '.join(map(str, leaps)) if leaps else 'None'}")
    print('=' * 40 + '\n')


def interactive():
    print("Welcome to the interactive Age Calculator! \U0001F4C5\U0001F4C6")
    while True:
        name = input("\nPlease enter your name (or press Enter to use 'You'): ").strip() or 'You'
        print('\nHow would you like to provide your age?')
        print('  1) I know my birthdate (YYYY-MM-DD)')
        print('  2) I know my age in years/months/days')
        print('  3) Quit')
        choice = input("Choose 1, 2 or 3: ").strip()

        if choice == '1':
            while True:
                s = input("Enter birthdate (YYYY-MM-DD): ").strip()
                try:
                    birth = parse_birthdate(s) 
                    break
                except Exception as  e:
                    print(f"Invalid date: {e}")
            show_age_summary(name, birth)

        elif choice == '2':
            years = input_int("Enter full years (e.g. 34): ", min_val=0)
            months = input_int("Enter extra months (0-11, press Enter for 0): ", min_val=0, max_val=11, allow_empty=True)
            months = months or 0
            days = input_int("Enter extra days (0-31, press Enter for 0): ", min_val=0, max_val=31, allow_empty=True)
            days = days or 0
            # construct approximate birth by subtracting years/months/days from now
            now = datetime.now()
            months_to_subtract = years * 12 + months
            birth_approx = add_months(now, -months_to_subtract)
            birth_approx = birth_approx - timedelta(days=days)
            show_age_summary(name, birth_approx)

        elif choice == '3':
            print('Goodbye!')
            return
        else:
            print('Please choose a valid option (1, 2 or 3).')

        again = input("Would you like to do another calculation? (y/N): ").strip().lower()
        if again != 'y':
            print('Thanks for using the Age Calculator!')
            break


if __name__ == '__main__':
    try:
        interactive()
    except KeyboardInterrupt:
        print('\nInterrupted. Bye!')
        sys.exit(0)
