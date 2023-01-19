print('****Find Square Root Program****')
# without build in module.
num=int(input('Enter your number: \n'))

def squareRoot(num):
    return num**0.5
print(f"the square root of given number is {squareRoot(num)}")

# with build math module.
import math
print(f"the square root of given number is {math.sqrt(num)}")
