class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for i in range(len(self.sales)):
            sales_index = self.sales[i]
            for j in range(len(sales_index)):
                total = total + sales_index[j]
            return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        total = 0
        for i in range(len(self.sales)):
            sales_index = self.sales[i]
            for j in range(len(sales_index)):
                total = total + sales_index[j]
        if total >= quota:
            return True
        return False

    def compare_to(self, other):
        total = 0
        for i in range(len(self.sales)):
            sales_index = self.sales[i]
            for j in range(len(sales_index)):
                total = total + sales_index[j]
        if total < other:
            return -1
        elif total > other:
            return 1
        else:
            return 0

    def __str__(self):
        total = 0
        for i in range(len(self.sales)):
            sales_index = self.sales[i]
            for j in range(len(sales_index)):
                total = total + sales_index[j]
        employee = str(self.employee_id) + '-' + self.name + ': ' + str(total)
        return employee
class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for i in range(len(self.sales)):
            sales_index = self.sales[i]
            for j in range(len(sales_index)):
                total = total + sales_index[j]
            return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        total = 0
        for i in range(len(self.sales)):
            sales_index = self.sales[i]
            for j in range(len(sales_index)):
                total = total + sales_index[j]
        if total >= quota:
            return True
        return False

    def compare_to(self, other):
        total = 0
        for i in range(len(self.sales)):
            sales_index = self.sales[i]
            for j in range(len(sales_index)):
                total = total + sales_index[j]
        if total < other:
            return -1
        elif total > other:
            return 1
        else:
            return 0

    def __str__(self):
        total = 0
        for i in range(len(self.sales)):
            sales_index = self.sales[i]
            for j in range(len(sales_index)):
                total = total + sales_index[j]
        employee = str(self.employee_id) + '-' + self.name + ': ' + str(total)
        return employee
