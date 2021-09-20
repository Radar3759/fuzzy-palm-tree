# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "s":
  bill = 15
elif size == "m":
  bill = 20
else:
  bill = 25

#add cheese
if extra_cheese == "y":
  bill += 2

#pepperoni
if add_pepperoni == "n":
  bill = bill
elif add_pepperoni == "y" and size == "s":
  bill += 2
elif add_pepperoni == "y" and size == "m" or size == "l":
  bill += 3


print(bill)

