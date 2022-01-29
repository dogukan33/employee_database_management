from company import *


print("""
********************
   Welcome.

1) View Data
2) Edit Data
3) Shut Down

********************
""")

company = Company()

while True:
   request= input("REQUEST: ")
   if request== '1':

      print("""
      ********************
         menu/view.

      1) View ALL
      2) View Employee
      3) View Department

      ********************
      """)

      while True:
         request = input("Type the option: ")
         if request == '1':
            company.view_data()
            break
      
         elif request == '2':
            name = input("Enter the name of employee: ")
            company.view_employee(name)
            break

         elif request == '3':
            department = input("Enter the department: ")
            company.view_department(department)
            break
   
   elif request == '2':

      print("""
      ********************
         menu/edit.

      1) Add Employee
      2) Delete Employee
      3) Increase Salary
      4) Change Department

      ********************
      """)
      while True:
         request = input("Type the option: ")

         if request == '1':

            name = input('Name:' )
            department = input('Department: ')
            profession = input('Profession: ')
            salary = input('Salary: ')

            new_employee = Employee(name,department,profession,salary)
            print("Confirming...")
            time.sleep(1)
            print("New employee registered.")
            company.add_employee(new_employee)
            break
         
         elif request == '2':
            
            name = input("Enter name of the employee: ")
            print("Deleting %s's data..."%(name))

            confirm = input("Type 1 to confirm,0 to cancel: ")
            if confirm == '1':
               company.delete_employee(name)
               print("Data has been deleted.")
            break

         elif request == '3':
            name = input('Enter the employee: ')        
            amount = int(input('Enter the amount of increase: '))

            company.increase_salary(name,amount)
            time.sleep(1)
            print("Salary updated.")

            break
         
         elif request == '4':
            name = input('Enter the employee: ') 
            nd = input("Enter new department: ")

            company.change_department(name,nd)
            print("Employee's department has been updated.")
            break
                     
   elif request == '3':
         break









