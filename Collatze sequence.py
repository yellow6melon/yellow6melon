def collatz(input_num):
    if input_num == 1:
        return 1
    else:
        if input_num % 2 ==0:
            input_num = input_num/2
            print(input_num)
            collatz(input_num)
        else:
            input_num = 3*input_num+1
            print(input_num)
            collatz(input_num)

try:
    number = int(input('Enter:'))
    collatz(number)
except ValueError as Error:
    print('ValueError:You need input digital.')






