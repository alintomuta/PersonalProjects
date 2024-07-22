# application that tells you the love between name compatibility
print("Welcome to Love Calculator!")
name1=input("What is your name\n")
name2=input("What is your pottential Lover's name\n")
name1=name1.upper()
name2=name1.upper()

a=(name1.count("T")+name1.count("R")+name1.count("U")+name1.count("E")+name2.count("T")+name2.count("R")+name2.count("U")+name2.count("E"))
b=(name1.count("L")+name1.count("O")+name1.count("V")+name1.count("E")+name2.count("L")+name2.count("O")+name2.count("V")+name2.count("E"))

z3=str(a+b)
z3=int(z3)


if (z3<10)or(z3>90):
    print(f"Your score is {z3}, you go togheter like coke and mentos")
elif (z3>40)&(z3<50):
    print(f"Your score is {z3}, you are alright togheter")
else:
    print(f"Your score is {z3}")