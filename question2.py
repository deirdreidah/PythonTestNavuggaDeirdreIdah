# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

#2
percentage = int(input("Enter the mark scored: "))
if 90<= percentage <=100:
 print("Grade A") 
elif 80<= percentage <=89:
 print("Grade B")
elif 70<= percentage <=79:
 print("Grade C")
elif 60<= percentage <=69:
 print("Grade D")
elif 40<= percentage <=59:
 print("Grade E")
else:
 print("Grade F")



