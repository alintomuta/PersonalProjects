print("Welcome to Wien Rollercoaster")
height=int(input(print("Please provide your height in cm:\n")))
if height>120:
    print("You can ride the rollercoaster")
    age=int(input("What is your age\n"))
    bill=0
    pic=(str(input("Do you want a picture? YES/NO\n")))
    if pic:=("YES"):
     bill=3
 
    if (age>12) & (age<18):
        print(f"You pay just: {bill+7} dollars")
    elif age<12:
         print(f"You pay just: {bill+5} dollars")
    elif (age>=45) & (age<=55) & (pic=="YES"):
    
        print(f"You pay just: {bill} dollars")
    else:
         print(f"You pay just: {bill+12} dollars")

else:
    print("You can not ride the roller coaster, because you are a midgit")
