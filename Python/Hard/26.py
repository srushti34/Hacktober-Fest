from datetime import datetime
date_str = "2024-02-30"
date = datetime.strptime(date_str, "%Y-%m-%d")
print(f"Parsed date: {date}")
