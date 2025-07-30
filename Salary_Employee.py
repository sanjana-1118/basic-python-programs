Name=input("Enter your name:")
Salary=eval(input("Enter your Salary:"))
Hra=eval(input("Enter the Hra amount:"))
DA=eval(input("Enter the DA amount:"))
PF=eval(input("Enter the PF amount"))
IT=eval(input("Enter the IT amount:"))
Gross=Salary+Hra+DA
Net=PF-IT
print("Name of the Employee is:")
print("Gross Amount is",Gross)
print("Net Amount is",Net)

