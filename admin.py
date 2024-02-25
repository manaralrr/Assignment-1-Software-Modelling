class Admin:

    def __init__(self,access_level,flight_data,user_accounts):
        self.access_level = access_level
        self.flight_data = flight_data
        self.user_accounts = user_accounts
    
    def manage_user_accounts(self):
        '''The function updates the information associated to users.'''
        pass

    def update_flight_information(self):
        '''The function updates the flight information.'''
        pass

    def generate_report(self):
        '''The function generate the report according the the requirements.'''
        pass
