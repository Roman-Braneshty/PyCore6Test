class AdressBook:

    def __init__(self, fullname, phone):
        self.fullname = fullname
        self.phone = phone

    def __str__(self):
        return f'AdressBook({self.fullname}, {self.phone})'


    def add_new_phone(self, phone):
        self.phone = phone
