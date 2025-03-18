#Define the menu of restaurent
menu = {
    'Pizza': 100,
    'Pasta': 80,
    'Bueger': 70,
    'Salad': 60,
    'Coffee': 30,
    'Tea': 15,
}
print("Welcome to our restaurent")
print("Pizza : Rs 100\n Pasta : Rs 80\n Berger : Rs 70\n Salad : Rs 30\n Coffee : Rs 30\n Tea : Rs 15")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print (f"Oredered item {item_1} is not available yet !")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2= input("Enter the second item = ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item{item_2} has been added to order")
    
    else:
        print(f"Ordered item {item_2} is not available!")

print(f" the total amount of items to pay is {order_total}")


