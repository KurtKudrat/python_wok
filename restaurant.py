
'''A set of classes that represent restaurants '''

class Restaurant():

    def __init__(self,name,type):
        #initialize name and type attributes.
        self.name = name
        self.type = type
        self.number_served = 0


    def describe_restaurant(self):
        """describe the restaurant"""
        print(self.name.title() + " is a really good " + self.type.title() + " restaurant.")


    def open_restaurant(self):
        """open status """
        print(self.name.title() + " is open right now.")


    def set_number_served(self,num_served):
        # set the customer number for the restaurant
        self.number_served = num_served


    def increment_number_served(self,customer_num):
        # increment the customer number for the restaurant
        self.number_served =+ customer_num
