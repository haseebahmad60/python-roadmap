from student_manager import (
    add_student,
    list_students,
    search_student,
    remove_student,
    update_student
)

def get_student_details():
    """ gets student input and validates them"""
    while True:
        name=input("Enter name:").strip()
        if name=="":
            print("name cannot be empty")
            continue
        else:
            break
    while True:
        try:
            age=int(input("Enter age:"))
            if age<=0 or age>120:
                print("invalid age")
            else:
                break 
        except ValueError:
            print("enter integer only")
    while True:
        department=input("Enter department:").strip()
        if department=="":
            print("department cannot be empty")
            continue
        else:
            break
    return name,age,department
    
def display_student(student):
    """displays sytudents information """
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Department: {student['department']}")
    print("-" * 20) 

def display_students(students):
    if students:
        for student in students:
            display_student(student)
    else:
        print("no students found")

while True:
    print("\nSTUDENT MANAGEMENTS SYstem")
    print("1.Add Student")
    print("2.List Students")
    print("3.Search Student")
    print("4.Remove Student")
    print("5.Update Student")
    print("6.Exit")

    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("enter integer only")
        continue

    if choice==1:
        name,age,department=get_student_details()
        add_student(name,age,department)
        
    elif choice==2:
        all_students=list_students()
        print("\nAll Students:")
        for student in all_students:
            display_student(student)
    elif choice==3:
        name=input("Enter name to search:").strip()
        search_result=search_student(name)
        if search_result:
            display_student(search_result)
        else:
            print("Student not found")
    elif choice==4:
        name=input("Enter name to remove:").strip()
        remove_student(name)
    elif choice==5:
        old_name=input("Enter name to update:").strip()
        new_name,age,department=get_student_details()
        update_student(old_name,new_name,age,department)
    elif choice==6:
        break
    else:           
        print("Invalid choice")