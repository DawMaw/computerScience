# futureValue.py
# A program to compute the value of an investment
# carried 10 years into the future

print("This program calculates the future value of an investment")

payment = eval(input("Enter amount to invest each year: "))
apr = eval(input("Enter the annual interest rate: "))
years = eval(input("Enter the number of years: "))

principal = 0.0
for i in range(years):
    principal = (principal + payment) * (1 + apr)

print("The amount in", years, " years is:", principal)
