from datetime import datetime

given_date = "Jan 15, 2023 - 12:05:33"

date_object = datetime.strptime(given_date, "%b %d, %Y - %H:%M:%S")

full_month_name = date_object.strftime("%B")
print(f"Full month name: {full_month_name}")

formatted_date = date_object.strftime("%d.%m.%Y, %H:%M")
print(f"Formatted date: {formatted_date}")
