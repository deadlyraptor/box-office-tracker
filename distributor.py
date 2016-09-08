import db

# A class, Distributor, that contains various properties
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

# Function that adds a distributor to the database.


def add(self):
    sql = '''INSERT INTO distributors VALUES (NULL, ?, ?, ?, ?, ?, ?)'''
    params = [self.name, self.payee, self.address,
              self.city, self.state, self.zip]
    db.save(sql, params)
