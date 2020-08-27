#Simultaneous Assignment examples below.  Sometimes, it makes sense to capture several values at the same time. 

x= int(input('Enter value of x: '))
y= int(input('Enter value for y: '))
sum, diff = x + y, x - y
print(sum,diff)
temp = x
x = y
y = temp
print (x,y, temp)
x, y = y, x
print (x,y)

def main():
    print("This program computers the average of two scores")
    score1, score2 = eval(input('Enter the two scores separated by a comma: '))
    average_score = (score1 + score2)/2

    print('The average score is:', average_score)

main()
