class PayrollProcessor:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def process_payroll(self):
        payroll_data = []
        for employee in self.employees:
            net_salary = employee['salary'] - employee['deductions'] - employee['taxes'] + employee['benefits']
            payroll_data.append({'name': employee['name'], 'net_salary': net_salary})
        return payroll_data

    def generate_report(self):
        report = "Payroll Report:\n"
        for employee in self.employees:
            net_salary = employee['salary'] - employee['deductions'] - employee['taxes'] + employee['benefits']
            report += f"{employee['name']}: Net Salary = {net_salary}\n"
        return report
