basic_pay=float(input("Enter the basic pay of the employee: "))
hra=0.1*basic_pay
da=0.05*basic_pay
total_salary=hra+da+basic_pay
print(f"Basic Pay:{basic_pay}")
print(f"HRA:{hra}")
print(f"DA:{da}")
print(f"Total Salary:{total_salary}")
