from models import create_student
from storage import load_students, save_students


def add_student(name, age, department):
    students = load_students()
    student_exists = search_student(name)
    if student_exists:
        print("Student already exists")
        return

    student = create_student(name, age, department)

    students.append(student)

    save_students(students)

def list_students():
    students=load_students()
    return students
    
def search_student(name:str)-> dict:
    students=load_students()
    name=name.lower()
    for student in students:
        if name==student["name"].lower():
            return student
    return None  
def remove_student(name):
    students=load_students()
    name=name.lower()
    for student in students:
        if name==student["name"].lower():
            students.remove(student)
            save_students(students)
            print("student removed")
            return
    else:
        print("student not found")


def update_student(old_name:str,new_name:str,age:int,department:str):
    students=load_students()
    old_name=old_name.lower()
    for student in students:
        if old_name==student["name"].lower():
            student["name"]=new_name
            student["age"]=age
            student["department"]=department
            save_students(students)
            print("student updated")
            return
    else:
        print("student not found")
    