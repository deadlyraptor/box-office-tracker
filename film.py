"""
This program creates films and distributors.
"""
import math
# import distributor
import datetime
import sqlite3

# A class, Film, that is used for various properties associated with a
# film booking.


class Film:

    # Global variables, usually monetary values that are initially 0.
    gross = 0.0
    overage = 0.0
    posted = False
    settled = False
    totalPaid = 0.0
    net = 0.0
    mgNum = None
    oNum = None
    mgDate = None
    oDate = None

    # Class constructor.
    def __init__(self,
                 name,
                 distributor,
                 start_date,
                 end_date,
                 guarantee,
                 percentage):
        self.name = name
        self.distributor = distributor
        self.start_date = start_date
        self.end_date = end_date
        self.guarantee = float(guarantee)
        self.percentage = (float(percentage)/100)

    # Returns the gross of a film; initially 0.
    def get_gross(self):
        # print('The {} gross is {}.'.format(self.name, self.gross))
        return self.gross

    # Sets the gross of a film to a new value input by user.
    def set_gross(self, gross):
        self.gross = gross

    # Returns the overage of a film; initially 0.
    def get_overage(self):
        # print('The {} overage is {}.'.format(self.name,self.overage))
        return self.overage
    """
    Sets the overage of a film to a new value using the following formula:

    if gross * percentage > guarantee:
        overage == (gross * percentage) - guarantee
    else:
        overage == 0.0
    """
    def set_overage(self):
        if self.get_gross() * self.percentage > self.guarantee:
            newOverage = round(((self.get_gross() * self.percentage) -
                                self.guarantee), 2)
            self.overage = newOverage
        else:
            pass

    # Returns False if film has been posted to QuickBooks (initial state)
    # or True if it has.
    def is_posted(self):
        return self.posted

    # Sets the posted status of a film to True.
    def set_posted(self):
        postedStatus = input('Has the film been posted? y/n: ')
        if postedStatus == 'y':
            self.posted = True
        else:
            pass

    # Returns False if film has been settled with distributor (initial state)
    # or True if it has.
    def is_settled(self):
        return self.settled

    # Sets the settled status of a film to True.
    def set_settled(self):
        settledStatus = input('Has the film been settled? y/n: ')
        if settledStatus == 'y':
            self.settled = True
        else:
            pass

    # Returns the total amount paid on a film; initially 0.
    def get_total(self):
        return self.totalPaid

    # Sets the total amount paid on a film.
    def set_total(self):
        newTotal = (self.guarantee + self.get_overage())
        self.totalPaid = newTotal

    # Returns the net profit made on a film; initially 0.
    def get_net(self):
        return self.net

    # Sets the net profit made on a film
    # by subtracting the total paid from the gross.
    def set_net(self):
        newNet = (self.get_gross() - self.get_total())
        self.net = newNet

    # Returns the minimum guarantee check number.
    def get_mgnum(self):
        return self.mgNum

    # Sets the minimum guarantee check number.
    def set_mgnum(self):
        newMGnum = input('Minimum guarantee check number: ')
        self.mgNum = newMGnum

    # Returns the overage check number.
    def get_onum(self):
        return self.oNum

    # Sets the overage check number.
    def set_onum(self):
        newOnum = input('Overage check number: ')
        self.oNum = newOnum

    # Returns the date minimum guarantee check was sent.
    def get_mgDate(self):
        return self.mgDate

    # Sets the date minimum guarantee check was sent.
    def set_mgDate(self):
        date = input('Minimum guarantee date: ')
        newDate = datetime.datetime.strptime(date, '%m/%d')
        self.mgDate = newDate.strftime('%m/%d')

    # Returns the date overage check was sent.
    def get_odate(self):
        return self.oDate

    # Sets the date overage check was sent.
    def set_odate(self):
        date = input('Overage check date: ')
        newDate = datetime.datetime.strptime(date, '%m/%d')
        self.oDate = newDate.strftime('%m/%d')


def addFilm(self):
    conn = sqlite3.connect('/home/javier/box_office_tracker.db')
    c = conn.cursor()
    film_list = [self.name, self.distributor, self.start_date,
                 self.end_date, self.guarantee, self.percentage]
    c.execute('INSERT into films VALUES (?, ?, ?, ?, ?, ?)', film_list)
    conn.commit()
    conn.close()

nosferatu = Film('Nosferatu', 'Kino Lorber', '10/29', '10/19', 250, '35')
isla_bonita = Film('Isla Bonita', 'Imagina', '7/24', '7/30', 0, '35')

addFilm(nosferatu)
addFilm(isla_bonita)

"""
print('Nosferatu values:')
print('Initial gross: {}'.format(nosferatu.get_gross()))
newGross = 100  # eval(input('Enter gross: '))
nosferatu.set_gross(newGross)
print('New gross: {}'.format(nosferatu.get_gross()))
print('Initial overage: {}'.format(nosferatu.get_overage()))
nosferatu.set_overage()
print('New overage: {}'.format(nosferatu.get_overage()))
nosferatu.set_total()
print('Total paid: {}'.format(nosferatu.get_total()))
nosferatu.set_net()
print('Net profit: {}'.format(nosferatu.get_net()))
nosferatu.set_mgnum()
print('Minimum guarantee check number: {}'.format(nosferatu.get_mgnum()))
nosferatu.set_onum()
print('Overage check number: {}'.format(nosferatu.get_onum()))
nosferatu.set_mgDate()
print('Minimum guarantee sent: {}.'.format(nosferatu.get_mgDate()))
nosferatu.set_odate()
print('Overage sent: {}.'.format(nosferatu.get_odate()))

print()

print('Isla Bonita values:')
print('Initial gross: {}'.format(isla_bonita.get_gross()))
newGross = 10475
isla_bonita.set_gross(newGross)
print('New gross: {}'.format(isla_bonita.get_gross()))
print('Initial overage: {}'.format(isla_bonita.get_overage()))
isla_bonita.set_overage()
print('New overage: {}'.format(isla_bonita.get_overage()))
isla_bonita.set_total()
print('Total paid: {}'.format(isla_bonita.get_total()))
isla_bonita.set_net()
print('Net profit: {}'.format(isla_bonita.get_net()))
print('Minimum guarantee check number: {}'.format(isla_bonita.get_mgnum()))
"""
