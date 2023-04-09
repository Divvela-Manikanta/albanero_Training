class Event:
    event_info = {}

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
        id  = len(Event.event_info)+1
        Event.event_info[id] = dict({'id':id,'name':self.name, 'venue':self.venue,'date':self.date,'time': self.time,'category':self.category,'price':self.price})
    
    def view_event(cls):
        """
        view the event.

        """
        for id in cls.event_info:
            print(f"""id:{cls.event_info[id]['id']}--->The event name is {cls.event_info[id]['name']} organized at {cls.event_info[id]['venue']} date={cls.event_info[id]['date']} and time={cls.event_info[id]['time']}. The event comes under {cls.event_info[id]['category']} and prices of the ticket starts from {cls.event_info[id]['price']}""")
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
            book = int(input("enter the id to book the tickets"))
            if(book in self.event_info ):
                amount =int(input("enter the amount to book the tickets"))
                print(self.event_info[book]['price'])
                if(amount>=self.event_info[book]['price']):
                    print("congratulations your ticket has booked ")
                    Tickets.booked.append(book)
                else:
                    print("you have entred less price than ticket please go through options again")
                    self.book_ticket()
            else:
                print("your entered event id has not found please tey again") 
                self.book_ticket()  

        except Exception as ex:
            print("SOMETHING WENT WRONG PLEASE TRY AGAIN WITH VALID EVENT-ID AS DISPLAYED")
            self.book_ticket()
    

    def view_tickets(cls):
        """
        Viewing the tickets that are booked by the users.

        """
        if(len(cls.booked)>0):
            for id in (cls.booked):
                print(f"you have booked your tickets for The event The event name is {cls.event_info[id]['name']} organized at {cls.event_info[id]['venue']} date={cls.event_info[id]['date']} and time={cls.event_info[id]['time']}. The event comes under {cls.event_info[id]['category']} and prices of the ticket starts from {cls.event_info[id]['price']}")
        else:
            print("you have not booked any tickets")



obj1 = Event('wedding','hyd','22-03-22','23:11','marriage',77777)
obj1.Create_Event()
obj1.view_event()
obj1 = Tickets('mani')
obj1.book_ticket()
obj1.view_tickets()