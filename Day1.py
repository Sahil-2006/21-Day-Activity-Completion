# Variables
x = 100
name = "sahil"
pi = 3.14
is_student = True
# input/output
'''Taking Input'''
age = input("Enter your age: ")
print("Your age is :" + age)
print("Sounds Cool")
age = input("Enter new age: ")
print(f"new age is {age}")
print("new age is {}".format(age))
# taking multiple inputs
a, b = input("Enter 2 numbers: ").split()
# type casting
a = int(a)
# better way: input + split + type cast
a, b = map(int, input("Enter two numbers: ").split())
# type casting another input
age = int(input("Enter new age: "))