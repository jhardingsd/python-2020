#Create a program to calculate the APR for 10 years at 2.5%.

print('This program calculates a future value of an investment at 2.5% return each year.')
principal = eval(input('Enter the principal investment amount: '))
apr = .025
years = eval(input('Enter the years of the investment: '))

for i in range(10):
    principal = principal * (1 + apr)
    print(principal)