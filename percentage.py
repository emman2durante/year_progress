from datetime import date

today = date.today()
day_one = date(today.year, 1, 1)
days_past = today - day_one
current_year_days_count = date(today.year, 12, 31) - day_one
print(days_past.days)
print(current_year_days_count.days)
percent = days_past.days / current_year_days_count.days * 100
print(percent)
