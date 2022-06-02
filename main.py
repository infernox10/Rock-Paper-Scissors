b = True
while b == True:
    game = ['R', 'P', 'S']
    print('Game Begins')
    print('This is the Rock, Paper, Scissors Game')
    print('Enter R for Rock, P for Paper and S for Scissors')
    a = input('Select R, P or S: ')
    for letter in a:
        if letter in game:
            continue
        else:
            break
            print('Invalid Input')
    import random
    computer_choice = random.choice(game)
    print('Your Choice is: ', a)
    print('Computer Choice is: ', computer_choice)
    if a == computer_choice:
        print('It is a Tie')
    elif a == 'R' and computer_choice == 'P':
        print('Computer WINS')
    elif a == 'P' and computer_choice == 'R':
        print('Congratulations You WIN')
    elif a == 'R' and computer_choice == 'S':
        print('Congratulations You WIN')
    elif a == 'S' and computer_choice == 'R':
        print('Computer WINS')
    elif a == 'P' and computer_choice == 'S':
        print('Computer WINS')
    elif a == 'S' and computer_choice == 'P':
        print('Congratulations You WIN')
    elif a not in game:
        print('Invalid Input')
    print('Do You want to play again?, y or n')
    c = input('Enter y to continue or n to end: ')
    if c == 'y':
        continue
    if c == 'n':
        print('Thank you for playing')
        break
