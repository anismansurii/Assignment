
class Ticket_Management:

    def __init__(self , passenger_details , bus_ticket_details , route_available ):
        self.passenger_details = passenger_details
        self.bus_ticket_details = bus_ticket_details
        self.route_available = route_available

    def available_routes(self):
        data = self.route_available
        for item in data:
            list_travel_data = data[item]
            print(f" {item} {list_travel_data[0]} To {list_travel_data[1]} Price : {list_travel_data[2]}")


    def Book_ticket(self):
        
        print("This Routes are Available ")
        self.available_routes()

        while True:

            choice = int(input('Enter a Choice of Bus Number Ex.1,2,3.. : '))
            if choice in self.route_available:
                break
            else:
                print("Enter Valid Bus Number")

        name = input("Enter Name of Passenger : ")
        age = int(input("Enter Age of Passenger : "))
        contact_details = input("Enter Mobile Number of Passenger : ")
        
        p_data = {
            "Name" : name ,
            "Age" : age , 
            "Mobile_Number" : contact_details ,
            "Bus_id" : choice
        }
        print("Bus Tickets Available : ")

        ticket_data = self.bus_ticket_details[choice]
        li_tick_avail = []
        for seat_number in range(1,41):
            if ticket_data[seat_number-1]==0:
                li_tick_avail.append(seat_number)
                print(seat_number , end=" ")
        print()
        
        while True:
            seat_n = int(input("Enter a Seat Number to Move Forward : "))
            if seat_n in li_tick_avail:
                break
            else:
                print("Enter a Valid Seat Number : ")
        

        Unique_Ticket_id = f"{choice}_{seat_n}"

        new_bus_tick_data = ticket_data
        new_bus_tick_data[seat_n-1] = Unique_Ticket_id
        self.bus_ticket_details[choice] = new_bus_tick_data

        full_data = {}

        full_data[Unique_Ticket_id] = p_data
        self.passenger_details.update(full_data) 

        print(self.passenger_details)
        for item in self.bus_ticket_details:
            for i in self.bus_ticket_details[item]:
                if i != 0 :
                    print("Bus Number" ,item , i)

    def view_ticket(self , ticket_id):
        
        bus_number = int(ticket_id[0])
        
        data = self.bus_ticket_details[bus_number]
        route_details = self.route_available[bus_number]
        

        if ticket_id in data:
            seat_number = data.index(ticket_id)
            print(f'Your Seat Number For Bus From {route_details[0]} To {route_details[1]} : {seat_number}')
        else:
            print("Invalid Ticket Id ")

    def cancel_ticket(self , ticket_id):

        bus_number, seat_number = ticket_id.split('_')
        bus_number, seat_number = int(bus_number), int(seat_number)

        # Remove passenger details
        if ticket_id in self.passenger_details:
            self.passenger_details.pop(ticket_id)
        else:
            print("Ticket ID not found in passenger records.")
            return

        # Mark the seat as available again (seat index = seat_number - 1)
        if bus_number in self.bus_ticket_details and 1 <= seat_number <= len(self.bus_ticket_details[bus_number]):
            self.bus_ticket_details[bus_number][seat_number - 1] = 0   # reset seat to available
        else:
            print("Invalid bus or seat number.")
            return

        print("Ticket cancelled successfully.")
        print("Updated Passenger Details:", self.passenger_details)
        print(f"Updated Seat Status for Bus {bus_number}:", self.bus_ticket_details[bus_number])

Travel1 = Ticket_Management(passenger_details = {} ,
                            
                             bus_ticket_details = {
                                        1 :  [0] * 40  , 
                                        2 :  [0] * 40  , 
                                        3 :  [0] * 40  , 
                                        4 :  [0] * 40  , 
                                        5 :  [0] * 40  , 
                                        6 :  [0] * 40  , 
                                        7 :  [0] * 40 , 
                                                    } , 
                            
                            route_available = {
                                                    1 : ['Ahmedabad' , 'Mumbai' , 1200] , 
                                                    2 : ['Mumbai' , 'Delhi' , 2000] ,
                                                    3 : ['Delhi' , 'Jaipur' , 1000] , 
                                                    4 : ['Jaipur' , 'Agra' , 2500] , 
                                                    5 : ['Agra' , 'Kolkata' , 5000] ,
                                                    6 : ['Kolkata' , 'Ranchi' , 3000] , 
                                                    7 : ['Kolkata' , 'Agartala' , 4500]
                                                }
                            )
while True:
    print("1 . Show Available Routes and Price " , "2 . Book Tiket " , "3 . View Ticket " , "4 . Cancel Ticket " , "5 . Exti " , sep = '\n')

    choice = int(input("Enter Operation Choice to Perform : "))

    match choice:
        case 1 :
            Travel1.available_routes()
        case 2:
            Travel1.Book_ticket()
        case 3:
            id = input("Enter Your ticket id")
            Travel1.view_ticket(id)
        case 4:
            id= input("Enter your ticket id : ")
            Travel1.cancel_ticket(id)
        case 5 :
            break
        case _:
            print("invalid action")