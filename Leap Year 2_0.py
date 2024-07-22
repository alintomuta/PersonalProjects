a=int(input("Please provide a year to check if its a leak year or not:"))

if (a%4)==0 &(a%100)==0 &(a%400)==0:
     print("The year its a leap year")
elif (a%4)==0 &(a%100)!=0:
    print("The year its a leap year")

else:
    print("The year its  not a leap year")