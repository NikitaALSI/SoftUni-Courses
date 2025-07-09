employees = {}

while (cmd := input()) != "End":
    company, employee = cmd.split(" -> ")
    employees[company] = employees.get(company, [])
    if employee not in employees[company]:
        employees[company].append(employee)

for company in employees:
    print(f"{company}")
    for employee in employees[company]:
        print(f"-- {employee}")
