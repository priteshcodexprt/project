class Train :
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats


    def getStatus(self):
        print(f"the name of the train is{self.name}")
        print(f"The seats available in the train are {self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is : {self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print(f"your ticket has been booked! your seats number is {self.seats}")
            self.seats= self.seats -1

        else:
            print("sorry this ticket is canceled")


intercity=Train ("Intercity Express : 14015",90,300)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.fareInfo()
