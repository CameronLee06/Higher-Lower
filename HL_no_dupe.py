SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = [] 
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:
    guess = int("Guess: ")

    if guess in already_guessed:
        print("you already guessed that number! please try again"
        "You still have {} guesses left".format(guesses_left, already_guessed))
        continue

guesses_left -= 1
already_guessed.append(guess)
