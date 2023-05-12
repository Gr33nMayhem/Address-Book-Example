class Person:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.phone}"

    def __repr__(self):
        return f"Person({self.name}, {self.phone})"

    def get_name(self):
        return self.name
