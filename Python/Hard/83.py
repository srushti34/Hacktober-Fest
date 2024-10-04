from datetime import datetime

def calculate_days_between(d1, d2):
    try:
        date_format = "%Y-%m-%d"
        start = datetime.strptime(d1, date_format)
        end = datetime.strptime(d2, date_format)
        delta = end - start
        return delta.days
    except ValueError as e:
        print(f"ValueError: {e}")

def main():
    date1 = "2023-09-15"
    date2 = "2023/09/20"  
    days_between = calculate_days_between(date1, date2)
    print(f"Days between: {days_between}")

main()
