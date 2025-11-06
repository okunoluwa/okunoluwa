##collect name from user 
ame = input("What is you name? ")
##Displaythe name
print(name)

##update the value
name = 'Christopher Herrison'
print(name)

##Manipulating variable
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
print("Hello " + firstName + " " + lastName)

##collect name from the user 
name = input("What is your name? ")
country = input("What country do you live in? ")
name = name.swapcase()
country = country.upper()


##Create a friendly output
print ('Hello ' + name + " from "+ country) 

##Challenge 
name = input("Enter your favourite character name? ")
age = input("Enter your character age? ")
place = input("Where is the richest country? ")
sport = input("Enter  the most popular sport? ")

name = name.capitalize()
place = place.capitalize()
age = age.lower()
sport = sport.capitalize()

print("My name is "+ name + " I am "+ age +""+ " I am from " + place + " my favourite sport is " + sport )
