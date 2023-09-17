# global vars
from config import developer


# functions
def print_menu():
    print("------------------------")
    print("----   Irvin Soft   ----")
    print("------------------------")
    
def dictionary_1():
    pet = {
        "type" : "Dog",
        "name" : "Junior",
        "color": "Brown",
        "age"  :  2
    }
    
    print("My pet is " + pet["name"])
    
    pet["age"] = 99
    pet["size"] = "big"
    pet.pop("type")
    print(pet)

def dictionary_2():
    print(developer)
    print("My name is " + developer["first"] + " " + developer["last"])
    print("My address is " + str(developer["address"]["num"]) + " " + developer["address"]["city"])

# plain instructions
# function calls
print_menu()
dictionary_1()
dictionary_2()