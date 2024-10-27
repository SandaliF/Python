def is_prime(n):
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            # print("Not Prime")
            return False
        else:
            continue
    return True

# n=(int(input("Enter: ")))

n=2
primes=[]
while len(primes)<10001:
    if is_prime(n):
        primes.append(n)
    n+=1
print (primes[-1])


        