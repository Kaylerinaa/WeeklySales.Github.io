"""
Karina Lopez
CIS 403
1/13/2023
"""
import datetime


def main():
    print("Programmer: " + os.getlogin() + "a lopez")
    print("Final Project " + time.strftime('%B %d, %Y @ %I:%H:%S\n'))

    name = input("Enter your name: ")
    days = "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
    profit = []
    header = "Enter the sales for "
    total = 0
    for i in days:
        aligned = f"{header}{i}:"
        x = int(input(f"{aligned:35}"))
        profit.append(x)

    for i in profit:
        total += i
    print(f"{name}, here are the results: \n")
    print(f"Total sales for the week:       ${total:,.2f}")
    new_day = input("Which day's sales to display? ")
    index = days.index(new_day)
    print(f"The sales entered for {new_day} is: ${profit[index]:,.2f}")
    new_profit = int(input("Enter new sales amount: "))
    profit[index] = new_profit
    total = 0

    for i in profit:
        total += i
    print(f"The adjusted total sales for the week: ${total:,.2f}")


main()
