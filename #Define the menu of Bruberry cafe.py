#Define the menu of Bruberry cafe
menu={'pizza':40,
      'pasta':50,
      'burger':60,
      'Salad':70,
      'coffie':80
      }
#Greet
print('Welcome to Bruberry cafe')
print(" pizza:40\n pasta:50\n Burger:60\n Salad:70\n Coffie:80")

order_total=0
#80+70=150
item_1=input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]#0+50
    print("Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")
another_order=input("Do you want to add another item? (Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name of the Second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Oredered item {item_2} is not Available!")
    print(f"Total amount of the item to pay {order_total}")