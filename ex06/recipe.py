def menu():
    print("\nPlease select an option by typing the corresponding number:\n"
          "1: Add a recipe\n"
          "2: Delete a recipe\n"
          "3: Print a recipe \n"
          "4: Print the cookbook\n"
          "5: Quit")
    check = input()
    if check.isnumeric():
        choose = int(check)
        if choose == 3:
            print_recipe()
        elif choose == 2:
            delete_recip()
        elif choose == 4:
            print_book()
        elif choose == 1:
            add_recip()
        elif choose == 5:
            exit()
        else:
            print("This option does not exist, please")
            menu()
    else:
        menu()


book = {
    'sandwich': {'ingredients': ["ham", "bread", "cheese", "tomatoes"],
                 'meal': 'lunch', 'prep_time': '10'},
    'cake': {'ingredients': ["flour", "sugar", "eggs"],
             'meal': 'dessert', 'prep_time': '60'},
    'salad': {'ingredients': ["avocado", "arugula", "tomatoes", "spinach"],
              'meal': 'lunch ', 'prep_time': '15'},
}


def add_recip():
    name = input("Enter name of recip please.\n")
    ingredients = input(
        "Enter list of ingredients separated with ',' please.\n")
    ingredients = ingredients.split(",")
    meal = input("Enter the type of meal please.\n")
    time = input("Enter time for doing this recip please.\n")
    book[name] = {'ingredients': ingredients, 'meal': meal, 'prep_time': time}


def delete_recip():
    erase = input("Please enter the recipe's name you want delet\n").lower()
    if erase in book:
        del book[erase]
    else:
        print()


def print_recipe(name=""):
    if name == "":
        name = input("Please enter the recipe's name to get its details\n")
        name = name.lower()
    if name in book:
        print("Recipe for " + name + ":" + "\n" +
              "Ingredients list: " + str(book[name]["ingredients"]) + "\n" +
              "To be eaten for " + book[name]["meal"] + "." + "\n" +
              "Takes " + book[name]["prep_time"] + " minutes of cooking\n")
    else:
        print("This recipe does not exist")


def print_book():
    print("This is my beautiful cook book:")
    for r in book:
        print_recipe(r)


while 1:
    menu()
