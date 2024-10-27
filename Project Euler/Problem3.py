#largest prime factor

from math import sqrt

def is_prime(n):
    for i in range (2,int(sqrt(n))+1):
        if n%i==0:
            # (print("Not a prime"))
            return False
        else:
            continue
    # (print("Prime Number"))
    return True



n=(int(input("Enter number: ")))
largest=0

# for i in range(2,int(sqrt(n))+1):
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        if is_prime(i):
            # print (i)
            largest=i

print(largest)