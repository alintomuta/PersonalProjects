#tip calculator made by A.T
print("Welcome to the tip calculator!")
a=input(print("What was the total bill? $\n"))
a=float(a)
b=input("What percentage tip would you like to give to the waiter? 10%,12%,or 15%?\n")
b=int(b)
c=input("How many people to split the bill?\n")
c=int(c)
percentage=(a/c)/b
d=(percentage+a)/c
d=float('%.2f' % (d))
d=str(d)
print(f"Each person shoul pay $" + d)

