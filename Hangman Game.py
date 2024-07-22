#this is a form of Hangman game written by me and Angela
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
cuvinte=['extraterestru','copilas','berbec','pamant','magazin','nuvela','perfect','nobil','cariera','autovehicul','Suceava']

chosen_word=(random.choice(cuvinte))
print(chosen_word)

display=[]
for letter in chosen_word:
        display.append("_")
while chosen_word!=display:
        
        print(f'The random word its: {display}')

        choice=input("Please choose a letter:\n")
        word_length=len(chosen_word)
        for position in range(0,word_length):
            letter=chosen_word[position]
            if letter==choice:
                    display[position]=letter
            
        if "_" in display:
            print(" try again")
            for life in stages:
                print(life[-1])
        else:
            print("The complete word its + ",display)
            print("You win")
            exit()


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        