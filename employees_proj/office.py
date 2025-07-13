class Office:
    employees_num = 0  

    def __init__(self, name):
        self.name = name
        self.employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num = num

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employees_num += 1

    def fire(self, emp_id):
        new_employees = []
        for emp in self.employees:
            if emp.id != emp_id:
                new_employees.append(emp)
        if len(new_employees) < len(self.employees):
            Office.employees_num -= 1
        self.employees = new_employees
   
    def calculate_lateness(self, expected_time=9, arrival_time=None):
        if arrival_time > expected_time:
            return arrival_time - expected_time
        return 0
    
    def return_arrival(self,arrival_time):
        return arrival_time
    
    
    def deduct(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= amount

    def reward(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += amount
