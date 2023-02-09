# 30-11-22
months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "Augest", 9: "September", 10: "October", 11: "November", 12: "December"}
total_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
day_suffixes = {"0": "th", "1": "st", "2": "nd", "3": "rd", "4": "th", "5": "th", "6": "th", "7": "th", "8": "th", "9": "th"}

def format_date(date):
    if date.count("/") != 2: return "INVALID DATE"
    day, month, year = date.split("/")
    try: day, month, year = int(day), int(month), int(year)
    except ValueError: return "INVALID DATE"
    if day < 1 or month < 1 or month > 12 or year < 1000 or day > total_days[month] + int(month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)): return "INVALID DATE"
    return f"{months[month]} {day}{day_suffixes[str(day)[-1]] if day < 11 or day > 13 else 'th'}, {year}"

dates = input("Input dates (DD/MM/YYYY, DD/MM/YYYY, ...): ").replace(" ", "").replace(";", ",").replace("-", "/").split(",")
print("Formatted dates: " + "; ".join(map(format_date, dates)))
