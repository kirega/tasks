import random
def dice():
    return random.randint(1,6)
def entry():
    print('The dice rolls the number ->' , dice())
    while True:
        m = str(input('Want to roll dice again? y - Yes or n - No  '))
        m.lower()
        if(m == 'y' or m == 'yes'):
            print('The dice rolls the number ->' , dice())
        elif(m == 'n' or m == 'no'):
            return False
        else:
            print('Invalid input, type "y" to roll dice again and "n" to exit')
if __name__ == '__main__':
    entry()