print("Hello, welcome to the coke machine!")
answer = input("Would you like to buy a coke bottle? (y/n) ").lower()

if answer == "y":
    remaining_coins = 50

    while remaining_coins > 0:
        deposit = int(input(f"Please deposit coins (5, 10 or 25 cents). Coins due: {remaining_coins} -> "))

        if deposit == 5 or deposit == 10 or deposit == 25:
            remaining_coins -= deposit
        else:
            print("Invalid coin! Only 5, 10, or 25 cents accepted.")

    if remaining_coins < 0:
        change_owed = abs(remaining_coins)
        print(f"Thanks for buying a coke! You are owed {change_owed} coins!")
    else:
        print("Thanks for buying a coke!")
else:
    print("Understood! You are always welcome! Thanks for visiting!")