menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def show_food_price(order):
    for food in menu:
        if order not in menu:
            print("Sorry, you don't have that food")
            raise ValueError
        elif food == order:
            print(menu[food])
def main():
    done = False

    while True:
        order = input("Item: ").casefold()
        try:
            show_food_price(order)
            print("Success!")
        except ValueError:
            print("Please enter a valid item")

        else:
            break


main()