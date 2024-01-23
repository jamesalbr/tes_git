def count_vowels(sentence): 
    sentence = sentence.casefold() 
    return sum(sentence.count(vowel) for vowel in 'aeiou') 
      
print(count_vowels("Welcome to Geeksforgeeks")) 

from functools import lru_cache 
import time 
 
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
 
    return Fibonacci(n-1) + Fibonacci(n-2)
# Driver Program
begin = time.time()
print(Fibonacci(40))
end = time.time()
print("Time taken to execute the function with lru_cache is", end-begin) 

@lru_cache(maxsize = 128)
def Fibonacci_cache(n):
 
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
 
    return Fibonacci_cache(n-1) + Fibonacci_cache(n-2)
# Driver Program
begin = time.time()
print(Fibonacci_cache(40))
end = time.time()
print("Time taken to execute the function with lru_cache is", end-begin) 