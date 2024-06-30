print("Welcome to the CUIGEAR Pizza Deliveries!")

size = input("What size of Pizza do you want? S , M or L?")

add_pepperoni = input ("Do you want to add some pepperoni? Y or N?")

extra_cheese = input ("Do you need extra cheese? Y or N?")

bill = 0

if size == "S":
    bill += 19
elif size == "M":
    bill += 29
elif size == "L":
    bill += 39
else:
    print("Sorry! Input your order correctly.")

if add_pepperoni == "Y":

    if size == "S":
        bill += 2.9
    else:
        bill += 4.9
if extra_cheese == "Y":
    bill += 1.9

print (f"Your final bill is: ${bill}")