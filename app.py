from re import T


MAX_PASS_LENGTH = 128
MIN_PASS_LENGTH = 20

symbols = False
numbers = False
upper = False
lower = False

run = True

while run:
    # Initial user prompt
    print('=========================================')
    print('Welcome to the secure password generator!')
    print('=========================================\n')

    print('Firstly, let\'s get some things in order. Continue? [Y/N]')

    prompt = True

    while prompt:
        user_input = input('> ')

        if user_input == 'Y' or user_input == 'y':
            break
        elif user_input == 'N' or user_input == 'n':
            print('Goodbye.')
            run = False
            break
        else:
            print('This is not a valid answer')
            continue
    
    if run == False:
        break
    
    # Set password length
    print('A password should be 20 characters at a minimum and 128 characters at max\n')
    
    while prompt:
        user_input = input('> ')
        pass_length = user_input
        try:
            if int(pass_length) > 128:
                print('Password is too long')
                continue
            elif int(pass_length) < 20:
                print('Password is too short')
                continue
            elif int(pass_length) >= 20:
                print('Your password will be set to ' + pass_length + ' characters long')
                prompt = False
                break
        except ValueError:
            print('These are not valid numbers.')
            continue
    
    print('A secure password should ideally include numbers, symbols, uppercase and lowercase letters')

    prompt = True

    # Include numbers
    print('Include numbers? [Y/N]')

    user_input = input('> ') 
    while prompt:
        if user_input == 'Y' or user_input == 'y':
            numbers = True
            break
        elif user_input == 'N' or user_input == 'n':
            break
        else:
            print('These are not valid characters.')
            continue

    #Include uppercase
    print('Include uppercase letters? [Y/N]')

    user_input = input('> ')
    while prompt:
        if user_input == 'Y' or user_input == 'y':
            upper = True
            break
        elif user_input == 'N' or user_input == 'n':
            break
        else:
            print('These are not valid characters.')
            continue
        
     #Include lowercase
    print('Include lowercase letters? [Y/N]')

    user_input = input('> ')
    while prompt:
        if user_input == 'Y' or user_input == 'y':
            lower = True
            break
        elif user_input == 'N' or user_input == 'n':
            break
        else:
            print('These are not valid characters.')
            break

    #Include symbols
    print('Include symbols? [Y/N]')

    user_input = input('> ')
    while prompt:
        if user_input == 'Y' or user_input == 'y':
            symbols = True
            break
        elif user_input == 'N' or user_input == 'n':
            break
        else:
            print('These are not valid characters.')
            continue