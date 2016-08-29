"""
This program creates films and distributors.
"""
import math
# A class, Film, that is used for various properties associated with a film booking.
class Film:

    # Global variables, usually monetary values that are initially 0.
    gross = 0.0
    overage = 0.0
    posted = False
    settled = False

    # Class constructor.
    def __init__(self, name, distributor, start_date, end_date, guarantee, percentage):
        self.name = name
        self.distributor = distributor
        self.start_date = start_date
        self.end_date = end_date
        self.guarantee = float(guarantee)
        self.percentage = (float(percentage)/100)

    # Returns the gross of a film; initially 0.
    def get_gross(cls):
        return cls.gross

    # Sets the gross of a film to a new value input by user.
    def set_gross(cls, gross):
        cls.gross = gross

    # Returns the overage of a film; initially 0.
    def get_overage(cls):
        return cls.overage

    # Sets the overage of a film to a new value using a film's gross, percentage, and a formula.
    def set_overage(self):
        newOverage = round(((self.get_gross() * self.percentage) - self.guarantee),2)
        self.overage = newOverage
        
    # Returns False if film has been posted to QuickBooks (initial state) or True if it has.
    def is_posted(self):
        return self.posted
    # Sets the posted status of a film to True.
    def set_posted(self):
        postedStatus = input('Has the film been posted? y/n: ')
        if postedStatus == 'y':
            self.posted = True
        else:
            pass

    # Returns False if film has been settled with distributor (initial state) or True if it has.
    def is_settled(self):
        return self.settled
    # Sets the settled status of a film to True.
    def set_settled(self):
        settledSatus = input('Has the film been settled? y/n: ')
        if settledSatus == 'y':
            self.settled = True
        else:
            pass

# A class, Distributor, that is used for various properties associated with a distributor.
class Distributor:

    # Class constructor.
    def __init__(self, name, payable, address, city, state, zip):
        self.name = name
        self.payable = payable
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

kino_lorber = Distributor('Kino Lorber', 'Kino Lorber', '333 West 39th Street', 'New York', 'New York', '10018')
nosferatu = Film('Nosferatu', kino_lorber, '10/29', '10/19', 250, '35')
isla_bonita = Film('Isla Bonita', 'Imagina', '7/24', '7/30', 0, '35')

print('Nosferatu values:')
print('Initial gross: ' + str(nosferatu.get_gross()))
newGross = 1000.0  # eval(input('Enter gross: '))
nosferatu.set_gross(newGross)
print('New gross: ' + str(nosferatu.get_gross()))
print('Initial overage: ' + str(nosferatu.get_overage()))
nosferatu.set_overage()
print('New overage: ' + str(nosferatu.get_overage()))

print()

print('Isla Bonita values:')
print('Initial gross: ' + str(isla_bonita.get_gross()))
newGross = 10475
isla_bonita.set_gross(newGross)
print('New gross: ' + str(isla_bonita.get_gross()))
print('Initial overage: ' + str(isla_bonita.get_overage()))
isla_bonita.set_overage()
print('New overage: ' + str(isla_bonita.get_overage()))

nosferatu.set_settled()
print(nosferatu.is_settled())