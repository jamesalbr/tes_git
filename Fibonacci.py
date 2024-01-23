#The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …….. In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation.
#Fn = Fn-1 + Fn-2
#with seed values : F0 = 0 and F1 = 1.

#NATIVE APPROACH

def FibNA(n):
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1
    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    print()
# Driver Program
FibNA(9)

#import numpy as np
#print('KONTOL')

#RECURSION

def Fibonacci(n):
 
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
# Driver Program
print(Fibonacci(9))



FibArray = [0, 1]
 
def fibonacciAR(n):
   
    # Check is n is less 
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is less 
    # than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:        
        FibArray.append(fibonacciAR(n - 1) + fibonacciAR(n - 2))
        return FibArray[n]
 
# Driver Program
print(fibonacciAR(9))