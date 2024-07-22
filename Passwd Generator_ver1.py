import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=["!","@","#","$","%"]
numbers=["1","2","3","4","5","6","7","8","9","0"]

length_passwd=int(input("introdu numarul de caractere dorit din parola:\n"))

x = ((random.sample(letters,(length_passwd-5))+random.sample(symbols,2)+random.sample(numbers,3)))


print(random.sample(x,length_passwd))

