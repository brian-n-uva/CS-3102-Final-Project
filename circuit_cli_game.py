# Circuit CLI Game - Final project for CS 3102
# Sylvan Moore and Brian Nguyen
# 12/4/2021

# Ascii art for menus
MENUS = [
'        ________\n'
'       [  [11]  ]\n'
'       [________]\n'
'       /  \  /  \\\n'
'       \ _/__\_ /\n'
'        \_|__|_/\n'
' ________\____/________\n'
'|    |            |    |\n'
'|____|            |____|\n'
' |[1]|    /  \    |   |\n'
' |___|___/    \___|___|\n'
' |   |            |   |\n'
' |   |            |   |\n'
' |   |   ______   |   |\n'
' |___|  | [10] |  |___|\n'
' \   |  |______|  |   /     _________\n'
'  \__|    ____    |__/    (/ Robot  /,\n'
'     |   |    |   |      (/ Manual //\n'
'     |   |    |   |     (/  [0]   //\n'
'     |___|    |___|    (/________//\n'
'     |   |    |   |    (|_______(/\n'
'     |___|    |___|\n'
'     |   |    |   |\n'
'  ___|___|    |___|___\n'
' |       |    |       |\n'
' |_______|    |_______|\n',

'                                  _____\n'
'    __________________   ________/ !!! \___\n'
'.-/|                  \ /                  |\-.\n'
'||||  ~~~~~~~~~~~~~    | EMERGENCY SHUTOFF ||||\n'
'||||  ~~~~~~~~~~~~~    |                   ||||\n'
'||||    ~~~~~~~~~~~    | There are three   ||||\n'
'||||                   | panels with       ||||\n'
'||||    ~~~~~~~~       | circuitry on the  ||||\n'
'||||                   | robots body.      ||||\n'
'||||  ~~~~~~~~~~~~~    | Make each circuit ||||\n'
'||||  ~~~~~~~~~~~~~    | evaluate to true  ||||\n'
'||||  ~~~~~~~~~~~~~    | to turn off the   ||||\n'
'||||  ~~~~~~~~~~~~~    | robot.            ||||\n'
'||||__________________ | __________________||||\n'
'||/___________________\|/___________________\||\n'
'                     \___/     \n',


]

# Ascii art for the story/plot of the game
STORY_SCENES = [
'                                         |\n'
'                                         |\n'
'                                         |\n'
'                                         |\n'
'   _______                   ________    |\n'
'  |ooooooo|      ____       | __  __ |   |\n'
'  |[]+++[]|     [____]      |/  \/  \|   |\n'
'  |+ ___ +|     (o)(o)      |\__/\__/|   |\n'
'  |:|   |:|   ___\__/___    |[][][][]|   |\n'
'  |:|___|:|  |__|    |__|   |++++++++|   |\n'
'  |[]===[]|   |_|_/\_|_|    | ______ |   |\n'
'_ ||||||||| _ | | __ | | __ ||______|| __|\n'
'  |_______|   |_|[::]|_|    |________|   \\\n'
'              \_|_||_|_/                  \\\n'
'                |_||_|                     \\\n'
'               _|_||_|_                     \\\n'
'      ____    |___||___|                     \\\n'
'     /  __\          ____                     \\\n'
'     \( oo          (___ \                     \\\n'
'     _\_o/           oo~)/\n'
'    / \|/ \         _\-_/_\n'
'   / / __\ \___    / \|/  \\\n'
'   \ \|~~~|)_/_)  / / .- \ \\\n'
'    \/_)~ |)      \ \ .  /_/\n'
'     ||___|)       \/___(_/\n'
'     | | |          | |  |\n'
'     | | |          | |  |\n'
'     |_|_|          |_|__|\n'
'     [__)_)        (_(___]\n',



'       _.-^^---....,,--\n'
'   _--                  --_\n'
'  <                        >)\n'
'  |                         |\n'
'   \._                   _./\n'
'      ```--. . , ; .--\n'
'            | |   |\n'
'         .-=||  | |=-.\n'
'         `-=#$%&%$#=-\n'
'            | ;  :|  ___\n'
'     ___.,-#%&$@%#&#~,. |____\n'
'    /______________|[][]|____\  \n'
'    |[X] [X] [][]  |[][]|[X] |_____\n'
'    |              |    |    |_____\ \n'
'    |              |[]|||     [_]|||\n'
'  ===================================\n'
'  -  -  -  -  -  -  -  -  -  -  -  -  -\n'
'=========================================\n',


'                                        \|  _\n'
'   / / / /                    / / / /    | /\n'
'   \ \ \ \                    \ \ \ \    |/\n'
'   /_/_/_/                   _/_/_/_/    |\n'
'  |o-o-oo\       ____       | __  __ |   |\n'
'  |[]++-[)\     [____]      |/\ \)_/\|   |\n'
'  |?  __ +|     (\)(/)      ||_\/\_\/|   |\n'
'  |: _/ |:|   ___\__/___    |[]*][][]|   |\n'
'  |:|___|:|  |__|    |__|   |+-+-+-++|   |\n'
'  |[]=/=[]|   |_|_/\_|_|    | ______ |   |\n'
'_ |||\||/|| _ | | __ | | __ ||_?__?_|| __|\n'
'  |_______|   |_|[::]|_|    |________|   \\\n'
'              \_|_||_|_/                  \\\n'
'                |_||_|                     \\\n'
'      \ \ \    _|_||_|_                     \\\n'
'      /_/_/   |___||_\_\ \                  |\\\n'
'     {  __}          /_/_/                   | \--\n'
'     \(x x          {___ }                 /   \\\n'
'     _\_o/           x x)/\n'
'    / \ / \         _\o_/_\n'
'   / / __\ \       / \ /  \\\n'
'   \ \|~~~|)\     / /    \ \\\n'
'    \_) ~ |)_)    \_\    / /\n'
'     ||___|)       \ )__(_/\n'
'     | | |          | |  |\n'
'     | | |          | |  |\n'
'     | | |          | |  |\n'
'     [__)_)        (_(___]\n',


]

STORY_SCENES_CAPTIONS = [
    'In the year 3012, scientists invented a new super-robot that would be able to mine bitcoin 3000000.00% faster than any robot before. Press any key to continue...',
    'BOOM!!! Press any key to continue...',
    'It turns out that the robot was evil and wanted to destroy all life. Press any key to continue...',
]

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
'           *Output*\n',

'                  *Input*\n'
'    [_]       [_]   [_]      [_]       [_]\n'
'     |         |     |    ____|_____    |\n'
'     |    _____|____,|,_,|,_____    |   |\n'
'     |   |     |     |   |      |   |   |\n'
'     |   |     |     |  NOT     |   |   |\n'
'     |   |     |     |  \-/     |   |   |\n'
'    _|   |_    |     |   v     _|   |_  |\n'
'   |  \_/  |  NOT    |   o     _|\_/|_  |\n'
'   \  NOR  /  \-/   _|___|    |  \_/  | |\n'
'    \     /    v   |       |  \  XOR  / |\n'
'      \ /      o   |  AND  |   \     /  |\n'
'       o       |   [       ]     \ /    |\n'
'       |       |    \ ___ /       |     |\n'
'       |    __,|,_____,|,________,|,____|\n'
'       |   |   |       |      |   |     \n'
'       |   |   |___    |      |   |\n'
'      _|___|_     _|   |_    _|   |_\n'
'     |       |    _|\_/|_   |  \_/  |\n'
'     |  AND  |   |  \_/  |  \   OR  /\n'
'     [       ]   \  XOR  /   \     /\n'
'      \ ___ /     \     /      \ /\n'
'         |          \ /         |\n'
'         |    _______|    ______|\n'
'         |   |       |   |  \n'
'         |  NOT      |   | \n'
'         |  \-/      |   | \n'
'         |   v       |   | \n'
'         |   o       |   |\n'         
'        _|   |_      |   |\n'
'        _|\_/|_     _|___|_\n'
'       |  \_/  |   |       |\n'
'       \  XOR  /   |  NAND |\n'
'        \     /    [       ]\n'
'          \ /       \ ___ /\n'
'           |           o \n'
'           |___     ___|\n'
'               |   |\n'
'              _|___|_\n'
'             |       |\n'
'             |  AND  |\n'
'             [       ]\n'
'              \ ___ /\n'
'                 |\n'
'                 |\n'
'              *Output*\n',

]

# Simulates circuit 1
def circuit_1(bits):
    return bits[0] and bits[1]

# Simulates circuit 2
def circuit_2(bits):
    return (not bits[0] or bits[2]) and bits[1] and (not bits[2] or bits[3])

# Simulates circuit 3
def circuit_3(bits):
    return (not bits[0] and not bits[1] and bits[3]) or (bits[1] and bits[3] and bits[4]) or (not bits[1] and bits[2] and not bits[3] and bits[4])

# Helper to ensure input is valid
def is_binary(input):
    for bit in input:
        if bit != '1' and bit != '0':
            return False
    return True

