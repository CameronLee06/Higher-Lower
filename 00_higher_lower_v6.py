 
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

# initialise variables, set up holding list for game history
rounds_played = 0 
rounds_lost = 0
mode = "regular"

end_game = "no"

game_summary = []


# Get user input
show_instructions = yes_no("Do you want to see the instructions?" )

if show_instructions == "yes":
    instructions()

# checks that response is an integer    
low_num = intcheck("Low Number: ")

# checks that response is an integer more than the low number
high_num = intcheck("High Number: ", low_num)


# calculate max guesses below
max_guesses = 3

# Ask user for # of rounds..
rounds = intcheck("How many rounds <enter> for infinite: ", 1, exit_code = "")


print()
if rounds == "":
    mode = "infinite"
    rounds = 3

# Ask user for # rounds, <enter> for infinite mode

while rounds_played < rounds and end_game == "no":
    
    rounds_played += 1
    guesses_allowed = max_guesses
    guesses_used = []

    print()
    if mode == "infinite":
        heading = "Infinite Mode: Round {}".format(rounds_played)
    else: 
        heading = "Round {} of {}".format(rounds_played, rounds)

    print(heading)
    
    # generate the secret number
    secret = random.randint(low_num, high_num)
    print("Spoiler alert", secret)
    print()



    if mode == "infinite":
        rounds += 1


    guess = ""
    while guess != secret and len(guesses_used) <= guesses_allowed:

        guesses_left = guesses_allowed - len(guesses_used)
    # Put guessing and comparing loop here.
        guess = intcheck("Guess: ", low_num, high_num, "xxx")
    
        if guess in guesses_used:
            print("you already guessed that number! please try again,"
            " You still have {} guesses left".format(guesses_left, guesses_used))
            continue

        guesses_used.append(guess)
        
        # HLcomponent 11- Maximum Guesses Calculator

    import math

    for item in range(0,4):

        low = int(input("Low: "))
        high = int(input("High"))

        range = high - low + 1
        max_raw = math.log2(range)
        max_upped = math.ceil(max_raw)
        max_guesses = max_upped + 1
        print ("Max Guesses: {}".format(max_guesses))

        print()
        # End game if exit code is typed
         
        if guess == "xxx" or rounds_played > rounds:
            end_game = "yes"
            break

        elif guess == secret:
            feedback = "Well done, you got it in {} guesses".format(len(guesses_used))
            break
        if guess <= secret:
            print ("Higher")
        elif guess >= secret:
            print ("Lower")

        if len(guesses_used) >= guesses_allowed:
            feedback = "sorry you lose"
            rounds_lost += 1
            #end_game = "yes"
            break

    outcome = "Round {}: {}".format(rounds_played, feedback)
    game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost

# **** Calculate Game Stats ******
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100


print()
print ("***** Game History *****")
for game in game_summary:
    print(game)

print()
# displays game stats with % values to the nearest whole number
print("******* Game Statistics *******")
print ("Win {}, ({:.0f}%) \nLoss: {}, " "({:.0f}%)".format(rounds_won,percent_win,rounds_lost,percent_lose))

print("Thank you for playing")