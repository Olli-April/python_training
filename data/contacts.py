from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1", middlename="middlename1", mobilephone="1234567"),
    Contact(firstname="firstname2", lastname="lastname2", middlename="middlename2", mobilephone="7654321")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", mobilephone="")] + [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 15),
            lastname=random_string("lastname", 15), mobilephone=random_string("7", 10))
    for i in range(5)]