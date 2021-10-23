money = float(input("How much money do you have? "))
apple = int(input("What is the price of an apple per piece? "))

maximumNumberApples= money // apple

change = money % apple
print(f"You can buy {maximumNumberApples} apples and your change is ₱{change: .2f}.")