class Hosppital_Management:
    def __init__(self , data_original , doc_data):
        self.data_orginal = data_original
        self.doc_data = doc_data


    def save_patient_data(self):
        name_patient = input("Enter a name of patient: ")
        
        while True:
            try:
                age_patient = int(input("Enter age of patient: "))
                if 0 < age_patient < 120:
                    break
                print("Invalid age, try again.")
            except:
                print("Enter a valid number.")

        while True:
            contact_patient = input("Enter Mobile number of patient: ")
            if contact_patient.isdigit() and len(contact_patient) == 10:
                break
            print("Enter a valid 10-digit number.")

        patient_data_temp = {

            'Name': name_patient,
            "Age": age_patient,
            "Contact": contact_patient
        }

        # Use contact as unique key
        self.data_orginal[contact_patient] = patient_data_temp

        return contact_patient


    def show_doc_availability(self):
        print("Available Doctors:")
        print("1 . Dr Joshi 2 . Dr Mehta 3 . Dr Malik 4 . Dr Shah")
        preferred_doc = int(input("Enter your preferred doctor number: "))

        doc_dict = {
            1: "Dr.Joshi",
            2: "Dr.Mehta",
            3: "Dr.Malik",
            4: "Dr.Shah"
        }

        if preferred_doc not in doc_dict:
            print("Invalid doctor choice")
            return None

        key_dict = doc_dict[preferred_doc]

        print(f"Available slots for {key_dict}:" , end=" ")
        for key , value in self.doc_data[key_dict].items():
            if value == 'False':
                print(key , end=' ')
        print()



    def confirm_booking(self , doc_name, p_id):
        time_to_book = input("Select time to book (e.g., '10 AM', '12 PM', '2 PM', '3 PM'): ")

        if doc_name not in self.doc_data:
            print("Invalid doctor name")
            return
        
        if self.doc_data[doc_name][time_to_book] == "False":
            self.doc_data[doc_name][time_to_book] = "True"   # mark as booked

        else:
            print("Slot not available!")
            return

        # Save updated slots
        # Update patient record
        self.data_orginal[p_id]['Booking'] = {
            "booked": True,
            "Doc_name": doc_name,
            "time": time_to_book
        }

        print(f"Appointment confirmed with {doc_name} at {time_to_book}")
        print(self.data_orginal[p_id])


    def view_appointment(self):

        contact = input("Enter your registered mobile number: ")
        if contact in self.data_orginal and 'Booking' in self.data_orginal[contact]:
            booking = self.data_orginal[contact]['Booking']
            print(f"Appointment Details : Doctor: {booking['Doc_name']} , Time: {booking['time']}")
        else:
            print("No appointment found for this patient.")


    def cancel_appointment(self):
    
        contact = input("Enter your registered mobile number: ")

        if contact not in self.data_orginal or 'Booking' not in self.data_orginal[contact]:
            print("No appointment found to cancel.")
            return

        booking = self.data_orginal[contact]['Booking']
        doc_name = booking['Doc_name']
        time_slot = booking['time']

        # Free the doctor’s slot
      
        self.doc_data[doc_name][time_slot] = 'False'

        # can also use pop 
        del self.data_orginal[contact]['Booking']

        print(f"Appointment with {doc_name} at {time_slot} cancelled.")

    def show_doc_persistent(self):
        print("Available Doctors:")
        print("1 . Dr Joshi 2 . Dr Mehta 3 . Dr Malik 4 . Dr Shah")
        preferred_doc = int(input("Enter your preferred doctor number: "))

        doc_names = {
            1: "Dr.Joshi",
            2: "Dr.Mehta",
            3: "Dr.Malik",
            4: "Dr.Shah"
        }

        if preferred_doc not in doc_names:
            print("Invalid doctor choice")
            return None

        key_dict = doc_names[preferred_doc]

        count = 0
        for item in self.doc_data[key_dict].values():
            if item == 'True':
                count+=1

        print(f"Available slots for {key_dict}:")
        if count>3:
            print("Doctor is not persistent ")
        else:
            print("Doctor is persistent")

    # def Book_appointment(self):
    #     p_id = save_patient_data()
    #     doc_name = show_doc_availability(self.doctor_slot_data)
        
    #     if doc_name:
    #         confirm_booking(doc_name, p_id)

        

hospital_obj = Hosppital_Management({} , doc_data= {
                        "Dr.Joshi": {
                            "10 AM": "False",
                            "12 PM": "False",
                            "2 PM": "False",
                            "3 PM": "True"
                        },
                        "Dr.Mehta": {
                            "10 AM": "False",
                            "12 PM": "False",
                            "2 PM": "False",
                            "3 PM": "False"
                        },
                        "Dr.Malik": {
                            "10 AM": "False",
                            "12 PM": "False",
                            "2 PM": "False",
                            "3 PM": "False"
                        },
                        "Dr.Shah": {
                            "10 AM": "False",
                            "12 PM": "False",
                            "2 PM": "False",
                            "3 PM": "False"
                        }
                    })

# Run booking system
while True:
    print("1 . Book Appointment " , "2 . View / Cancel Appointment " , "3 . Doctor Availability " , "4 . Data Persistent" , "5 . Exit " , sep='\n')
    choice = int(input("Ente Choice of Action : "))
    match choice:

        case 1 :
            p_id = hospital_obj.save_patient_data()

            hospital_obj.show_doc_availability()

            print("1 . Dr Joshi 2 . Dr Mehta 3 . Dr Malik 4 . Dr Shah")
            preferred_doc = int(input("Enter your preferred doctor number: "))

            doc_dict = {
                    1: "Dr.Joshi",
                    2: "Dr.Mehta",
                    3: "Dr.Malik",
                    4: "Dr.Shah"
                }

            if preferred_doc not in doc_dict:
                print("Invalid doctor choice")
                pref_doc= None
            pref_doc = doc_dict[preferred_doc]
            hospital_obj.confirm_booking(pref_doc , p_id)
            
        case 2:
            while True:
                print("For View write V to cancel write C , E for exit : ")
                action = input("Enter Whether you want to view or cancel appointment : ")
                action = action.upper()
                if action == 'V':
                    hospital_obj.view_appointment()
                elif action == 'C':
                    hospital_obj.cancel_appointment()
                elif action=='E':
                    break
                elif action:
                    print("Invallid Action To view type 'v' to cancel write 'C' : ")
        case 3 :

            hospital_obj.show_doc_availability()

        case 4 :
            
            hospital_obj.show_doc_persistent()
        
        case 5: break

