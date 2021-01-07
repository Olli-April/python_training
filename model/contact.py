from sys import maxsize

class Contact:
    def __init__(self, first_name=None, last=None, address=None, id=None):
        self.name = first_name
        self.last = last
        self.address = address
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.last)

    def __eq__(self, other):
        return(self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.last == other.last

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize