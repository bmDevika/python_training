print("Welcome to pizza Land")
print("Select the toppings from below options")

print("Sizes: ")
print("1.Small,2.Medium,3.large\n please enter integer")
size=int(input("select the size: "))
if size==1:
    print("size=Small")
elif size==2:
    print("size=Medium")
else:
    print("size=Large")

print("Toppings: ")
print ("1.onion,2.capsicum,3.olives\n please enter integer")
toppings=int(input("select the toppings: "))
if size==1:
    print("toppings=onion")
elif size==2:
    print("toppings=capsicum")
else:
    print("toppings=olives")

option=input("Extracheese[y/n]: ")
if option=="y":
    print("your bill is: ")
else:
    print("your bill is: ")    
