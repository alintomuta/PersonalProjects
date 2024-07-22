#this is the popular game of Rock-Paper-Scissors
#piatra bate foarfeca, foarfeca bate hartia,hartia bate piatra
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
a=input("What do you choose? Type 0 for rock,1 for paper or 2 for Scissors!\n")
a=int(a)
game=[0,1,2]
random_object=random.randint(0,len(game)-1)
if a==0:
    print(rock+"rock")
    print("Computer choose:\n")
    print (random_object)
    if (random_object)== 0:
        print("Equal,rock vs rock")
        print(rock)
    elif (random_object)==1:
        print("You lose, paper its stronger than rock")
        print(paper)
    elif (random_object)==2:
        print("You win , rock its stronger then scissors")
        print(scissors)
if a==1:
    print(paper+"paper")
    print("Computer choose:\n")
    print (random_object)
    if (random_object)== 0:
        print("You win,paper its stronger than rock")
        print(rock)
    elif (random_object)==1:
        print("Equal, paper vs paper")
        print(paper)
    elif (random_object)==2:
        print("You lose , scissors its stronger than paper ")
        print(scissors)
if a==2:
    print(scissors+"scissors")
    print("Computer choose:\n")
    print (random_object)
    if (random_object)== 0:
        print("You lose,scissors its stronger than rock")
        print(rock)
    elif (random_object)==1:
        print("You win, scissors its stronger than paper")
        print(paper)
    elif (random_object)==2:
        print("Equal , scissors vs scissors ")
        print(scissors)
 