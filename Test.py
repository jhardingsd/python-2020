#Case Study: An investment Report.  Page 73

investment_amount = float(input('Enter initial investment amount: '))
years = int(input('Enter years of investment: '))
interest_rate = float(input('Enter Interest Rate, i.e. 3.0: '))
new_number = interest_rate *.01
tabular = years

print('{:10}'.format('Year'), end='')
print('{:>16}'.format('Starting Balance'), end='')
print('{:>13}'.format('Interest'), end='')
print('{:>20}'.format('Ending Balance'), end='')
print('')
for i in range(1, years + 1):
    investment_amount *= (1 + new_number)
    print(i,' ', end='')
    print('%23.2f' % (investment_amount))