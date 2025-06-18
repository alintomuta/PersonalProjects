logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
import random
print(logo)
print("Welcome to the Number Guessing Game! - by Anakin Software Dev.Corporation")
print("Computer say: Im thinking of a number between 1 and 100")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard' :")
list=[]
for i in range(0,101):
    list.append(i)
print(list)
number=random.choice(list)

user_attempts=0

while difficulty =='easy' and user_attempts<=10:

        guess=int(input("Make a guess, number: "))
        if guess==number:
            print(f"You win , the number was {number}")
            exit()
        elif guess<number:
            print(f"Too low, you have {10-user_attempts} remaining to guess the number")
            user_attempts+=1
        elif guess>number:
            print(f"Too high, you have {10-user_attempts} remaining to guess the number")
            user_attempts += 1
        elif user_attempts==10:
            print("Game over")

while difficulty == 'hard' and user_attempts <= 5:
        guess=int(input("Make a guess, number: "))

        if guess==number:
            print(f"You win , the number was {number}")
            exit()
        elif guess<number:
            print(f"Too low, you have {5-user_attempts} remaining to guess the number")
            user_attempts+=1
        elif guess>number:
            print(f"Too high, you have {5-user_attempts} remaining to guess the number")
            user_attempts+=1
if user_attempts==5 or 10:
    print("Game over, you reached the maximum number of attempts")