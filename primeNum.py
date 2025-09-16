def PrimeCheck(num):
    flag=True
    for i in range(2,num):
        if num%i == 0:
            flag = False
            break
    if flag==True:
        return num
    

num1 = 5
for i in range(2,num1+1):
    if PrimeCheck(i):
        print(i)

