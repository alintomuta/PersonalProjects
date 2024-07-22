#bidding program
import os

name=input("What is your name?")
bid=input("What is your bid?__$")
bid_dictionary={name,bid}
clear=lambda:os.system('cls')
def add_bid(new_name,new_bid):
    add_bid={}
    add_bid[name]=new_name
    add_bid[bid]=new_bid
    bid_dictionary.append(add_bid)


'''a=input("Is someone else ready to make a bid? Type 'yes' or 'No'")
while a=="yes":
    clear()
    name=input("What is your name?")
    bid=input("What is your bid")
    bid_dictionary={name,bid}
    add_bid(name,bid)
    break
'''    
print(bid_dictionary)

