# price at 0
# get number of items
# error check for correct items
# iterate each item
# apply discount if total  > 100

total_price = 0
number_of_items = int(input(f"Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input(f"Number of items: "))
for i in range(1, number_of_items + 1):
    item_price = float(input(f"Price of item: "))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
