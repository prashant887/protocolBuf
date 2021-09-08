import addressbook_pb2
import employee_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
"""
phone_home = person.phones.add()
phone_home.number = "555-4321"
phone_home.type = addressbook_pb2.Person.HOME

phone_mobile = person.phones.add()
phone_mobile.number = "555-4322"
phone_mobile.type = addressbook_pb2.Person.MOBILE

phone_work = person.phones.add()
phone_work.number = "555-4323"
phone_work.type = addressbook_pb2.Person.WORK
"""

data = [addressbook_pb2.Person.PhoneNumber(number="555-4324"),
        addressbook_pb2.Person.PhoneNumber(number="555-4321", type=addressbook_pb2.Person.MOBILE),
        addressbook_pb2.Person.PhoneNumber(number="555-4322", type=addressbook_pb2.Person.HOME),
        addressbook_pb2.Person.PhoneNumber(number="555-4323", type=addressbook_pb2.Person.WORK),
        ]
print(data, '\n')
person.phones.extend(data)

print("=========phones==========\n")
print(person.phones)

print("=========person==========\n")

print(person)

for dat in person.phones:
    print(dat.number)

address = addressbook_pb2.AddressBook()
address.people.extend([person,person])

print("\n==========\n")
print(address)


f = open('buffout', "wb")
f.write(address.SerializeToString())
f.close()



address_book = addressbook_pb2.AddressBook()

# Read the existing address book.
f = open('buffout', "rb")
address_book.ParseFromString(f.read())
f.close()
print("\n Read From File \n")
print(address_book)