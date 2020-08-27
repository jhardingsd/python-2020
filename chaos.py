def main():
    print('This program illustrates a chaotic function')
    n = int(input('How many values should I print?:'))
    n1 = int(input('How many values should I print?:'))
    x = eval(input('Enter a number between 0 and 1'))
    y = eval(input('Enter a number between 0 and 1'))
    for i in range(n):
        x = 3.45 * x * (1 - x)
        print(x)
    for i in range(n1):
        y = 3.45 * y * (1 - y )
        print(y)
main()
