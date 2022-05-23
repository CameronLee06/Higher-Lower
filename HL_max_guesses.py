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