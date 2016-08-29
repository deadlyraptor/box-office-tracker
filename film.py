"""
This program creates films and distributors.
"""
import math
import distributor
# A class, Film, that is used for various properties associated with a film booking.
class Film:

    # Global variables, usually monetary values that are initially 0.
    gross = 0.0
    overage = 0.0
    posted = False
    settled = False
    totalPaid = 0.0

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
    """
    Sets the overage of a film to a new value using the following formula:

    if gross * percentage > guarantee:
        overage == (gross * percentage) - guarantee
    else:
        overage == 0.0
    """
    def set_overage(self):
        if self.get_gross() * self.percentage > self.guarantee:
            newOverage = round(((self.get_gross() * self.percentage) - self.guarantee),2)
            self.overage = newOverage
        else:
            pass
        
    # Returns False if film has been posted to QuickBooks (initial state) or True if it has.
    def is_posted(cls):
        return cls.posted
    # Sets the posted status of a film to True.
    def set_posted(cls):
        postedStatus = input('Has the film been posted? y/n: ')
        if postedStatus == 'y':
            cls.posted = True
        else:
            pass

    # Returns False if film has been settled with distributor (initial state) or True if it has.
    def is_settled(cls):
        return cls.settled
    # Sets the settled status of a film to True.
    def set_settled(cls):
        settledStatus = input('Has the film been settled? y/n: ')
        if settledStatus == 'y':
            cls.settled = True
        else:
            pass

    # Returns the total amount paid on a film; initially 0.
    def get_total(cls):
        return cls.totalPaid
    # Sets the total amount paid on a film.
    def set_total(self):
        newTotal = (self.guarantee + self.get_overage())
        self.totalPaid = newTotal

nosferatu = Film('Nosferatu', 'Kino Lorber', '10/29', '10/19', 250, '35')
isla_bonita = Film('Isla Bonita', 'Imagina', '7/24', '7/30', 0, '35')

print('Nosferatu values:')
print('Initial gross: ' + str(nosferatu.get_gross()))
newGross = 25.0  # eval(input('Enter gross: '))
nosferatu.set_gross(newGross)
print('New gross: ' + str(nosferatu.get_gross()))
print('Initial overage: ' + str(nosferatu.get_overage()))
nosferatu.set_overage()
print('New overage: ' + str(nosferatu.get_overage()))
nosferatu.set_total()
print('Total paid: ' + str(nosferatu.get_total()))

print()

print('Isla Bonita values:')
print('Initial gross: ' + str(isla_bonita.get_gross()))
newGross = 10475
isla_bonita.set_gross(newGross)
print('New gross: ' + str(isla_bonita.get_gross()))
print('Initial overage: ' + str(isla_bonita.get_overage()))
isla_bonita.set_overage()
print('New overage: ' + str(isla_bonita.get_overage()))
isla_bonita.set_total()
print('Total paid: ' + str(isla_bonita.get_total()))