# 1922 Gibson L-5 CES for about $16,036!

def main():
    """This function will print"""
    year_of_guitar = 1922
    type_of_guitar = "Gibson"
    model_of_guitar = "L-5 CES"
    price_of_guitar = 16035.9
    print(f"{year_of_guitar} {type_of_guitar} {model_of_guitar} for about ${price_of_guitar:,.0f}!")
    powers()


def powers():
    """This function will print powers of 2 from 0 to 10"""
    for i in range(11):
        print(f"2  ^ {i:2} is {2 ** i:4}")


main()
