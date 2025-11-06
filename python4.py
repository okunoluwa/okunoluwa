#Demo for 
area = 0 
height = 10
width = 20

#Calculate the area of a triangle
area = width * height / 2
 
#printing formatting float value with 2 decimal places
print("the area of the triangle would be %.2f" %area)

#printing the formatted decimal number with right justified to take up 6 spaces
# with leading zero 
print("my favourite number is %06d !" %42)

#do the same thing with the .format syntax to include numbers our output
print("The area of the triangle would be {0:f0}".format(area))
print("My favourite number is {0:d}!".format(42))

#this is an example with multiple number
print(" Here are three numbers"+\
    "The first is {0:d} The second is{1:4d}and the third is {2:d}!".format(7,8,9))

##Demo for storing number (inputting Number)
salary = input("Please enter your Salary: ")
bonus = input("Please enter your Bonus: ")

paycheckAmount = float(salary) + float(bonus)

print(paycheckAmount)

