#student info dict and menu driven program
dict_info = {101 : "Anis"  , 102:"Jil"}

while True:
    print("1.Add Name" , "2.Edit Student Info" , "3.Delete Student" , "4.View All" ,"5.Search" , "6.Exit" , sep="\n")
    choice = int(input("Enter a Choice "))
    match choice:
        case 1 :
            roll_no = int(input("enter a roll number "))
            name = input("Enter Name ")
            dict_info[roll_no] = name
            

        case 2 :
            roll_no = int(input("Enter a roll number "))
            if roll_no in dict_info.keys():
                print(f"Data is {roll_no} : {dict_info[roll_no]}")
                name = input("Enter a new name ")
                dict_info[roll_no] = name
            else:
                print("Roll number does not exist")
            
        case 3 :
            roll_no = int(input("Enter a roll number "))
            del dict_info[roll_no]
            print(dict_info)
            
        
        case 4:
            for i in dict_info.keys():
                print(f"{i}:{dict_info[i]}")
                
        case 5 :
            roll_num = int(input("Enter a roll number "))
            if roll_num in dict_info.keys():
                print("Data Found",roll_num,":",dict_info[roll_num])
            
        case 6 :
            break 


            