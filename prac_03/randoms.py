# print(random.randint(5, 20))
# smallest number was 5 , largest number was 15

# print(random.randrange(3, 10, 2))
# smallest number was 5 , largest number was 9
# No as it stars as a count from 3 adding 2 up to 10 , resulting in odd numbers

# print(random.uniform(2.5, 5.5))
# smallest number was 3.2285255870224523, largest number was 5.448057854999945

import random


def main():
    """This function will produce a randome number between 1 and 100 inclusive."""

    print(random.randint(1, 100))


main()
