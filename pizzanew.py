print("Welcome to pizza Land")
print("Select the toppings from below options")
bill = 0
print("Sizes: ")
print("Small, Medium,large")
size=(input("select the size: "))
if size=="small":
    bill += 5
elif size=="Medium":
    bill += 10
else:
    bill += 15
print("Toppings: ")
print ("onion,capsicum,olives")
toppings=(input("select the toppings: "))
if toppings =="onion":
    bill += 3
    print(f"You have selected a {toppings} pizza")
elif toppings=="capsicum":
    bill += 5
    print(f"You have selected a {toppings} pizza")
else:
    bill += 8
    print(f"You have selected a {toppings} pizza")
option=input("Extracheese[y/n]: ")
if option == "y":
    bill += 15
else:
    print("you have not selected the cheese")    
print(f"You have selected {size} pizza and the topping is {toppings}")
print(f"Yor total bill is {bill} ")