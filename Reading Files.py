

employees_file = open("employees.txt", "r")
for employee in employees_file.readlines():
    print(employee)
employees_file.close()
