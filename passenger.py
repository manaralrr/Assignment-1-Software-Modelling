class Passenger:

    def __init__(self,name,passport_no,seat):
          self.name = name
          self.passport_no = passport_no
          self.booking_ref = None
          self.seat = seat
          self.sp_needs = None
    
    def setname(self,name):
        self.name = name

    def getname(self):
        return self.name
    
    def set_passport_no(self,passport_no):
        self.passport_no = passport_no
    
    def get_passport_no(self):
        return self. passport_no

    def assign_booking_ref(self):
        '''This function assigns a unique booking reference number.'''
        # assign a random book reference for boarding pass
        self.booking_ref = '5A6BCD78'

    def request_assistance(self):
        '''The function checks whether a passenger wants special assistance or not'''
        pass 
          
