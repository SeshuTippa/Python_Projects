menu = {
    "chicken Biryani":"200",
    "mutton Biryani" : "250",
    "Fish Biryani" : "300",
    "Prawns Biryani" : "350"
}

for item,price in menu.items():

    print("Welcome to our Restaurent")

    print("Below is the Menu and its prices")

    print(f"The name of the item is {item} and price of the item is {price}.")

    print("\n")

order_1 = input("please select the order in the menu:")

if order_1 in menu:

    print(f"The item you have ordered is {order_1}")

    quantity = int(input("Please enter the Quantity:"))

    price = int(menu[order_1]) * quantity        #300*2=600

    print(f"The item you have ordered is {order_1} and price of the item is {price}")
# else:
#     print(f"sorry {order_1} is not availale")

    add_more = input("Are you want to add another oreder yes/no:")

    if add_more == 'yes':

        print("Please place the another order:")

        order_2 = input("Please select the order from the menu:")

        if order_2 in menu:

            print(f"The item you have ordered is {order_2}")

            quantity = int(input("Please enter the quantity:"))

            price_2 = int(menu[order_2]) * quantity

            print(f"The item you have ordered is {order_2} and the cost is RS.{price_2}")

            total_price = price +price_2

            print(f"The total price of the two items are :{total_price}")
        else:
            print(f"Sorry,The selected item {order_2} is not available")

print("Thank you visit again😊❤️")





# print(300*2)
