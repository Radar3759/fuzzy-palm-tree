#find the larges number from scores entered

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_num = 0
for score in student_scores:
  if score > max_num:
    max_num = score
  
  elif score < max_num:
    continue
print(f"The largest number is: {max_num}") 
 

