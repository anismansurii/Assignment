def lab_task1():
    with open("test1.txt" , 'a') as f:
        while True:
            data = input("Enter Context to append (Enter end/exit to exit ) ")
            data.strip()
            if data=='end' or data=='exit':
                break
            f.write(data)

def lab_task2():
    with open("test.txt" , 'r') as f :
        lines = f.read()
        with open('copy_test.txt' , 'w+') as copy_f:
            copy_f.write(lines)
            data_copied = copy_f.read()
            print(data_copied)

# to run any task call func ... 
# lab_task1()
# lab_task2()