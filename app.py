from cgi import print_form
from time import sleep
import pyperclip
import random
import string

MAX_PASS_LENGTH = 128
MIN_PASS_LENGTH = 20

final_pass = ''

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

    while prompt:
        symbols = False
        numbers = False
        upper = False
        lower = False

        # Include numbers
        print('Include numbers? [Y/N]')

        while prompt:
            user_input = input('> ')
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

        while prompt:
            user_input = input('> ')
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

        while prompt:
            user_input = input('> ')
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

        while prompt:
            user_input = input('> ')
            if user_input == 'Y' or user_input == 'y':
                symbols = True
                break
            elif user_input == 'N' or user_input == 'n':
                break
            else:
                print('These are not valid characters.')
                continue
        
        if numbers == False and symbols == False:
            print('A password must contain numbers and symbols.')
            continue
        elif symbols == False and upper == False and lower == False:
            print('A password must contain symbols and letters.')
            continue
        elif upper == False and lower == False:
            print('A password must contain letters.')
            continue
        else:
            prompt = False
            break

    print('Generating password...')
    sleep(3)

    #Generate password function
    def gen_pass(number, upper, lower, symbol, user_pass):
        if number == True and upper == True and lower == True and symbol == True:
            user_pass = ''.join(random.choice(string.punctuation + string.digits + string.ascii_letters) for i in range(int(pass_length)))            
            print(user_pass)
        elif number == True and upper == True and symbol == True:
            user_pass = ''.join(random.choice(string.punctuation + string.digits + string.ascii_uppercase) for i in range(int(pass_length)))
            print(user_pass)
        elif number == True and lower == True and symbol == True:
            user_password = ''.join(random.choice(string.punctuation + string.digits + string.ascii_lowercase) for i in range(int(pass_length)))
            print(user_pass)

    gen_pass(numbers, upper, lower, symbols, final_pass)

    # Prompt user to copy to clipboard
    print('Congratulations on your new password! Would you like to copy to clipboard? [Y/N]')

    user_input = input('> ')

    prompt = True
    
    while prompt:
        if user_input == 'Y' or user_input == 'y':
            pyperclip.copy(final_pass)
            print('Password has been successfully copied!')
            break
        elif user_input == 'N' or user_input == 'n':
            break
        else:
            print('This is not a valid answer.')
            continue
    
    
    # Prompt user to export to file
    print('Would you like to export the password to a text file? [Y/N]')

    user_input = input('> ')

    prompt = True
    
    while prompt:
        if user_input == 'Y' or user_input == 'y':
            with open('Password.txt', 'w') as p:
                p.write(final_pass)
            print('Password successfully exported to file!')
            break
        elif user_input == 'N' or user_input == 'n':
            break
        else:
            print('This is not a valid answer.')
            continue
            
    # Prompt user to restart
    print('Would you like to generate a new password again? [Y/N]')

    user_input = input('> ')

    if user_input == 'Y' or user_input == 'y':
        continue
    else:
        print('Goodbye!')
        sleep(3)
        run = False
        break
