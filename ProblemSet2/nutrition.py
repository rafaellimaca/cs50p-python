foods = {"apple": 130,
         "avocado": 50,
         "banana": 100,
         "cantaloupe": 50,
         "grapefruit":60
         }
Item = input("Enter your item: ").lower()
output = ""
for food in foods:
    if(food == Item):
        print(foods[food])