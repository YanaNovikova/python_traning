from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def randomstring(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                                home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="",
                                address2="", phone2="", notes="")] + [
    Contact(firstname=randomstring("firstname", 10), middlename=randomstring("middlename", 10), lastname=randomstring("lastname", 10),
            nickname=randomstring("nickname", 10), title=randomstring("title", 5), company=randomstring("company", 20), address=randomstring("address", 20),
            home=randomstring("home", 11), mobile=randomstring("mobile", 11), work=randomstring("work", 11), fax=randomstring("fax", 15),
            email=randomstring("email", 10), email2=randomstring("email2", 10), email3=randomstring("email3", 10), homepage=randomstring("homepage", 15),
            address2=randomstring("address2", 20), phone2=randomstring("phone2", 11), notes=randomstring("notes", 20))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))