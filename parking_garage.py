class ParkingGarage():
    ticketPrice = 25
    tickets = 50
    parking_spaces = 50

    def __init__(self, current_ticket=False):
        self.current_ticket = current_ticket

    def takeTicket(self):
        ParkingGarage.tickets -= 1
        ParkingGarage.parking_spaces -= 1
    
    def payForParking(self):
        total_paid = 0
        pay = input("One ticket is $25.\nAdd Cash Amount in Dollars OR Insert Credit Card (Enter 'C'): ")
        if pay.lower() == 'c':
            total_paid = 25
            self.current_ticket = True
            print("Your ticket has been paid. You have 15 minutes to leave.")
            self.leaveGarage()
        elif pay.isdigit():
            if ParkingGarage.ticketPrice > int(pay):
                balanceOwed = ParkingGarage.ticketPrice - int(pay)
                complete_payment = input(f"Enter ${balanceOwed} (in # of dollars): ")
                total_paid = int(pay) + balanceOwed
                if total_paid == balanceOwed + int(pay):
                    print("Your ticket has been paid. You have 15 minutes to leave.")
                    self.current_ticket == True
                    self.leaveGarage()
                elif total_paid < balanceOwed + int(pay):
                    balanceOwed = ParkingGarage.ticketPrice - (int(pay) + int(complete_payment))
                    print(balanceOwed)
                    self.payForParking()

            elif int(pay) > ParkingGarage.ticketPrice:
                changeBack = int(pay) - ParkingGarage.ticketPrice
                print(f'You will receive ${changeBack} back in change.')
                self.leaveGarage()
                self.current_ticket == True
            else:
                self.current_ticket == True
                print("Your ticket has been paid. You have 15 minutes to leave.")
                self.leaveGarage()
        else:
            print("Invalid Option: Please enter dollar amount in numbers OR enter 'c' to pay with Credit Card")
            self.payForParking()

    def leaveGarage(self):
        if self.current_ticket == False:
            self.payForParking()
        else:
            ParkingGarage.tickets += 1
            ParkingGarage.parking_spaces += 1
            print("Thank You, have a nice day")
        
                # Once paid, display message "Thank you, have a nice day!"
        # Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        # Update tickets list to increase by 1 (meaning add to the tickets list)
   # pass


Customer1 = ParkingGarage()

Customer2 = ParkingGarage()

Customer1.takeTicket()
Customer2.takeTicket()

print(ParkingGarage.tickets)
print(ParkingGarage.parking_spaces)


Customer1.payForParking()
Customer2.payForParking()

print(ParkingGarage.tickets)
print(ParkingGarage.parking_spaces)


























