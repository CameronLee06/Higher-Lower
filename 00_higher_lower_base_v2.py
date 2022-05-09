 
import random

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

# Number checking function goes here
def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)
            
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            
            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue


# ***** Main Routine ******
show_instructions = yes_no("Do you want to see the instructions?" )

if show_instructions == "yes":
    instructions()

# Ask user for # of rounds..
rounds = intcheck("How many rounds <enter> for infinite: ", 1, exit_code = "")

if rounds == "":
    print("you chose infinite mode")
else:
    print("you asked for {} rounds".format(rounds))

# checks that response is an integer    
low_num = intcheck("Low Number: ")
print("You chose a low number of ", low_num)

# checks that response is an integer more than the low number
high_num = intcheck("High Number: ", low_num)
print("You chose a high number of ", high_num)

# loop four times for easy testing
for item in range(0, 4):
    
    # checks that the response is either the exit code
    # or a number between low_num and high_num
    guess = intcheck("Guess: ", low_num, high_num, "xxx")
    print("You guessed {}".format(guess))


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



# get user input (low number, high number and number of rounds)


rounds_played = 0 


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
    guess = input("Guess")


    # End game if exit code is typed
    if guess == "xxx" or rounds_played == rounds - 1:
        break

    # rest of loop / game
    print("You chose {}".format(guess))

    rounds_played +=1

print("Thank you for playing")
