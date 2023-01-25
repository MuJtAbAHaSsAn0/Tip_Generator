#string 

print("Hello"[0])
# Result = H


# Integers

print(123 + 896)
# Result = 1019


# Float 

print(34.43)
# Result = 34.43 


# Boolean 

print(True, False)
# Result = True, False


# string + integer

my_name = input("Your name character is ")
new_name = str(my_name)
print("Your name contain " + new_name +" letters")
#Reslut = Your name contain "new_name" letters


# Check Type 
a = int(34)
print(type(a))
# Result = <integer>


# Adding two random numbers

two_digit_number = input("Type a two digit number: 34")
a = int(two_digit_number[0])
b = int(two_digit_number[1])
c = a + b
print(c)
# Result = 7


# Using F-String
height = 7.5
weight = 95
print(f"your height is {height} and weight is {weight}")