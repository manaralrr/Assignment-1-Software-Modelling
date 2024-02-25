class CheckIn:

    def __init__(self,passenger,flight):
        self.passenger = passenger
        self.flight = flight

    def issue_boarding_pass(self):
        '''The function generates the boarding pass for the passenger'''
        print('BOARDING PASS')
        print(self.flight.airline)
        print('Passenger')
        print(self.passenger.name)
        print('From: ',self.flight.origin,'   To:',self.flight.destination)
        print('Flight:',self.flight.flight_no)
        print('Date:',self.flight.dept.date)
        print('Time:',self.flight.dept_time,'    Arrival Time:',self.flight.arrival_time)
        print('Terminal:',self.flight.terminal)
        print('Electrinic Ticket No: 629')
        print('Booking Reference:',self.passenger.booking_ref)
    
    def verify_booking(self):
        '''The function checks the check in status for the passenger'''
        pass
