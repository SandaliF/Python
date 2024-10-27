def is_Pal(n):
    Num=str(n)
    # print(Num[::-1])
    if Num==Num[::-1]:
        # print("Palindrome")
        return True
    # print("Not")
    return False  

largest=0
for i in range (100,1000):
    for j in range (100,1000):
        mul=i*j
        if is_Pal(mul):
            if largest<mul:
                largest=mul
print(largest)

