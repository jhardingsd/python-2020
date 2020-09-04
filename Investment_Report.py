#Case Study: An investment Report.  Page 73

start_balance = float(input('Enter initial investment amount: '))
years = int(input('Enter the number of years: '))
rate = int(input('Enter the rate as a %: '))
rate = rate / 100

total_interest = 0.0

print('%4s%18s%10s%16s' % \
      ('Year', 'Starting Balance', 'Interest', 'Ending Balance'))

for year in range(1, years + 1):
    interest = start_balance * rate
    end_balance = start_balance + interest
    print('%4d%18.2f%10.2f%16.2f' % \
          (year, start_balance, interest, end_balance))
    start_balance = end_balance
    total_interest += interest

print('Ending balance: $%0.2f' % end_balance)
print('Total interest earned: $%0.2f' % total_interest)
