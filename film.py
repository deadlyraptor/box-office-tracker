import math
import datetime
import db

# A class, Film, that is used for various properties associated with a
# film booking.


class Film:

    # Global variables, usually monetary values that are initially 0.
    gross = 0.0
    overage = 0.0
    total_paid = 0.0
    net = 0.0
    mg_num = None
    mg_date = None
    o_num = None
    o_date = None
    posted = False
    settled = False

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


class Calls:
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
            new_overage = round(((self.get_gross() * self.percentage) -
                                self.guarantee), 2)
            self.overage = new_overage
        else:
            pass

    # Returns False if film has been posted to QuickBooks (initial state)
    # or True if it has.
    def is_posted(self):
        return self.posted

    # Sets the posted status of a film to True.
    def set_posted(self):
        posted_status = input('Has the film been posted? y/n: ')
        if posted_status == 'y':
            self.posted = True
        else:
            pass

    # Returns False if film has been settled with distributor (initial state)
    # or True if it has.
    def is_settled(self):
        return self.settled

    # Sets the settled status of a film to True.
    def set_settled(self):
        settled_status = input('Has the film been settled? y/n: ')
        if settled_status == 'y':
            self.settled = True
        else:
            pass

    # Returns the total amount paid on a film; initially 0.
    def get_total(self):
        return self.total_paid

    # Sets the total amount paid on a film.
    def set_total(self):
        new_total = (self.guarantee + self.get_overage())
        self.total_paid = new_total

    # Returns the net profit made on a film; initially 0.
    def get_net(self):
        return self.net

    # Sets the net profit made on a film
    # by subtracting the total paid from the gross.
    def set_net(self):
        new_net = (self.get_gross() - self.get_total())
        self.net = new_net

    # Returns the minimum guarantee check number.
    def get_mgnum(self):
        return self.mg_num

    # Sets the minimum guarantee check number.
    def set_mgnum(self):
        new_mgnum = input('Minimum guarantee check number: ')
        self.mg_num = new_mgnum

    # Returns the overage check number.
    def get_onum(self):
        return self.o_num

    # Sets the overage check number.
    def set_onum(self):
        new_onum = input('Overage check number: ')
        self.o_num = new_onum

    # Returns the date minimum guarantee check was sent.
    def get_mgDate(self):
        return self.mg_date

    # Sets the date minimum guarantee check was sent.
    def set_mgDate(self):
        date = input('Minimum guarantee date: ')
        new_date = datetime.datetime.strptime(date, '%m/%d')
        self.mg_date = new_date.strftime('%m/%d')

    # Returns the date overage check was sent.
    def get_odate(self):
        return self.o_date

    # Sets the date overage check was sent.
    def set_odate(self):
        date = input('Overage check date: ')
        new_date = datetime.datetime.strptime(date, '%m/%d')
        self.o_date = new_date.strftime('%m/%d')

# Function generates the sql command and parameters then passes them to db.save.


def add(self):
    sql = '''INSERT INTO films VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    params = [self.name, self.distributor, self.start_date,
              self.end_date, self.percentage, self.guarantee,
              self.gross, self.overage, self.total_paid,
              self.net, self.mg_num, self.mg_date,
              self.o_num, self.o_date, self.posted, self.settled]
    db.save(sql, params)
