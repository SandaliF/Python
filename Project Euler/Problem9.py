def isPyTriplet(a,b,c):
    if (a**2)+(b**2)==c**2:
        return True
    else:
        return False

# i,j,k=3,4,5
# while i>=3:
#     while j>=4:
#         while k>=5:
#             if isPyTriplet(i,j,k):
#                 if i+j+k==1000:
#                     print(i*j*k)
#                 else:
#                     k+=1
#                     continue
                
#         break
#     break

m=1
flag=False

while m>0:
    for n in range (1,m):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if isPyTriplet(a,b,c):
            if a+b+c==1000:
               print(a*b*c)
               flag=True
               break
    if flag==True:
        break
    else:
        m+=1
            