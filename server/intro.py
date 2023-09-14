print("Hello world")

first_name = "Irvin"
last_name = "Zavala"
total = 9.99
age = 21
found = True

print(last_name)
print(first_name)
print(total)
print(9+1)
print("9"+"1")

print(10+1)
print(10-1)
print(10*10)
print(10/2)

if(age < 100):
    print("Young boi")
    print("Still  inside if")
elif age == 100:
    print("Century!")
else:
    print("Too old sir")
print("Outside if")


def say_hello(name):
    print("Hello " + name + " from function")
    
say_hello("")
say_hello("Irvin")
say_hello("Eduardo")