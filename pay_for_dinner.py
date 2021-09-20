# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random 

#print names to test split
print(names)
#find length of names array
x = len(names)
#test len
#print(x)

#don't use random.choice 
num = random.randint(0, x -1)
who_pays = names[num]
print(f"The person who pays for the meal is {who_pays}.")

#use random.choice
pays = (random.choice(names))
print(f" The person who pays for the meal is {pays}.")

