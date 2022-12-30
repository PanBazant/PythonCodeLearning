def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"Year {year} is leap")
            else:
                print(f"Year {year} is not leap")
        else:
            print(f"Year {year} is leap")
    else:
        print(f"Year {year} is not leap")

def days_in_month():
    """Docstring wyświetla się po najechaniu kursorem na funkcje
        opis funkcji
        """
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)