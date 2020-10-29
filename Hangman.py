# Hangman Game
import random
def greet():
    '''this function greets to the player'''
    print("hello friend \nit's time to play hangman game")
greet()

word_list=["book","laptop","apple","coffee","cup","bag","mirror"]
turns=3
guessedword=''
word_index=random.randrange(len(word_list))
word=word_list[word_index]
print(word)

def checkIFcorrect(word,guessedword):
    if (sorted(word)== sorted(guessedword)):
        return True
    else:
        return False

            
while (turns !=0 and checkIFcorrect(word,guessedword)== False ):
    char=str(input('enter a letter'))
    while char in word and char in guessedword:
        break
    for c in word:
        if char==c:
            guessedword +=char
            print (guessedword)
            checkIFcorrect(word,guessedword)
        elif char not in word :
            turns -=1
            print("you have",turns,"turn\s left")
            break
    if char ==' ':
        print('no blank')
while checkIFcorrect(word,guessedword)== True:
    print("winner winner :D")
    print("the word is",word)
    break
while turns ==0:
    print("You Lose :(")
    break
