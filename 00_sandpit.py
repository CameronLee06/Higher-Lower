 
def yes_no(question):

    valid = False
    while not valid:
        response = input(question).lower()

        # strip removes white space before / after a string
        response = response.strip()

        if response== "yes" or response== "y":
            return "yes"

        elif response == "n" or response== "no":
            return "no"

        else:
            print("Please answer yes / no")


def instructions():
    print("**** How To Play ****")
    print()
    print("You will start by choosing 2 numbers of your choice to guess between.")
    print()
    return ""

show_instructions = yes_no("Do you want to see the instructions?" )

if show_instructions == "yes":
    instructions()
else:
    print("Program Continues")