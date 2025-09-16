while True:
    print("1 . Whole file " , "2 . Only single line " , "3 . Particular line " , "4 . particular character number of line " , " 5 . exit " , sep='\n')
    
    file_name = input("Enter a file to read ")
    
    choice = int(input("Enter a choice "))

    f = open(file_name , 'r')

    match choice:
        case 1 :

            data = f.read()
            print(data)
        
        case 2 :

            line = f.readline()
            print(line)

        case 3 :
            n = int(input("Enter a Particular number of line : "))
            
            n_lines = f.readlines()
            if n > 0 and n <= len(n_lines):
                n = n - 1
                print(n_lines[n])
            else:
                print(f"File only has {len(n_lines)} lines")
            
        case 4 :

            n_char = int(input("Enter a Particular Number untill to read"))

            print(f.readline(n_char))
        
        case 5 : 

            break
            