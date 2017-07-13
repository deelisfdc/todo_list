"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""

    item = raw_input("What would you like to add? ")
    print item

            
    my_list.append(item)


def view_list(my_list):
    """Print each item in the list."""
    for items in my_list:
        print items
    # print "The view_list function has not yet been written"


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
    >>> """
    # print user_options
    while True:
        user_choices = raw_input(user_options).upper()
        if user_choices == "A":
            add_to_list(my_list)
        elif user_choices == "B":
            view_list(my_list)
        elif user_choices == "C":
            break  

        #     user_options.upper()
        #     print "Add new item"
        #     item = raw_input("What would you like to add? ")
        #     item.append(my_list)
         
        # Collect input and include your if/elif/else statements here.
       
#-------------------------------------------------

my_list = []
display_main_menu(my_list)

