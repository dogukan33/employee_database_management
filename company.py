import sqlite3

import time


class Employee():

    def __init__(self,name,department,profession,salary):
        self.name = name
        self.department = department
        self.profession = profession
        self.salary = salary
    
    def __str__(self):
        return "Name: {}\nDepartment:{}\nProfession: {}\nSalary:{}\n".format(self.name,self.department,self.profession,self.salary)

class Company():
    def __init__(self):
        self.get_connection()
    
    def get_connection(self):

        self.con = sqlite3.connect("company.db")
        self.cursor = self.con.cursor()

        table_execute = "CREATE TABLE IF NOT EXISTS company (name TEXT,department TEXT,profession TEXT,salary INT)"
        self.cursor.execute(table_execute)

        self.con.commit()

    def cut_connection(self):
        self.con.close()

    def view_data(self):

        exec = "SELECT * from company"
        
        self.cursor.execute(exec)
        employees = self.cursor.fetchall()
        if len(employees) == 0:
            print("There is no data...")
        else:
            for emp in employees:
                print(emp)

    def view_employee(self,name):
        exec = "SELECT * from company where name = ?"
        self.cursor.execute(exec,(name,))
        employee = self.cursor.fetchall()
        if len(employee) == 0:
            print("There is no employee named %s..."%(name))
        else:
            for emp in employee:
                print('\n')
                emp = Employee(emp[0],emp[1],emp[2],emp[3])
                print(emp)

    def view_department(self,department):
        exec = "SELECT * from company where department = ?"
        self.cursor.execute(exec,(department,))
        employees = self.cursor.fetchall()
        if len(employees) == 0:
            print("There is no employee in %s department..."%(department))
        else:
            for emp in employees:
                print(emp)

    def add_employee(self,employee):

        exec = "INSERT into company values(?,?,?,?)"
        self.cursor.execute(exec,(employee.name,employee.department,employee.profession,employee.salary))

        self.con.commit()

    def delete_employee(self,name):

        exec = "DELETE from company where name = ?"
        self.cursor.execute(exec,(name,))
        
        self.con.commit()

    def increase_salary(self,name,amount): 

        exec = "SELECT * from company where name = ?"
        self.cursor.execute(exec,(name,))

        employee = self.cursor.fetchall()
        if len(employee) == 0:
            print("There is no one named %s..."%(name))
        else:
            salary = employee[0][3]
            salary += amount

            exec = "UPDATE company set salary = ? where name = ?"
            self.cursor.execute(exec,(salary,name))

            self.con.commit()
        

    def change_department(self,name,new_department):

        exec = "SELECT * from company where name = ?"
        self.cursor.execute(exec,(name,))

        employee = self.cursor.fetchall()
        if len(employee) == 0:
            print("There is no one named %s..."%(name))
        else:
            exec = "UPDATE company set department = ? where name = ?"
            self.cursor.execute(exec,(new_department,name))

            self.con.commit()



    


