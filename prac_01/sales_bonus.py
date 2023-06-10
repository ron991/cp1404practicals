"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get sales
while sales >= 0
    calculate bonus
    get sales
do next thing
"""


def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        if sales < 1000:
            sales_bonus = sales * 0.1
        else:
            sales_bonus = sales * 0.15
        print("Sales bonus is $", sales_bonus, sep='')
        sales = float(input("Enter sales: $"))


main()
