import random


def dice():
    # Randonly generates the die roll
    return random.randint(1, 6)


def get_input():
    # Function to get the user input
    # Deliberately separated to make testing possible.
    return input('Want to roll dice again? y - Yes or n - No ')


def entry():
    # Determines the course of action after atleast rolling die once:
    # It will then based on user input choose what to do.

    print('The dice rolls the number ->', dice())
    while True:
        m = str(get_input())
        m.lower()
        if(m == 'y' or m == 'yes'):
            print('The dice rolls the number ->', dice())
        elif(m == 'n' or m == 'no'):
            return False
        else:
            return('Invalid input, type "y" to roll dice again and "n" to exit')


if __name__ == '__main__':
    entry()
