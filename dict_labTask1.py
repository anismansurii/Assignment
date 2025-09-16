# To check if marks greater than 200
dict_marks = {1:210 , 2:234 , 3:256 , 4:187 , 5:190}
for i in dict_marks.keys():
    if dict_marks[i]>200:
        print(f"{i} : {dict_marks[i]}")

# sum of all students marks 
sum = 0
for i in dict_marks.keys():
    sum += dict_marks[i]
print(f"Total Marks of Class is {sum}")

