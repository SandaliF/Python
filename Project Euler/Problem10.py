def is_Prime(n):
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=2
tot=0
while n<2000000:
    if is_Prime(n):
        tot+=n
    n+=1
print (tot)
