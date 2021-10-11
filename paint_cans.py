import math

def paint_calc(height, width, cover):
  num_can = (height * width) / cover
  cans_rounded = int(math.ceil(num_can))
  #print(num_can)
  print(f"You need: {cans_rounded} cans of paint.")






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
