import pymysql

class Person:

    def __init__(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = age
        print("Uspesno kreirana nova osoba: {}, {}, ({})".format(self.name, self.lastName, self.age))

    def selectAll(self):
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='cs324')
        results = []
        cursor = connection.cursor()
        cursor.execute("select * from person")
        for response in cursor:
            results.append(response)
        cursor.close()
        connection.close();
        return results;

    def insert(self):
        connection = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='cs324')
        cursor = connection.cursor()
        sql = "insert into person(name, lastname, age) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.name, self.lastName, self.age))
        connection.commit()
        connection.close()
