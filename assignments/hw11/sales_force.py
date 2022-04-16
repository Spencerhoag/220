"""
hw11.py
"""


class SalesForce:
    """
    represents a team of sales people.
    """

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        in_file = open(file_name, "r")
        words = in_file.readlines()
        for line in words:
            self.sales_people.append(line)

    def quota_report(self, quota):
        mylist = []
        for i in self.sales_people:
            line_split = i.split(",")
            eid = line_split[0]
            name = line_split[1]
            sales = line_split[2]
            sales_split = sales.split(" ")
            total_sales = sum(sales_split)
            mylist.append([eid, name, total_sales])
        for j in mylist:
            if j[2] < quota:
                j.append(False)
            elif j[2] >= quota:
                j.append(True)
        return mylist

    def top_seller(self):
        mylist = []
        topsellers = []
        for i in self.sales_people:
            line_split = i.split(",")
            eid = line_split[0]
            name = line_split[1]
            sales = line_split[2]
            sales_split = sales.split(" ")
            total_sales = sum(sales_split)
            mylist.append([eid, name, total_sales])
        for j in mylist:
            sales_sorted = mylist.sort(key=j[2])
            top = sales_sorted[:-1]
            topsellers.append(top)
            if top[2] == j[2]:
                topsellers.append(j)

    def individual_sales(self, employee_id):
        mylist = []
        for i in self.sales_people:
            line_split = i.split(",")
            eid = line_split[0]
            name = line_split[1]
            sales = line_split[2]
            sales_split = sales.split(" ")
            total_sales = sum(sales_split)
            mylist.append([eid, name, total_sales])
        for j in mylist:
            if j[0] == employee_id:
                return j
            else:
                return None

    def get_sale_frequencies(self):
        pass
