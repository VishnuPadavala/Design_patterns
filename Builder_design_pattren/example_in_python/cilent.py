
from studentbuilder import studentbuilder
from student import student
        
def main():
    student1=(studentbuilder().set_name("vishnu").set_rollno(10).set_phoneno("90909").build())
    student1.display()


if __name__=='__main__':
    main()