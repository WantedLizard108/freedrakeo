class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        print('Сотрудник:', self.name, 'ID:', self.emp_id)

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self):
        print(self.name, 'управляет проектом в отделе', self.department)

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        print (self.name, 'выполняет техническое обслуживание в области', self.specialization)

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        return [employee.get_info() for employee in self.team]

employee = Employee("Alice", 101)
manager = Manager("Bob", 102, "Sales")
technician = Technician("Charlie", 103, "Electronics")
tech_manager = TechManager("Diana", 104, "IT", "Network Maintenance")

employee.get_info()
manager.get_info()
manager.manage_project()
technician.get_info()
technician.perform_maintenance()
tech_manager.get_info()
tech_manager.manage_project()
tech_manager.perform_maintenance()

tech_manager.add_employee(employee)
tech_manager.add_employee(technician)
tech_manager.get_team_info()
