import random
#We need this for the code since we will need to choose the words randomly from the word bank.
art = ('''

 *---*
 |   |
 |
 |
 |
 |
---------''', '''

 *---*
 |   |
 |   O
 |
 |
 |
---------''', '''

 *---*
 |   |
 |   O
 |   |
 |    
 |    
---------''', '''

 +---+
 |   |
 |   O
 |  /|
 |
 |
---------''', '''

 *---*
 |   |
 |   O
 |  /|\ 
 |
 |
---------''', '''

 *---*
 |   |
 |   O
 |  /|\ 
 |  /
 |
---------''', '''

 *---*
 |   |
 |   O
 |  /|\ 
 |  / \ 
 |
---------''')
#I had to draw all of the parts out. They are separated by the commas. These drawings will be used everytime a guess is incorrect. It is all under the variable "art".
wordbank = "aardvark binocular computer dog energy ferocious good hello igloo jigsaw kangaroo listen mayonnaise nostalgic ostrich parabellum queen river suvethan thirunavukkarasu universe value warrant yield xylophone zebra".split()
#These are the words that are going to be used at random.
def RanWord(wordlist):
    index = random.randrange(0, len(wordlist) - 1)
    return wordlist[index]
#I have to define the choosing of the word to RanWord so I can use it later on in the code.
def hangman(art, incorrect, correct, word):
    print(art[len(incorrect)])
    print()
    print("Incorrect letters:", end=" ")
    for letter in incorrect:
        print(letter, end=" ")
    print()
    #This is the part of the board where the hanging man is displayed.
    blanks = "_"*len(word)
    #This puts the "_" where the letters would be.
    for x in range(len(word)):
        if word[x] in correct:
            blanks = blanks[:x]+word[x]+blanks[x+1:]
            #This is to replace the "_" with the letter when it is correct.
    for letter in blanks:
        print(letter, end=" ")
    print()
    #This shows the word with spaces in between each letter.
def guess(pastguess):
     while True:
         prediction = input("Give a guess. What letter do you think is in this word?")
         prediction = prediction.lower()
         if len(prediction)!=1:
             print("Please enter a single letter.")
         elif prediction in pastguess:
             print("Wait a minute...You already guess that. Try again.")
         elif not prediction.isalpha():
             print("Please enter a letter not a number.")
         else:
             return prediction
#This defines everything to guess. The input is under prediction. It is also where the I made the code crash proof. If a number, multiple letters or a past guess is entered, it will ask the user to enter another letter.
def playagain():
     print("Do you want to play this amazing, fantastic game, worth 100% game again? Enter yes or no.")
     return input().lower().startswith("y" or "Y")
#This is to be used at the very end. The "input()" changes the printed statement into a input. It will take in the word that starts with the letter "y".
print("HANGMAN: the game, recreated by Suvethan Thirunavukkarasu, that is definitely worth 100% if you ask me.")
incorrect=""
correct=""
word = RanWord(wordbank)
#Defining word to the randomly generated word.
gameover = False
#Assigning a variable so that I can create a while loop after. this variable means that the game is over.
while True:
    hangman(art, incorrect, correct, word)
    prediction = guess(incorrect+correct)
    if prediction in word:
        correct=correct+prediction
        allletters = True
        for x in range(len(word)):
            if word[x] not in correct:
                allletters = False
                break
        if allletters:
            print("Oh my god! You did it! You guessed all the letters!\nThe word was ",word.upper()+"!\nThis game is definetly worth 100%.")
            gameover = True
            #This is to be used when the user inputs all the correct letters.
    else:
        incorrect = incorrect + prediction
        if len(incorrect)==len(art)-1:
               hangman(art, incorrect, correct, word)
               print("Incorrect guesses:",str(len(incorrect))," Correct guesses:",str(len(correct)),"\nThe word was",word+".")
               print("You ran out of guesses.\nIt's okay, I still think that this game is worth 100%.")
               gameover = True
               #This is to be used when the user reaches his/her limit of guesses.
    if gameover:
        if playagain():
            incorrect=""
            correct=""
            gameover = False
            word = RanWord(wordbank)
            #If yes is entered, this triggers the gameover, which is set to equal False, which then triggers playagain. Then it resets the variables.
        else:
            print("You are now exiting the code. Thank you for playing HANGMAN: the game worth 100%.")
            break
            #If no is entered, this breaks the entire loop.
