li_nums = [x for x in range(1,10)]


def primecheck(num):
    if num ==0 or num==1:
        return False
    for i in range(2,num):
        if num%i == 0 :
            return False
    return True


li_ans = list(filter(primecheck , li_nums))


print(li_ans)