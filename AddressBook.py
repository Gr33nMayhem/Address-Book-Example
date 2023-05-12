class AddressBook:
    def __int__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search(self, name):
        for person in self.people:
            if person.get_name() == name:
                return person
        return None