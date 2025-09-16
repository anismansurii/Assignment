List_main = ["Tops" , "Technologies" , "data sci" , "data analysis"]
while True:
    print()
    print(f"1 . Upper Case it " )
    print(f"2 . Lower case it ")
    print(f"3 . Count Vowel ")
    print(f"4 . Length of each element. ")
    print(f"5 . Exit")

    choice = int(input("Enter a Choice between 1-4 : "))
    match choice:
        
        case 1 :
            for i in List_main:
                print(i.upper())
            break
        case 2 :
            for i in List_main:
                print(i.lower())
            break
        case 3:
            for i in List_main:
                count = 0 
                for char in i :
                    if char in 'aeiou':
                        count+=1
                print(count)    
            break
        case 4: 
            for i in List_main:
                print(f"{i} length is {len(i)}")
            break
        case _ :
            print("Enter a valid choice between 1-4")

    