# Task 3: You are tasked with creating a Python program that calculates the square root of a non-negative number
# entered by the user. The program should handle exceptions such as ValueError and NameError appropriately.
# Additionally, it should include an else block to print the square root if no exception occurs and a finally block
# to ensure that the program execution is completed. Write the Python program to fulfill these requirements.
import math

try:
    num = float(input('Enter a non-negative number: '))
    if num < 0:
        raise ValueError('Number must be non-negative')
    square_root = math.sqrt(num)
except ValueError as e:
    print(f'Error: {e}')
except NameError as e:
    print('Name error occurred')
else:
    print(f'The square root of {num} is {square_root}')
finally:
    print('Program executed successfully')

