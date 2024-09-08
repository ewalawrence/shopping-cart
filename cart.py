# Shopping Cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter the name of food ('q to quite'): ")
    if food.lower() == "q":
        break
    else: 
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print()
print("---------YOUR CART---------")

for food in foods:            
    print(food, end=" ")
for price in prices:
    total += price

print (f"your total is: ${round(total, 2)}")