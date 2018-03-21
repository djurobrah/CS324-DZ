class BankAccount:

    def __init__(self, amount = 0):
        self.amount = amount
        print("Uspesno otvoren racun. Racun trenutno sadrzi: {}".format(self.amount))

    def deposit(self, amount):
        self.amount += amount
        print("Uplata od {} uspesno izvrsena, trenutno stanje racuna je {} ".format(amount, self.amount))

    def withdraw(self, amount):
        self.amount -= amount
        print("Sa racuna uspesno skinuto {}, trenutno stanje racuna je {} ".format(amount, self.amount))

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount
