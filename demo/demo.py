# importing os module 
from os import system, name

# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

#create a global list of animals
animals = ['lion', 'tiger', 'cheetah', 'panther', 'leopard']

print("Welcome to the animal zoo!")
print("Here are the animals in the zoo:")
print(animals)

# Function to add an animal to the list
def add_animal():
    new_animal = input("Enter the name of the animal to add: ")
    animals.append(new_animal)
    print(f"The {new_animal} has been added to the zoo!")
    print("Here are the animals in the zoo now:")
    print(animals)

# Function to remove an animal from the list
def remove_animal():
    remove_animal = input("Enter the name of the animal to remove: ")
    if remove_animal in animals:
        animals.remove(remove_animal)
        print(f"The {remove_animal} has been removed from the zoo!")
        print("Here are the animals in the zoo now:")
        print(animals)
    else:
        print("The animal is not in the zoo!")


# Main loop

while True:
    print("What would you like to do?")
    print("1. Add an animal")
    print("2. Remove an animal")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_animal()
    elif choice == "2":
        remove_animal()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")