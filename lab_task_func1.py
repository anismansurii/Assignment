#Factorial of num
def Find_fact(num):
     ans = 1
     for i in range(1,num+1):
          ans*= i
     return ans
print(Find_fact(5))