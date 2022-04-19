class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        file_list = file.readlines()
        self.sales_people.append(file_list)
        file.close()

    def quota_report(self, quota):
        for i in range(len(self.sales_people)):
            return self.sales_people[i]

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            for j in range(len(self.sales_people[i])):
                ind = self.sales_people[i]
                if ind[j] == employee_id
                    return self.sales_people[i]
                else:
                    return None
