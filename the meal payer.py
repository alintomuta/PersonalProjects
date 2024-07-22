import random 

names_string=input("Give me averybody's name,separated by a comma\n")
names=names_string.split(" ")

 
a=len(names)
choise=random.randint(0,a-1)
a=(names[choise])


print(f"{a} is going to pay the meal today for everyone! ")
