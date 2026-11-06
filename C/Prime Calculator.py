from itertools import count
import math,gmpy2


def prime(n):
    answers=[]
    a=math.isqrt(n)
    for i in range (2,a):
        q=int(n/i)
        if q*i==n:
            answers.append((q,i))
    return answers

n= int(input("n= "))
solutions = prime(n)

if solutions:
    for sol in solutions:
        print(f"Found factors: a = {sol[0]}, b = {sol[1]}")
else:
    print("The given number is prime")
#count=len(solutions)
#print(f'Number of factors= {count}')