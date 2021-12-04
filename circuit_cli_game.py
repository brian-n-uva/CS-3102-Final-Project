# Circuit CLI Game - Final project for CS 3102
# Sylvan Moore and Brian Nguyen
# 12/4/2021

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
            guesses += 1
            if user_guess != problems[key]:
                print("Wrong answer, try again!")
            # If the guess is right, proceed to the next problem
            else:
                print("\nRight answer! It took you " + str(guesses) + " tries. Here's the next level...\n")
                break