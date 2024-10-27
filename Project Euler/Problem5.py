n=1
while True:
    for i in range(2,21):
        if n%i==0:
            continue
        else:
            break
    if i<20:
        n+=1
    else:
        print (n)
        break


# n=1
# while True:
#     for i in range(20,1,-1):
#         if n%i==0:
#             continue
#         else:
#             break
#     if i>1:
#         n+=1
#     else:
#         print (n)
#         break