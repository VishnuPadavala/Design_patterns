from student import student
def main():
    student1=student.get_instance()
    student2=student.get_instance()
    print(student1.college," ",student1.address)


if __name__=="__main__":
    main()