fib=[1,2]

# for i in range (0,8):
#     fib.append(fib[i]+fib[i+1])
# print(fib)

sum=2
i=0
while fib[-1]<4000000:
    new=fib[i]+fib[i+1]
    fib.append(new)
    i+=1
    if new%2==0:
        sum+=new

print(sum)