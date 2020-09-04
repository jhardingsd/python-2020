#range function expects a third argument that allows you to skip some numbers.


the_sum = 0
for count in range(2,11,2):
    the_sum += count
    print(the_sum)

print(the_sum)

#range function that counts down

for count in range(10,0,-1):
    print(count,'', end='')

list(range(10,0,-1))

for count in range(5):
    print(count + 1, end='')
print('space')

for count in range(1,4):
    print(count, end='')

for count in range(1,6,2):
    print(count, end='')
#1,3,5

for count in range(6,1,-1):
    print(count)
#5,4,3,2

#print your name 100 times

for count in range(100):
    print('Jeffrey Harding')

#loop variable, which allows the body to know which iteration is being executed.
# For-loops are typically used when the number of iterations is known before entering the loop.