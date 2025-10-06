class School_Management:
    def __init__(self):
        self.data_main = {}  

    def new_admission(self):
        name = input("Enter student name: ")

        while True:
            try:
                age = int(input("Enter student age: "))
                if 5 <= age <= 18:
                    break
                else:
                    print("Invalid Age! Age must be between 5 and 18.")
            except ValueError:
                print("Enter a valid number for age.")

        class_no = int(input("Enter student Class: "))

        while True:
            contact_no = input("Enter a Mobile number: ")
            if contact_no.isdigit() and len(contact_no) == 10:
                break
            else:
                print("Enter a valid 10-digit number.")

        unique_id = f"{name[:2]}{age}{class_no}{contact_no[:3]}"

        student_data = {
            "Name": name,
            "Age": age,
            "Standard": class_no,
            "Mobile_number": contact_no
        }

        self.data_main[unique_id] = student_data

        print(f"Successfully added your unique ID is {unique_id}")
    
    def get_student(self):
        while True:
            id = input("Enter a Student ID: ")
            if id in self.data_main:
                break
            else:
                print("Invalid ID")

        student_data = self.data_main[id]
        print("Student Details")
        print("Student ID:", id)
        for key, value in student_data.items():
            print(f"{key} : {value}")
        print("Data Printed Successfully")

    def update_stud_info(self):
        while True:
            id = input("Enter a Student ID: ")
            if id in self.data_main:
                break
            else:
                print("Invalid ID")
    
        student_data = self.data_main[id]

        while True:
            print("Update Menu")
            print("1. Change Mobile Number")
            print("2. Change Class")
            print("3. Exit Edit Menu")
            choice = int(input("Enter a Choice: "))

            if choice == 1:
                while True:
                    new_number = input("Enter New Number: ")
                    if len(new_number) == 10 and new_number.isdigit():
                        student_data["Mobile_number"] = new_number
                        print("Mobile number updated!")
                        break
                    else:
                        print("Enter a valid Number")

            elif choice == 2:
                new_class = int(input("Enter a new class: "))
                student_data["Standard"] = new_class
                print("Class updated")

            elif choice == 3:
                break
            else:
                print("Invalid choice.")

        self.data_main[id] = student_data
        print(f"Student Data Updated for ID: {id}")
        print(f"{id} : {self.data_main[id]}")

    def delete_student(self):
        while True:
            id = input("Enter a Student ID: ")
            if id in self.data_main:
                break
            else:
                print("Invalid ID")

        deleted_student = self.data_main.pop(id)
        print(f"Student with id {id} deleted successfully ")
        print("Deleted Student:", deleted_student)


stud = School_Management()

while True:
    
    print("School Management Menu")
    print("1. Add New Student")
    print("2. View Student Details")
    print("3. Update Student Info")
    print("4. Remove Student Record")
    print("5. Exit")
    
    try:
        choice = int(input("Enter an Action to Perform: "))
    except :
        print("Enter a valid choice (1-5)")
        continue

    match choice:
        case 1:
            stud.new_admission()
        case 2:
            stud.get_student()
        case 3:
            stud.update_stud_info()
        case 4:
            stud.delete_student()
        case 5:
            break
        case _:
            print("Invalid choice, please try again.")
