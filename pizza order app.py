# This is Pizza King order app
print("Welcome to pizza King")
size=input("What size of Pizza do you want to order?: S (Small),M (Medium),or L (Large)?\n")
add_pepperoni=str(input("Do you want pepperoni? : Y or N?\n"))
extra_cheese=str(input("Do you want extra cheese? : Y or N?\n"))
bill=0
if size=="S":
    bill=15
    if add_pepperoni=="Y":
        bill=bill+2
if size=="M":
    bill=20
if size=="L":
    bill=25
if extra_cheese=="Y":
    bill = bill+1
if (size=="M") & (add_pepperoni=="Y"):
    bill = bill+3
if (size=="L") & (add_pepperoni=="Y"):
    bill+=3
print(f"Your final bill is {bill} dollars, Thank you")