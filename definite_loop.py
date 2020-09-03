# for <variable> in range(<lower bound>, <upper bound +1>):

product = 1

for count in range(1,5):
    product = product * count
    print(product)

#acccumulating a single result value from a series of values
#note that we use variable the_sum rather than sum to accumulate the sum of the numbers.

lower = int(input('Enter the lower bound: '))
upper = int(input('Enter the upper bound: '))

the_sum = 0
for number in range(lower,upper+1):
    the_sum += number

print(the_sum)

# the_sum += number is equal to the_sum = the_sum + number.  <variable> <operator> = <expression>
