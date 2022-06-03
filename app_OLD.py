from time import sleep
import string
import random

PASS_LIMIT = 128

run = True
passwd_lower = False
passwd_symbols = False
passwd_numbers = False
passwd_upper = False

# Main program loop
while(run):

    # Initial user prompt
    print('Welcome to the secure password generator!\nBefore we continue, we have some questions, proceed? [Y/N]')

    user_input = input('> ')

    prompt = True

    while(prompt):
        if user_input == 'N' or user_input == 'n':
            print('Program is terminating...')
            sleep(1)
            run = False
            break
        elif user_input == 'Y' or user_input == 'y':
            print('Great! let\'s continue!')
            break
        else:
            print('This is not a valid answer...')
            break

    if run == False:
        break

    # Set amount of characters for password
    while(prompt):
        print('How many characters do you want your password to have? [20-128 characters]')

        user_input = input('> ')
        char_length = user_input

        try:
            if int(char_length) < 20:
                print('You need more characters.')
                continue
            elif int(char_length) > PASS_LIMIT:
                print('You have surpassed the max number of allowed characters.')
                continue
            elif int(char_length) >= 15:
                print('You have set your password length to ' + str(char_length) + ' characters')
                prompt = False
                break
        except ValueError:
            print('These are not valid characters.')
            continue

    prompt = True

    # Prompt user to include different password parameters
    while(prompt):
        print('Include symbols? [Y/N]')

        user_input = input('> ')

        if user_input == 'Y' or user_input == 'y':
            passwd_symbols = True
            break
        elif user_input == 'N' or user_input == 'n':
            break
        else:
            print('Invalid answer.')
            continue

    while(prompt):
        print('Include numbers? [Y/N]')

        user_input = input('> ')

        if user_input == 'Y' or user_input == 'y':
            passwd_numbers = True
            break
        elif user_input == 'N' or user_input == 'n':
            break
        else:
            print('Invalid answer.')
            continue

    while(prompt):
        print('Include lowercase letters? [Y/N]')

        user_input = input('> ')

        if user_input == 'Y' or user_input == 'y':
            passwd_lower = True
            break
        elif user_input == 'N' or user_input == 'n':
            break
        else:
            print('Invalid answer.')
            continue

    while(prompt):
        print('Include uppercase letters? [Y/N]')

        user_input = input('> ')

        if user_input == 'Y' or user_input == 'y':
            passwd_upper = True
            break
        elif user_input == 'N' or user_input == 'n':
            break
        else:
            print('Invalid answer.')
            continue

    data = [passwd_lower, passwd_upper, passwd_numbers, passwd_symbols]

    if not any(data):
        print('Program is terminating...')
        sleep(1)
        run = False
        break
    elif data[0] == False and data[1] == False:
        print('Password must contain letters!')
        print('Program is terminating...')
        sleep(1)
        run = False
        break
    elif data[2] == False and data[3] == False:
        print('Password must contain either letters or symbols!')
        print('Program is terminating...')
        sleep(1)
        run = False
        break

    print('Generating user password...')
    sleep(1)

    # Password generation function
    def generate(length, symbols, numbers, lower, upper):
        if symbols == True and numbers == True and lower == True and upper == True:
            user_password = ''.join(random.choice(string.punctuation + string.digits + string.ascii_letters) for i in range(int(length)))
            print(user_password)
        elif symbols == False and lower == False and numbers == True and upper == True:
            user_password = ''.join(random.choice(string.digits + string.ascii_uppercase) for i in range(int(length)))
            print(user_password)
        elif symbols == False and upper == False and numbers == True and lower == True:
            user_password = ''.join(random.choice(string.digits + string.ascii_lowercase) for i in range(int(length)))
            print(user_password)
        elif numbers == False and lower == False and symbols == True and upper == True:
            user_password = ''.join(random.choice(string.punctuation + string.ascii_uppercase) for i in range(int(length)))
            print(user_password)
        elif numbers == False and upper == False and symbols == True and lower == True:
            user_password = ''.join(random.choice(string.punctuation + string.ascii_lowercase) for i in range(int(length)))
            print(user_password)
        elif symbols == False and upper == True and lower == True and numbers == True:
            user_password = ''.join(random.choice(string.digits + string.ascii_lowercase) for i in range(int(length)))
            print(user_password)
        elif numbers == False and symbols == True and lower == True and upper == True:
            user_password = ''.join(random.choice(string.punctuation + string.ascii_uppercase) for i in range(int(length)))
            print(user_password)
        elif lower == False and upper == True and symbols == True and numbers == True:
            user_password = ''.join(random.choice(string.punctuation + string.digits + string.ascii_uppercase) for i in range(int(length)))
            print(user_password)
        elif upper == False and lower == True and symbols == True and numbers == True:
            user_password = ''.join(random.choice(string.punctuation + string.digits + string.ascii_lowercase) for i in range(int(length)))
            print(user_password)


    generate(char_length, passwd_symbols, passwd_numbers, passwd_lower, passwd_upper)

    # Regeneration prompt
    print('Congratulations on your new password! it is now copied into your clipboard and is ready for use! \nWould you like to regenerate? [Y/N]')

    while(prompt):
        user_input = input('> ')
        if user_input == 'N' or user_input == 'n':
            print('Program is terminating...')
            sleep(1)
            run = False
            break
        elif user_input == 'Y' or user_input == 'y':
            break
        else:
            print('Invalid answer.')
            continue
