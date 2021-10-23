print("The price of the apples is ₱20 and the price of the oranges is ₱25.")
apple_price = 20
orange_price = 25
apple = input("Please indicate how many apples you want to purchase: ")
orange = input("Please indicate how many oranges you want to purchase: ")
apple_str= int(apple)
orange_str= int(orange)
total_apple = (apple_str * apple_price)
total_orange = (orange_str * orange_price)
grandtotalprice = (total_apple + total_orange)
print(f"The total amount of your purchase is ₱{grandtotalprice}.")