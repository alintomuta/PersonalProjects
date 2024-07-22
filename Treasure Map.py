#positions

row1=["☐","☐","☐"]
row2=["☐","☐","☐"]
row3=["☐","☐","☐"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure? enter 2digit number, which represent the column and the row!\n")

a=position[0]
b=position[1]
if (a=="1") & (b=="1"):
 row1=["💰","☐","☐"]
elif (a=="1") & (b=="2"):
 row2=["💰","☐","☐"]
elif (a=="1") & (b=="3"):
 row3=["💰","☐","☐"]
if (a=="2") & (b=="1"):
 row2=["💰","☐","☐"]
elif (a=="2") & (b=="2"):
 row2=["☐","💰","☐"]
elif (a=="2") & (b=="3"):
 row3=["☐","💰","☐"]
if (a=="3") & (b=="1"):
 row3=["💰","☐","☐"]
elif (a=="3") & (b=="2"):
 row2=["☐","☐","💰"]
elif (a=="3") & (b=="3"):
 row3=["☐","☐","💰"]

else:
    print("The number inputed it's wrong. You lost the map!")
print(f"{row1}\n{row2}\n{row3}")