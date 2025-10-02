# Welcome to my Calculator
   
def calculator():
    number_one = int(input('Enter your first number '))
    operation = input('What operation would you like to perform? Enter one of the following: +, -, *, /, //, % ').strip()
    number_two = int(input('Enter your second number '))
    if operation == '+':
        sum = number_one + number_two
        print(sum)
    elif operation == '-':
        sum = number_one - number_two
        print(sum)
    elif operation == '*':
        sum = number_one * number_two
        print(sum)
    elif operation == '/':
        if number_one or number_two != 0:
            sum = number_one / number_two
            print(sum)
        else:
            print('Cannot divide by 0. Enter a new set of numbers.')
            #calculator()
    elif operation == '//':
        if number_one or number_two != 0:
            sum = number_one // number_two
            print(sum)
        else:
           print('Cannot divide by 0. Enter a new set of numbers.')
            #calculator() 
    elif operation == '%':
        sum = number_one % number_two
        print(sum)
    else:
        print('Enter a valid operator.')

    return sum

result = calculator()


while True:
    prompt = int(input('Would you like to continue to build on your calculation or start over? Type 1 to build, or 2 to start over. Enter 3 to exit calculator and return to homepage. ').strip())
    while prompt != 1 and prompt != 2 and prompt != 3:
        print('Enter a valid prompt number.')
        prompt = int(input('Would you like to continue to build on your calculation or start over? Type 1 to build, or 2 to start over. Enter 3 to exit. ').strip())
    
    if prompt == 1:
        print(f'Your current number is {result}') 
        operation = input('What operation would you like to perform? Enter one of the following: +, -, *, /, //, % ').strip()
        number_two = int(input('Enter your second number '))
    
        if operation == '+':
            result += number_two
            print(result)
        elif operation == '-':
            result -= number_two
            print(result)
        elif operation == '*':
            result *= number_two
            print(result)
        elif operation == '/':
            if number_two != 0:
                result /= number_two
                print(result)
            else:
                print('Cannot divide by 0. Enter a new set of numbers. ')
        elif operation == '//':
            if number_two != 0:
                result //= number_two
                print(result)
            else:
                print('Cannot divide by 0. Enter a new set of numbers. ')
        elif operation == '%':
            result %= number_two
            print(result)
        else:
            print('Enter a valid operator.')
            continue
    elif prompt == 2: 
        calculator()
    elif prompt == 3:
        break




    



    


