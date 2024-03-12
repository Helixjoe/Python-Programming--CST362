#program to calculate simple interest
principle_amount=float(input('Enter the investment amount: '))
time=int(input("Enter the period of time in years: "))
interest=int(input("Enter the percentage of interest: "))
print("Year\tStarting Balance\tInterest\tEnding Balance")
total_interest=0.00
for i in range(time):
    new_interest=(interest/100)*principle_amount
    total_interest+=new_interest
    new_amount=new_interest+principle_amount
    print(i+1,"\t",principle_amount,"\t\t","%-6s"%round(new_interest,2),"\t",round(new_amount,2))
    principle_amount=new_amount
print("Ending Balance : $",round(principle_amount,2))
print("Interest Earned : $",round(total_interest,2))