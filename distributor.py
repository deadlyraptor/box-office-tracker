import sqlite3

# Connect to database
# conn = sqlite3.connect('/home/javier/box_office_tracker.db')
# c = conn.cursor()
# A class, Distributor, that is used for various properties
# associated with a distributor.


class Distributor:

    # Class constructor.
    def __init__(self, name, payee, address, city, state, zip):
        self.name = name
        self.payee = payee
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

kino_lorber = Distributor('Kino Lorber',
                          'Kino Lorber',
                          '333 West 39th Street',
                          'New York',
                          'New York',
                          '10018')

park_circus = Distributor('Park Circus',
                          'Park Circus, Inc.',
                          '11846 Ventura Blvd, Suite 140',
                          'Studio City',
                          'California',
                          '91604')

universal = Distributor('Universal Pictures',
                        'Universal Film Exchanges, Inc.',
                        'PO Box 848270',
                        'Dallas',
                        'Texas',
                        '75284')


def addDis(self):
    conn = sqlite3.connect('/home/javier/box_office_tracker.db')
    c = conn.cursor()
    dis_list = [self.name, self.payee, self.address,
                self.city, self.state, self.zip]
    c.execute('INSERT into distributors VALUES (NULL, ?, ?, ?, ?, ?, ?)', dis_list)
    conn.commit()
    conn.close()

addDis(park_circus)
addDis(universal)
