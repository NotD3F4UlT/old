import math
def find_integer_answers(c):
    answers=[]

    for b in range(1,c+1):
        q=c*c-b*b
        a=math.isqrt(q)
        if a*a==q:
            if a>0:
                answers.append((a,b))
    return answers
c=int(input("c= "))
solutions = find_integer_answers(c)
if solutions:
    for sol in solutions:
        print(f"a = {sol[0]}, b = {sol[1]}")
else:
    print("No PYTHAGOREAN TRIPLET exists with the give number")