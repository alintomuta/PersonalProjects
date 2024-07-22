age=input("What is your current age? ")
age=int(age)
d=365
w=52
m=12
age_days=age*365
age_weeks=age*52
age_months=age*12
limit_age_days=32850
limit_age_weeks=4680
limit_age_months=1080
print(f"You have {(limit_age_days-age_days)} days, {(limit_age_weeks-age_weeks)}weeks,{(limit_age_months-age_months) }months left")

