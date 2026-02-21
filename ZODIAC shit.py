from datetime import date, timedelta
import sys

# ------------------------ INPUT UTILITIES ------------------------

def get_int(prompt, min_val, max_val):
    """Safely get integer input within a specific range."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"⚠ Enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("⚠ Numbers only please.")

def pause():
    input("\nPress ENTER to continue...")

# ------------------------ DATE FUNCTIONS ------------------------

def is_leap(year):
    """Return True if year is leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_birth_date():
    print("\n📅 Enter your birth date")
    year = get_int("Year (1900 - today): ", 1900, date.today().year)
    month = get_int("Month (1 - 12): ", 1, 12)

    month_days = [31, 29 if is_leap(year) else 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    day = get_int(f"Day (1 - {month_days[month-1]}): ", 1, month_days[month-1])
    return date(year, month, day)

# ------------------------ CALCULATIONS ------------------------

def calculate_age(birthday):
    today = date.today()
    days_lived = (today - birthday).days

    years = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        years -= 1

    months = years * 12 + today.month - birthday.month
    if today.day < birthday.day:
        months -= 1

    return years, months, days_lived

def zodiac_sign(b):
    zodiac = [
        ("Capricorn", (1,20)), ("Aquarius",(2,19)), ("Pisces",(3,21)),
        ("Aries",(4,20)), ("Taurus",(5,21)), ("Gemini",(6,21)),
        ("Cancer",(7,23)), ("Leo",(8,23)), ("Virgo",(9,23)),
        ("Libra",(10,23)), ("Scorpio",(11,22)), ("Sagittarius",(12,22)),
        ("Capricorn",(12,32))
    ]
    for sign, (m,d) in zodiac:
        if (b.month, b.day) < (m,d):
            return sign

def next_birthday(birthday):
    today = date.today()
    nxt = birthday.replace(year=today.year)
    if nxt < today:
        nxt = nxt.replace(year=today.year + 1)
    return nxt

def estimate_heartbeats(days):
    avg_bpm = 72
    return days * 24 * 60 * avg_bpm

def milestones(days):
    facts = {
        3650: "🎉 You have lived over 10 years!",
        7300: "🏆 Two decades of memories!",
        10950: "🔥 30 Years Strong!",
        14600: "🌟 40 years of life experience!",
        18250: "👑 Half a century!"
    }
    return [v for k,v in facts.items() if days >= k]

# ------------------------ DISPLAY ------------------------

def show_report(name, birthday):
    years, months, days = calculate_age(birthday)
    sign = zodiac_sign(birthday)
    nxt = next_birthday(birthday)
    days_left = (nxt - date.today()).days
    beats = estimate_heartbeats(days)
    life_milestones = milestones(days)

    print("\n" + "="*60)
    print(f"📊 LIFE ANALYSIS REPORT FOR: {name.upper()}")
    print("="*60)
    print(f"🎂 Birthday            : {birthday}")
    print(f"🧓 Age in Years        : {years}")
    print(f"📆 Age in Months       : {months}")
    print(f"⏳ Age in Days         : {days}")
    print(f"♈ Zodiac Sign         : {sign}")
    print(f"🎉 Next Birthday       : {nxt} ({days_left} days left)")
    print(f"❤️ Estimated Heartbeats: {beats:,}")

    print("\n🏅 LIFE MILESTONES:")
    if life_milestones:
        for m in life_milestones:
            print(" -", m)
    else:
        print(" - Just getting started!")

# ------------------------ MAIN MENU ------------------------

def main():
    print("\n🌌 WELCOME TO LIFE ANALYTICS SYSTEM 🌌")
    name = input("Enter your name: ").title()
    birthday = get_birth_date()

    while True:
        print("\n📜 MAIN MENU")
        print("1. View Full Life Report")
        print("2. Show Zodiac Only")
        print("3. Days Until Next Birthday")
        print("4. Exit Program")

        choice = input("Select option (1-4): ")

        if choice == "1":
            show_report(name, birthday)
            pause()
        elif choice == "2":
            print("\n♈ Your Zodiac Sign is:", zodiac_sign(birthday))
            pause()
        elif choice == "3":
            nxt = next_birthday(birthday)
            print("\n🎉 Your next birthday is in", (nxt - date.today()).days, "days!")
            pause()
        elif choice == "4":
            print("\n👋 Thank you for using Life Analytics System!")
            sys.exit()
        else:
            print("⚠ Invalid choice!")

if __name__ == "__main__":
    main()
