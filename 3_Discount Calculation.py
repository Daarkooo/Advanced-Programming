total_amount = float(input("Total amount: "))
num_items = int(input("Number of items: "))
day_of_week = input("Day of the week: ").strip().capitalize()


if day_of_week in ["Saturday", "Sunday"]:
    discount = 20  
else:
    discount = 10  

if num_items > 5:
    discount += 5

final_price = total_amount * (1 - discount / 100)

print(f"Total price after discount: {final_price:.1f} dinars")
