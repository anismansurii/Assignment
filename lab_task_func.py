def isPositive(num):
    if num > 0:
        return "Positive"
    else:
        return "Negative"

def isEvenODD(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

ans = isPositive(14)
if ans=="Positive":
    print(isEvenODD(14))



#Find a power of a number
def FindPower(num , power):
    return num**power
print(FindPower(5,4))



#finfd if num is prime or not

def isNumPrime(num):
    if num>1:
        for i in range(2,num-1):
            if num%i == 0:
               return "Not Prime"
            else:
                return "Prime" 
            


num1 = int(input("Enter a Number "))
print(isNumPrime(num1))