if __name__ == '__main__':
    # Prologue
    print("\nWelcome to the Circuit CLI Game by Sylvan and Brian! Enter answers to problems below to play, and ctrl + C to quit.\n")
    for i in range(3):
        print(STORY_SCENES[i] + '\n')
        exit = input(STORY_SCENES_CAPTIONS[i])
    # Dictionary which maps circuit problems to functions that perform their logic and their number of inputs
    problems = {CIRCUIT_PROBLEMS[0] : (circuit_1, 2), CIRCUIT_PROBLEMS[1] : (circuit_2, 4), CIRCUIT_PROBLEMS[2] : (circuit_3, 5) }
    problems_solved = [False, False, False]
    menu_options = {'0', '1', '10', '11'}
    while True:
        if problems_solved[0] and problems_solved[1] and problems_solved[2]:
            exit = input('Congratulations! You defeated the evil robot! You receive $1,000,000 dollars and everyone likes you now. The End. Press any key to continue...')
            print('\nMade by Brian Nguyen and Sylvan Moore\n')
            print('With ASCII Art from Brian Green, Tom Harvey, Jussi Roine and jro\n')
            break
        print(MENUS[0] + '\n')
        option_chosen = input('After hours of searching, you find the robot in the ruins of the lab on cooldown after its attack. Nows your chance to figure out a way to shut it off. Choose an option to continue... (0, 1, 10, or 11): ')
        if option_chosen in menu_options:
            if option_chosen == '0':
                print(MENUS[1] + '\n')
                exit = input('Somehow this book survived the blast. Perhaps it has some useful information in it. Too bad you are a STEM major and cannot read. Press any key to continue...')
            elif option_chosen == '1':
                print('\nSolve the arm circuit by entering a 2-digit binary number to designate its input. Enter q to go back\n')
                guesses = 0
                print(CIRCUIT_PROBLEMS[0])
                # Have the user guess until they get the current problem right, or they quit
                while True:
                    user_guess = input("Answer: ")
                    # If they wish to go to the menu
                    if user_guess == 'q':
                        break
                    # Make sure input is binary
                    if not is_binary(user_guess):
                        print("Please enter a binary number with no spaces!")
                        continue
                    # Are the wrong number of bits provided?
                    if len(user_guess) != problems[CIRCUIT_PROBLEMS[0]][1]:
                        print("Please enter the correct number of input bits!")
                        continue
                    guesses += 1
                    # Extract the input
                    guess_bits = []
                    for bit in user_guess:
                        guess_bits.append(int(bit))
                    # Simulate circuit with the input
                    is_correct = problems[CIRCUIT_PROBLEMS[0]][0](guess_bits)
                    # Is the guess wrong?
                    if not is_correct:
                        print("You set the inputs to the circuit. It doesnt seem to do anything")
                    # If the guess is right, proceed to the next problem
                    else:
                        print("\nRight answer! It took you " + str(guesses) + " trie(s). Let's try another...\n")
                        problems_solved[0] = True
                        break
            elif option_chosen == '10':
                print('\nSolve the body circuit by entering a 4-digit binary number to designate its input. Enter q to go back\n')
                guesses = 0
                print(CIRCUIT_PROBLEMS[1])
                # Have the user guess until they get the current problem right, or they quit
                while True:
                    user_guess = input("Answer: ")
                    # If they wish to go to the menu
                    if user_guess == 'q':
                        break
                    # Make sure input is binary
                    if not is_binary(user_guess):
                        print("Please enter a binary number with no spaces!")
                        continue
                    # Are the wrong number of bits provided?
                    if len(user_guess) != problems[CIRCUIT_PROBLEMS[1]][1]:
                        print("Please enter the correct number of input bits!")
                        continue
                    guesses += 1
                    # Extract the input
                    guess_bits = []
                    for bit in user_guess:
                        guess_bits.append(int(bit))
                    # Simulate circuit with the input
                    is_correct = problems[CIRCUIT_PROBLEMS[1]][0](guess_bits)
                    # Is the guess wrong?
                    if not is_correct:
                        print("You set the inputs to the circuit. It doesnt seem to do anything")
                    # If the guess is right, proceed to the next problem
                    else:
                        print("\nRight answer! It took you " + str(guesses) + " trie(s). Let's try another...\n")
                        problems_solved[1] = True
                        break
            elif option_chosen == '11':
                print('\nSolve the head circuit by entering a 5-digit binary number to designate its input. Enter q to go back\n')
                guesses = 0
                print(CIRCUIT_PROBLEMS[2])
                # Have the user guess until they get the current problem right, or they quit
                while True:
                    user_guess = input("Answer: ")
                    # If they wish to go to the menu
                    if user_guess == 'q':
                        break
                    # Make sure input is binary
                    if not is_binary(user_guess):
                        print("Please enter a binary number with no spaces!")
                        continue
                    # Are the wrong number of bits provided?
                    if len(user_guess) != problems[CIRCUIT_PROBLEMS[2]][1]:
                        print("Please enter the correct number of input bits!")
                        continue
                    guesses += 1
                    # Extract the input
                    guess_bits = []
                    for bit in user_guess:
                        guess_bits.append(int(bit))
                    # Simulate circuit with the input
                    is_correct = problems[CIRCUIT_PROBLEMS[2]][0](guess_bits)
                    # Is the guess wrong?
                    if not is_correct:
                        print("You set the inputs to the circuit. It doesnt seem to do anything")
                    # If the guess is right, proceed to the next problem
                    else:
                        print("\nRight answer! It took you " + str(guesses) + " trie(s). Let's try another...\n")
                        problems_solved[2] = True
                        break
        else:
            print('Please choose a valid option!')


