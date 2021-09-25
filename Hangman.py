import random as rd
import art
from word import word_list
word=rd.choice(word_list)
word=word.lower()
length=len(word)
lives=5
guess=[]
word_list=list(word)
for _ in range(length):
    guess+="_"
stats=False
while(not stats):
    char=input("Guess a letter ")
    if(char in guess):
        print("Already chosen the letter ")
    elif(char in word):
        print("You made a right guess ")
        for i in range(length):
            if word[i]==char:
                guess[i]=char
        print(guess)
    else:
        print("Wrong Guess ")
        lives-=1
        print(art.stages[lives])
        if(lives==0):
            stats=True
    if(not("_" in guess)):
        stats=True
    print(f"Lives Left {lives}")
    if(lives==0):
        print(f"The word is {word}")
