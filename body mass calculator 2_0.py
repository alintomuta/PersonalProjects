#this is my BMI Calculator used for professionals

a=input(print("Please input your height in m: "))
a=float(a)
b=input(print("Please input your mass in kilograms: "))
b=int(b)
bmi_formula=b/(a**2)
bmi_formula=str(bmi_formula)
bmi_formula=float(bmi_formula)
bmi_formula=round(bmi_formula)
print(f"Your BMI score its: {bmi_formula}")
if bmi_formula<18.5:
 print("You are underweight")
elif (bmi_formula<=25) & (bmi_formula>18.5):
 print("You have a normal weight")
elif (bmi_formula>25) & (bmi_formula<=30): 
 print("You are overweight")
elif (bmi_formula>30) & (bmi_formula<=35):
 print("You are obese")
elif (bmi_formula>35):
 print("You are clinically obese! You're healt is in danger")
 