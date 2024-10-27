tot=0
sum_of_square=0

for i in range (1,101):
    tot+=i
    sum_of_square+=i**2

square_of_sum=tot**2
print(square_of_sum)  
print(sum_of_square)

print(square_of_sum-sum_of_square)
