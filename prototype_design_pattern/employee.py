from prototype import prototype
def main():
    base_employee=prototype.getconfiguration()
    employee1=base_employee.getconfiguration()
    employee1.set_employeename("vishnu")
    employee1.set_employeeid(325)
    employee1.display()
    employee2=base_employee.getconfiguration()
    employee2.set_employeename("srija")
    employee2.set_employeeid(324)
    employee2.display()

if __name__=='__main__':
    main()