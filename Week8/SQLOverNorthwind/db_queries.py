import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect(self.DB_NAME)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        #contend = self.file_reader("sql_requests.txt")
        #self.cursor.executescript(contend)
        #self.conn.commit

    DB_NAME = "northwind.db"

    ALL_EMPLOYEES = """
            SELECT FirstName, LastName, Title
            FROM Employees
    """

    CITY_EMPLOYEES = """
            SELECT FirstName, LastName, Title, City
            FROM Employees
            WHERE City = ?
    """

    EMPLOYEES_DEPART = """
            SELECT FirstName, LastName, Title
            FROM Employees
            WHERE Title LIKE '%Sales%'
    """

    FEMALE_EMPLOYEES = """
            SELECT FirstName, LastName, Title
            FROM Employees
            WHERE Title LIKE '%Sales%' AND
            (TitleOfCourtesy = 'Ms.' OR TitleOfCourtesy = 'Mrs.')
    """

    OLDEST_EMPLOYEES = """
            SELECT FirstName, LastName, BirthDate
            FROM Employees
            ORDER BY BirthDate
            LIMIT 5
    """

    LONGESTS_SERVING = """
            SELECT FirstName, LastName, HireDate
            FROM Employees
            ORDER BY HireDate
            LIMIT 5
    """

    REPORTS_TO_NOONE = """
            SELECT FirstName, LastName, ReportsTo
            FROM Employees
            WHERE ReportsTo IS NULL
    """


    WHO_REPORTS_TO = """
            SELECT E1.FirstName, E1.LastName, E2.FirstName, E2.LastName
            FROM Employees E1
            JOIN Employees E2 ON E1.ReportsTo = E2.EmployeeID
    """

    COUNT_FEMALE = """
            SELECT COUNT(EmployeeID)
            FROM Employees
            WHERE TitleOfCourtesy = 'Ms.' OR TitleOfCourtesy = 'Mrs.'
    """

    COUNT_MALE = """
            SELECT COUNT(EmployeeID)
            FROM Employees
            WHERE TitleOfCourtesy = 'Mr.' OR TitleOfCourtesy = 'Dr.'
    """

    DIFFERENT_CITY = """
            SELECT City, COUNT(City)
            FROM Employees
            GROUP BY City
    """

    ORDER_TO_EMPLOYEE = """
        SELECT O.OrderID, E.FirstName, E.LastName
        FROM Orders O
        JOIN Employees E ON O.EmployeeID = E.EmployeeID
    """

    ORDER_TO_SHIPPER = """
        SELECT O.OrderID, S.CompanyName
        FROM Orders O
        JOIN Shippers S ON O.ShipVia = S.ShipperID
    """

    COUNTRIES_TO_SHIP = """
        SELECT ShipCountry, COUNT(*)
        FROM Orders
        GROUP BY ShipCountry
    """

    EMPLOYEE_WITH_MOST_ORDERS = """
        SELECT E.FirstName, E.LastName, COUNT(O.OrderID) AS C
        FROM Orders O
        JOIN Employees E ON O.EmployeeID = E.EmployeeID
        GROUP BY E.EmployeeID
        ORDER BY C DESC
        LIMIT 1
    """

    CUSTOMER = """
        SELECT C.CompanyName, COUNT(O.OrderID) AS C
        FROM Orders O
        JOIN Customers C ON O.CustomerID = C.CustomerID
        GROUP BY C.CustomerID
        ORDER BY C DESC
        LIMIT 1
    """

    ORDER_SERVED = """
        SELECT O.OrderID, E.FirstName, E.LastName, C.CompanyName
        FROM Orders O
        JOIN Customers C ON O.CustomerID = C.CustomerID
        JOIN Employees E ON O.EmployeeID = E.EmployeeID
    """

    WHICH_SHIPPER = """
        SELECT C.CompanyName, S.CompanyName
        FROM Orders O
        JOIN Customers C ON O.CustomerID = C.CustomerID
        JOIN Shippers S ON O.ShipVia = S.ShipperID
    """


    @staticmethod
    def file_reader(filname):
        with open(filname, "r") as f:
            contend = f.read()
            return contend

    def all_employees(self):
        self.cursor.execute(self.ALL_EMPLOYEES)
        for row in self.cursor:
            print("{} {} : {}".format(row[0], row[1], row[2]))

    def city_employees(self, city):
        self.cursor.execute(self.CITY_EMPLOYEES, (city, ))
        for row in self.cursor:
            print("{} {} : {}, {}".format(row[0], row[1], row[2], row[3]))

    def employees_depart(self):
        self.cursor.execute(self.EMPLOYEES_DEPART)
        for row in self.cursor:
            print("{} {} : {}".format(row[0], row[1], row[2]))

    def female_employees(self):
        self.cursor.execute(self.FEMALE_EMPLOYEES)
        for row in self.cursor:
            print("{} {} : {}".format(row[0], row[1], row[2]))

    def oldest_employess(self):
        self.cursor.execute(self.OLDEST_EMPLOYEES)
        for row in self.cursor:
            print("{} {} : {}".format(row[0], row[1], row[2]))

    def longest_serving(self):
        self.cursor.execute(self.LONGESTS_SERVING)
        for row in self.cursor:
            print("{} {} : {}".format(row[0], row[1], row[2]))

    def who_is_theboss(self):
        self.cursor.execute(self.REPORTS_TO_NOONE)
        for row in self.cursor:
            print("{} {} : {}".format(row[0], row[1], row[2]))

    def who_reports_to(self):
        self.cursor.execute(self.WHO_REPORTS_TO)
        for row in self.cursor:
            print("{} {} : {} {}".format(row[0], row[1], row[2], row[3]))

    def count_famale(self):
        count = self.cursor.execute(self.COUNT_FEMALE).fetchone()
        print(count[0])

    def count_male(self):
        count = self.cursor.execute(self.COUNT_MALE).fetchone()
        print(count[0])

    def different_city(self):
        self.cursor.execute(self.DIFFERENT_CITY)
        for row in self.cursor:
            print("{} : {}".format(row[0], row[1]))

    def order_to_employee(self):
        self.cursor.execute(self.ORDER_TO_EMPLOYEE)
        for row in self.cursor:
            print("{} : {} {}".format(row[0], row[1], row[2]))

    def order_to_shipper(self):
        self.cursor.execute(self.ORDER_TO_SHIPPER)
        for row in self.cursor:
            print("{} : {}".format(row[0], row[1]))

    def countries_to_ship(self):
        self.cursor.execute(self.COUNTRIES_TO_SHIP)
        for row in self.cursor:
            print("{} : {}".format(row[0], row[1]))

    def employees_with_most_orders(self):
        self.cursor.execute(self.EMPLOYEE_WITH_MOST_ORDERS)
        for row in self.cursor:
            print("{} {} : {}".format(row[0], row[1], row[2]))

    def customer(self):
        self.cursor.execute(self.CUSTOMER)
        for row in self.cursor:
            print("{} : {}".format(row[0], row[1]))

    def orders_served(self):
        self.cursor.execute(self.ORDER_SERVED)
        for row in self.cursor:
            print("{} : {} {}, {}".format(row[0], row[1], row[2], row[3]))

    def which_shipper(self):
        self.cursor.execute(self.WHICH_SHIPPER)
        for row in self.cursor:
            print("{} : {}".format(row[0], row[1]))






def main():
    db = DB()
    #db.all_employees()
    #db.city_employees("London")
    #db.employees_depart()
    #db.female_employees()
    #db.oldest_employess()
    #db.longest_serving()
    #db.who_is_theboss()
    #db.who_reports_to()
    #db.count_famale()
    #db.count_male()
    #db.different_city()
    #db.order_to_employee()
    #db.order_to_shipper()
    #db.countries_to_ship()
    #db.employees_with_most_orders()
    #db.customer()
    #db.orders_served()
    db.which_shipper()


if __name__ == '__main__':
    main()
