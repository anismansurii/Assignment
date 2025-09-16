num1 = int(input("Enter a Number 1 "))
num2 = int(input("Enter a Number 2 "))


while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divison")

    choice = int(input("Enter A choice between 1-4 "))

    match choice:
        case 1 :
            print(f"You choose Addition And Sum is {num1+num2}")
            break
        case 2 :
            print(f"You choose to Subtract And Subtraction is {num1-num2}")
            break
        case 3 :
            print(f"You choose Multiply And Multiplication is {num1*num2}")
            break
        case 4 :
            print(f"You choose division and your divisior is {num1/num2}")  
            break
        case _ :
            print("Enter a valid Choice")     

                

