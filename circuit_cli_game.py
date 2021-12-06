# Circuit CLI Game - Final project for CS 3102
# Sylvan Moore and Brian Nguyen
# 12/4/2021

# Ascii art circuit problems to display to the terminal, used in main
CIRCUIT_PROBLEMS = [
'      *Input*\n'
'   [_]      [_]\n'
'    |____    |\n'
'    |    |   |\n'
'    |   NOT  |\n'
'    |   \-/  |\n'
'    |    v   |\n'
'    |    o   |\n'
'    |   _|   |_\n'
'    |  |  \_/  |\n'
'    |  \   OR  /\n'
'    |   \     /\n'
'    |     \ /\n'
'    |_    _|\n'
'      |   |\n'
'     _|___|_\n'
'    |       |\n'
'    |  AND  |\n'
'    [       ]\n'
'     \ ___ /\n'
'        |\n'
'        |\n'
'     *Output*\n',

'         *Input*\n'
' [_]   [_]     [_]    [_]\n'
'  |    _|___    |      |\n'
'  |   |     |   |     NOT\n'
'  |  NOT    |   |     \-/\n'
'  |  \-/    |   |      v\n'
'  |   v     |   |      o\n'
'  |   o     |   |      |\n'
' _|   |_   _|___|_     |\n'
'|  \_/  | |       |    |\n'
'\  NOR  / |  AND  |    |\n'
' \     /  [       ]    |\n'
'   \ /     \ ___ /     |\n'
'    o         |        |\n'
'    |__     __|__     _|\n'
'       |   |     |   |\n'
'      _|   |_   _|___|_ \n'
'     |  \_/  | |       |\n'
'     \  OR   / |  AND  |\n'
'      \     /  [       ]\n'
'        \ /     \ ___ /\n'
'         |__     __|\n'
'           _|   |_\n'
'           _|\_/|_\n'
'          |  \_/  |\n'
'          \  XOR  /\n'
'           \     /\n'
'             \ /\n'
'              |\n'
'              |\n'
'           *Output*\n'
]

# Simulates circuit 1
def circuit_1(bits):
    return bits[0] and bits[1]

# Simulates circuit 2
def circuit_2(bits):
    return (not bits[0] or bits[2]) and bits[1] and (not bits[2] or bits[3])

# Helper to ensure input is valid
def is_binary(input):
    for bit in input:
        if bit != '1' and bit != '0':
            return False
    return True

if __name__ == '__main__':
    # Dictionary which maps circuit problems to functions that perform their logic and their number of inputs
    print("\nWelcome to the Circuit CLI Game by Sylvan and Brian! Enter answers to problems below to play, and ctrl + C to quit.\n")
    problems = {CIRCUIT_PROBLEMS[0] : (circuit_1, 2), CIRCUIT_PROBLEMS[1] : (circuit_2, 4) }
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
            # Are the wrong number of bits provided?
            if len(user_guess) != problems[key][1]:
                print("Please enter the correct number of input bits!")
                continue
            guesses += 1
            # Is the guess wrong?
            # Extract the input
            guess_bits = []
            for bit in user_guess:
                guess_bits.append(int(bit))
            # Simulate circuit with the input
            is_correct = problems[key][0](guess_bits)
            if not is_correct:
                print("Wrong answer, try again!")
            # If the guess is right, proceed to the next problem
            else:
                print("\nRight answer! It took you " + str(guesses) + " trie(s). Here's the next level...\n")
                break