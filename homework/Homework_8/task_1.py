
import random

salary = int(input("Enter your salary: "))

bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(1, 5000)
    salary += bonus_amount
    print(f"${salary} (Bonus applied: {bonus_amount})")
else:
    print(f"${salary}")
