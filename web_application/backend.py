class Event:
    event_event_id = []
    event_name_list = []
    event_venue_list = []
    event_date_list = []
    event_time_list = []
    event_category_list = []
    event_price_list = []


    def __init__(self,name,venue,date,time,category,price):
        self.name = name
        self.venue = venue
        self.date = date
        self.time = time
        self.category = category
        self.price = price
    
    def Create_Event(self):
        """
        create an event 
        """
        Event.event_name_list.append(self.name)
        Event.event_venue_list.append(self.venue)
        Event.event_date_list.append(self.date)
        Event.event_time_list.append(self.time)
        Event.event_category_list.append(self.category)
        Event.event_price_list.append(self.price)
        id  = len(Event.event_name_list)
        Event.event_event_id.append(id)
    

    def view_event(cls):
        """
        view the event.

        """
        for i in range(len(cls.event_name_list)):
            print(f"""id:{cls.event_event_id}---The event name is {cls.event_name_list[i]} organized at {cls.event_venue_list[i]} date={cls.event_date_list[i]} and time={cls.event_time_list[i]}. The event comes under {cls.event_category_list[i]} and prices of the ticket starts from {cls.event_price_list[i]}""")
            print(" ")

class Tickets(Event):
    booked=[]

    def __init__(self,name)->None:
        self.name =name


    def book_ticket(self):
        """
        Book's the ticket by taking the name and 
        """
        self.view_event()
        
        try:
            book = int(input("enter the event_event_id to book the tickets"))
            if(book in self.event_event_id ):
                index = self.event_event_id.index(book)
                amount =int(input("enter the amount to book the tickets"))
                if(amount>=self.event_price_list[index]):
                    print("congratulations your ticket has booked ")
                    Tickets.booked.append(index)
                else:
                    print("you have entred less price than ticket please go through options again")
                    self.book_ticket()
            else:
                print("your entered event id has not found please tey again") 
                self.book_ticket()  

        except Exception as ex:
            print("INVALID EVENT ID PLEASE TRY AGAIN WITH VALID EVENT-ID AS DISPLAYED")
            self.book_ticket()
    

    def view_tickets(cls):
        """
        Viewing the tickets that are booked by the users.

        """
        if(len(cls.booked)>0):
            for i in (cls.booked):
                print(f"you have booked your tickets for The event {cls.event_name_list[i]} organized at {cls.event_venue_list[i]} date={cls.event_date_list[i]} and time={cls.event_time_list[i]}. The event comes under {cls.event_category_list[i]} and prices of the ticket is {cls.event_price_list[i]}")
        else:
            print("you have not booked any tickets")



obj1 = Event('wedding','hyd','22-03-22','23:11','marriage',77777)
obj1.Create_Event()
obj1.view_event()
obj1 = Tickets('mani')
obj1.book_ticket()
obj1.view_tickets()