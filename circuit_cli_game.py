# Circuit CLI Game - Final project for CS 3102
# Sylvan Moore and Brian Nguyen
# 12/4/2021

# Logic operations to validate input using AON straight line
def AND(a,b):
    return str(int(a)*int(b))

def OR(a,b):
    return str(int(a)+int(b) - int(a)*int(b))

def NOT(a):
    return str(1-int(a))

def XOR(a,b):
    not_a = NOT(a)
    not_b = NOT(b)
    a_not_b = AND(a, not_b)
    b_not_a = AND(b, not_a)
    return OR(a_not_b, b_not_a)

# Helper to ensure input is valid
def is_binary(input):
    for bit in input:
        if bit != '1' and bit != '0':
            return False
    return True

if __name__ == '__main__':
    # Dictionary of problems and their answers
    print("\nWelcome to the Circuit CLI Game by Sylvan and Brian! Enter answers to problems below to play, and ctrl + C to quit.\n")
    problems = {'Problem 1' : '0101', 'Problem 2' : '01001' }
    # Loop through each problem
    for key, value in problems.items():
        guesses = 0
        print(key)
        # Have the user guess until they get the current problem right
        while True:
            user_guess = input("Answer: ")
            # Make sure input is binary
            if not is_binary(user_guess):
                print("Please enter a binary number with no spaces!")
                continue
            guesses += 1
            if user_guess != problems[key]:
                print("Wrong answer, try again!")
            # If the guess is right, proceed to the next problem
            else:
                print("\nRight answer! It took you " + str(guesses) + " trie(s). Here's the next level...\n")
                break