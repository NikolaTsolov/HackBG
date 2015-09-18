from manage_company import ManageCompany

class CompantUI:
    def __init__(self):
        self.db = ManageCompany()

    def start(self):
        while True:
            var_input = input("comand>")
            try:
                if ' ' not in var_input:
                    function = "self.{}()".format(var_input)
                    eval(function)
                else:
                    inputs = var_input.split(' ')
                    function = "self.{}({})".format(inputs[0], inputs[1])
                    eval(function)
            except:
                print("Wrong comand!")

    def list_employees(self):
        for item in self.db.list_employees():
            print(item)

    def monthly_spending(self):
        print("The company is spending {} every mounth!".format(sum(self.db.get_selary())))

    def yearly_spending(self):
        yearly_spending = 12 * sum(self.db.get_selary())
        yearly_spending += sum(self.db.get_yearly_bonus())
        print("The company is spending {} every year!".format(yearly_spending))

    def _enter_name(self):
        while True:
            var_input = input("name>")
            if len(var_input) < 1 or ' ' not in var_input:
                print("Write First and Sir name!")
            else:
                return var_input

    def _enter_monthly_selary(self):
        while True:
            var_input = input("monthly_selary>")
            try:
                selary = int(var_input)
                if selary < 0:
                    print("Wrong input!")
                else:
                    return var_input
            except:
                print("Wrong input!")

    def _enter_yearly_bonus(self):
        while True:
            var_input = input("yearly_bonus>")
            try:
                bonus = int(var_input)
                if bonus < 0:
                    print("Wrong input!")
                else:
                    return var_input
            except:
                print("Wrong input!")

    def _enter_position(self):
        while True:
            var_input = input("position>")
            if len(var_input) < 1:
                print("Wrong Input!")
            else:
                return var_input

    def add_employee(self):
        employee = []
        employee.append(self._enter_name())
        employee.append(self._enter_monthly_selary())
        employee.append(self._enter_yearly_bonus())
        employee.append(self._enter_position())
        self.db.add_employee(employee)

    def delete_employee(self, _id):
        self.db.delete_employee(_id)

    def update_employee(self, _id):
        employee = []
        employee.append(self._enter_name())
        employee.append(self._enter_monthly_selary())
        employee.append(self._enter_yearly_bonus())
        employee.append(self._enter_position())
        self.db.update_employee(employee, _id)


def main():
    company = CompantUI()
    company.start()

if __name__ == '__main__':
    main()
