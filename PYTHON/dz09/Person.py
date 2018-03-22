class Person:

    def __init__(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = age
        print("Uspesno kreirana nova osoba: {}, {}, ({})".format(self.name, self.lastName, self.age))

    def fetchPersons(connection):
        cursor = db.cursor()

        sql = "select * from table1"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print
            row[0]

        # disconnect from server
        db.close()
        print("Uplata od {} uspesno izvrsena, trenutno stanje racuna je {} ".format(amount, self.amount))

