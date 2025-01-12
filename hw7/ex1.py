class Employee:
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        print(self.name, '\n', self.id, sep = '')

class Manager(Employee):
    department= None

    def __init__(self, name, id, department):
        super(Manager, self).__init__(name, id)
        self.department = department

    def manage_project(self):
        print(self.department)

    def get_info(self):
        super().get_info()
        print(self.department)

class Technician(Employee):
    specialization = None

    def __init__(self, name, id, specialization):
        super(Technician, self).__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        print(self.specialization)

    def get_info(self):
        super().get_info()
        print(self.specialization)

class TechManager(Manager, Technician):

    employee_list = ['f']

    def __init__(self, name, id, department, specialization):
        self.name = name
        self.id = id
        self.department = department
        self.specialization = specialization

    def get_info(self):
        print(self.specialization)



    def add_employee(self):
        self.employee_list = [self.name, self.id, self.department, self.specialization]
        print('Введите данные нового сотрудника')
        print('Введите имя')
        self.name = input()
        print('Введите идентификационный номер')
        self.department = input()
        print('Введите отдел')
        self.department = input()
        print('Введите специализацию')
        self.specialization = input()
        self.employee_list= [self.employee_list, '\n', self.name, self.id, self.department, self.specialization]

    def get_info(self):
        print(self.employee_list)

boy1 = Employee('Mike', '49621518')
boy1.get_info()

boy2 = Manager('Ron', '68455132', 'bakery')
boy2.get_info()

girl1 = Technician('Rose', '541651858', 'chef')
girl1.get_info()

girl2 = TechManager('Sally', '687888899', 'sales department', 'logistician')
girl2.get_info()
