#   A program to convert celsius temperature into fahrenheit.

first_name = 'Lord Jeffrey'
last_name = 'Harding'

def main():
    celsius = int(input('Enter the degrees in celsius:'))
    fahrenheit = int((celsius/5) * 9) + 32
    print('The temperature is', end=' ')
    print(fahrenheit, 'degrees.')
    print('Brought to you by', first_name,last_name)

main()
