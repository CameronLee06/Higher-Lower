 
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
    print(
        """
    **** How To Play ****

    You will start by choosing 2 numbers of your choice to guess between.

    Then the computer will choose a number at random between your 2 chosen numbers.

    You will then have a specific amount of guesses ranging from how big the difference in your 2 numbers is.

    You will guess a number and the computer will say either higher or lower to get you closer to your number.


    ****Good Luck!****
        """
    )
    return ""

show_instructions = yes_no("Do you want to see the instructions?" )

if show_instructions == "yes":
    instructions()
else:
    print("Program Continues")
   
    import random


def check_rounds():
    while True:
        response = input("Choose 2 starting numbers (1 higher and 1 lower): ")

        round_error = "Please type either <enter> / or an integer that is more than 0"
        if response != "":
            try: 
                response = int(response)

                if response <1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response



# Main routine goes here...

rounds_played = 0 
choose_instruction = "Please choose rock (r) , paper / (p) or scissors (s) or 'xxx' to end"


# Ask user for # rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game =="no":

    # Rounds Heading 
    print()
    if rounds == "":
        heading = "Infinite Mode: Round {}".format(rounds_played + 1)
        print(heading)

    else: 
        heading = "Round {} of {}".format(rounds_played + 1, rounds)


    print(heading)
    choose = input(choose_instruction)


    # End game if exit code is typed
    if choose == "xxx" or rounds_played == rounds - 1:
        break

    # rest of loop / game
    print("You chose {}".format(choose))

    rounds_played +=1

print("Thank you for playing")
