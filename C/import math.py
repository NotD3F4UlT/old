import math,time, subprocess
def find_integer_answers(n):
    answers=[]

    for b in range(n+1):
        nb=n*b
        k=math.isqrt(nb)
        if k*k==nb:
            a=n-2*k+b
            if a>=0:
                answers.append((a,b))
            
    return answers
n=int(input("n= "))

solutions = find_integer_answers(n)

if solutions:
    for sol in solutions:
        print(f"Found values: a = {sol[0]}, b = {sol[1]}")
else:
    print("Root n has to be a real no.")

    time.sleep(1.5)
    print("Therefore, please input non-negative value of n")

count=len(solutions)

print(f"Number of Solutions: {count}")