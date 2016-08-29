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