class Flight:

    def __init__(self,airline,flight_no,origin,destination,dept_time,arrival_time,gate,dept_date):
        self.airline = airline
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.dept_time = dept_time
        self.arrival_time = arrival_time
        self.gate = gate
        self.dept_date = dept_date

    def update_status(self):
        '''The function regularly check the flight status and updates the pessangers about the same.'''
        pass

    def check_boarding_time(self):
        '''The function get a recond of the boarding time of the flight.'''
        pass
