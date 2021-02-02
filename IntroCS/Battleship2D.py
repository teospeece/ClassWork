#author: Teo Speece
#date: 2/23/17
#description: a program that runs a battleship game using nested loops
#proposed points (15 of 15): In my program I successefully met the
# requirements and the code was functional
# _8/8 points: functionality
# _5/5 points: nested loops
# _2/2 points: score counter


print('Battlefield 2D')

# asks the user for an integer, sets it to variable size
rowsize= int(input('How large do you want your row to be? '))
colsize2 = int(input('How large do you want your column to be? '))
#imports random integer
import random
#creates variables for row and col making sure it stays in the range 0-rand integer -1
rowanswer = random.randint(0, rowsize-1)
colanswer2 = random.randint(0, colsize2-1)


#creates the battle ship map
for col in range(colsize2):
    for row in range(rowsize):
            print('~  ', end='')
    print()


# stars a new line
print('\n')
# create new variables to print the integer range
newcolnumber = colsize2 - 1
newrownumber = rowsize - 1
print('Using the Map. Where is the battleship (row integer (0 -',newrownumber,')  (col integer (0 -',newcolnumber,')')

counter = 0

shipgame_over = True
ship2game_over = True
#while loop where the program lets you guess until you get it right
while shipgame_over == True:
    guesscol = int(input('where is it in the col? '))
    # asks user to input their guess
    guessrow2 = int(input('where is it in the row? '))
    # if guess for col does not equal the (random integer - 1) or row doesn't then game loops
    if guesscol != rowanswer or guessrow2 != colanswer2:
        # counter to keep track of guesses
        counter += 1
        print('Missed! guess again')
        # reprints the battleship map

# prints the map with where the ship was missed with o
        for col in range(rowsize):
            for row in range(colsize2):
                #if col == user's guess for col and row then * prints
                if col == guesscol and row == guessrow2:
                    #if there is a hit the program prints * in the map
                    #if col and row is answered corrctly then prints *
                    if col == rowanswer and row == colanswer2:
                        print("* ", end="")
                        ship = False
                    #prints an o for a miss/ the user guesses wrong
                    else:
                        print("o ", end="")
                #prints an ~ for the ocean/map
                else:
                    print("~ ", end='')
            print()


        print('Using the Map. Where is the battleship (row integer (0 -',newrownumber,')  (col integer (0 -',newcolnumber,')')
    else:
        counter += 1
        #program checks if the guess is correct
        for col in range(rowsize):
            for row in range(colsize2):
                # checks the guess
                if col == guesscol and row == guessrow2:
                    if col == rowanswer and row == colanswer2:
                        #if guess is correct then program prints an *
                        print("* ", end="")
                    else:
                        #prints o for miss
                        print("o ", end="")
                else:
                    #prints ~ for map around miss
                    print("~ ", end='')
            print()
#succesfully sunk program tells you how many attempts it took
        print('Battle ship sunk! it took you ',counter, 'attempts')
        # ends statement
        shipgame_over = False

print('\n')


