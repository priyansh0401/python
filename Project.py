import pickle





# global variables


STUDENT_DATA_FILE_NAME = "students.dat"
TEACHER_DATA_FILE_NAME = "teachers.dat"

is_master_mode = False

hidden_teacher_properties = ["sal", "phone"]
hidden_student_properties = ["dob", "phone"]













# Student helper functions

def create_student():
    id = int(input("Enter Student ID : "))
    name = input("Enter student Name : ")
    dob = input("Enter student's date of birth : ")
    phone = input("Enter Mobile Number : ")
    student = {}
    student["id"] = id
    student["name"] = name
    student["dob"] = dob
    student["phone"] = phone
    fs = open(STUDENT_DATA_FILE_NAME, "ab+")
    pickle.dump(student, fs)
    fs.close()


def display_student(id):
    student = get_student(id)
    if student:
        display_details(student, True)
    else:
        print("No record found")


def display_students():
    students_list = get_students()
    for student in students_list:
        display_details(student, True)


def get_student(id):
    students_list = get_students()
    for student in students_list:
        if int(id) == int(student["id"]):
            return student

    return None


def get_students():
    students_list = []

    try:
        f = open(STUDENT_DATA_FILE_NAME, "rb+")
        while True:
            students_list.append(pickle.load(f))
        f.close()
    except EOFError:
        pass
    except Exception as ex:
        print(ex)
    return students_list


def edit_student_handler():
    while True:
        print("Select from the following")
        print("[N]. Edit Name")
        print("[D]. Edit DOB")
        print("[P]. Edit Phone")
        print("[X]. Go back")

        choice = input("Enter your choice: ")

        if choice.lower() == "n":
            edit_student_name()

        elif choice.lower() == "d":
            edit_student_dob()

        elif choice.lower() == "p":
            edit_student_phone()

        elif choice.lower() == "x":
            break
        else:
            print("Please enter a valid choice")


def edit_student_name():
    student_id = input("Enter the ID of the student you want to edit: ")
    student = get_student(student_id)
    if student:
        new_name = input("Enter the new name: ")
        student["name"] = new_name
        update_student(student)
        print("Student name updated successfully!")
    else:
        print("No student record found with the given ID.")


def edit_student_dob():
    student_id = input("Enter the ID of the student you want to edit: ")
    student = get_student(student_id)
    if student:
        new_dob = input("Enter the new date of birth: ")
        student["dob"] = new_dob
        update_student(student)
        print("Student date of birth updated successfully!")
    else:
        print("No student record found with the given ID.")


def edit_student_phone():
    student_id = input("Enter the ID of the student you want to edit: ")
    student = get_student(student_id)
    if student:
        new_phone = input("Enter the new phone number: ")
        student["phone"] = new_phone
        update_student(student)
        print("Student phone number updated successfully!")
    else:
        print("No student record found with the given ID.")


def update_student(student):
    students_list = get_students()
    found = False

    for i in range(len(students_list)):
        if students_list[i]["id"] == student["id"]:
            students_list[i] = student
            found = True
            break

    if found:
        try:
            with open(STUDENT_DATA_FILE_NAME, "wb") as f:
                for s in students_list:
                    pickle.dump(s, f)
            print("Student record updated successfully!")
        except Exception as ex:
            print("An error occurred while updating student record:", str(ex))
    else:
        print("No student record found with the given ID.")














# Teacher helper functions


def create_teacher():
    id = int(input("Enter teacher ID : "))
    name = input("Enter teacher Name : ")
    sub = input("Subject Expertise : ")
    sal = input("Enter teacher's salary : ")
    phone = input("Enter Mobile Number : ")
    teacher = {}
    teacher["id"] = id
    teacher["name"] = name
    teacher["sub"] = sub
    teacher["sal"] = sal
    teacher["phone"] = phone
    fs = open(TEACHER_DATA_FILE_NAME, "ab+")
    pickle.dump(teacher, fs)
    fs.close()


def display_teachers():
    teachers_list = get_teachers()
    for teacher in teachers_list:
        display_details(teacher, False)


def display_teacher(id):
    teacher = get_teacher(id)
    if teacher:
        display_details(teacher, False)
    else:
        print("No record found")


def get_teacher(id):
    teachers_list = get_teachers()
    for teacher in teachers_list:
        if int(id) == int(teacher["id"]):
            return teacher
    return None


def get_teachers():
    teachers_list = []

    try:
        f = open(TEACHER_DATA_FILE_NAME, "rb+")
        while True:
            teachers_list.append(pickle.load(f))
        f.close()
    except EOFError:
        pass
    except Exception as ex:
        print(ex)

    return teachers_list


def edit_teacher_handler():
    while True:
        print("Select from the following:")
        print("[N]. Edit Name")
        print("[S]. Edit Subject")
        print("[SS]. Edit Salary")
        print("[P]. Phone")
        print("[X]. Go back")

        choice = input("Enter your choice: ")

        if choice.lower() == "n":
            edit_teacher_name()

        elif choice.lower() == "s":
            edit_teacher_subject()

        elif choice.lower() == "ss":
            edit_teacher_salary()

        elif choice.lower() == "p":
            edit_teacher_phone()

        elif choice.lower() == "x":
            break
        else:
            print("Please enter a valid choice")


def edit_teacher_name():
    teacher_id = input("Enter the ID of the teacher you want to edit: ")
    teacher = get_teacher(teacher_id)
    if teacher:
        new_name = input("Enter the new name: ")
        teacher["name"] = new_name
        update_teacher(teacher)
        print("Teacher name updated successfully!")
    else:
        print("No teacher record found with the given ID.")


def edit_teacher_subject():
    teacher_id = input("Enter the ID of the teacher you want to edit: ")
    teacher = get_teacher(teacher_id)
    if teacher:
        new_subject = input("Enter the new subject expertise: ")
        teacher["sub"] = new_subject
        update_teacher(teacher)
        print("Teacher subject expertise updated successfully!")
    else:
        print("No teacher record found with the given ID.")


def edit_teacher_salary():
    teacher_id = input("Enter the ID of the teacher you want to edit: ")
    teacher = get_teacher(teacher_id)
    if teacher:
        new_salary = input("Enter the new salary: ")
        teacher["sal"] = new_salary
        update_teacher(teacher)
        print("Teacher salary updated successfully!")
    else:
        print("No teacher record found with the given ID.")


def edit_teacher_phone():
    teacher_id = input("Enter the ID of the teacher you want to edit: ")
    teacher = get_teacher(teacher_id)
    if teacher:
        new_phone = input("Enter the new phone number: ")
        teacher["phone"] = new_phone
        update_teacher(teacher)
        print("Teacher phone number updated successfully!")
    else:
        print("No teacher record found with the given ID.")


def update_teacher(teacher):
    teachers_list = get_teachers()
    found = False

    for i in range(len(teachers_list)):
        if teachers_list[i]["id"] == teacher["id"]:
            teachers_list[i] = teacher
            found = True
            break

    if found:
        try:
            with open(TEACHER_DATA_FILE_NAME, "wb") as f:
                for t in teachers_list:
                    pickle.dump(t, f)
            print("Teacher record updated successfully!")
        except Exception as ex:
            print("An error occurred while updating teacher record:", str(ex))
    else:
        print("No teacher record found with the given ID.")













# Utility Functions
def display_details(obj, is_student):
    for key, value in obj.items():
        if not is_master_mode:
            if is_student:
                if key in hidden_student_properties:
                    continue
            else:
                if key in hidden_teacher_properties:
                    continue
        print(str(key).title(), str(value).title(), sep="=", end=" | ")
    print()







# Master Control


def master_control():
    global is_master_mode
    is_master_mode = True

    print("WELCOME TO THE MASTER ACCESS")

    menu_handler()


def public_control():
    global is_master_mode
    is_master_mode = False

    print("WELCOME TO THE PUBLIC ACCESS")

    menu_handler()


def menu_handler():
    while True:
        print("Select from the following")
        print("[T]. Teacher")
        print("[S]. Student")
        print("[X]. Go back")

        choice = input("Enter your choice: ")
        if choice.lower() == "t":
            teacher_menu_handler()

        elif choice.lower() == "s":
            student_menu_handler()

        elif choice.lower() == "x":
            break
        else:
            print("Please enter a valid choice")


def student_menu_handler():
    while True:
        print("Select from the following")

        if is_master_mode:
            print("[A] Add new student")
        if is_master_mode:
            print("[E] Edit existing student")
        print("[D] Dispaly student records")
        print("[DA] Dispaly all students records")
        print("[X] Go back")

        choice = input("Enter your choice: ")
        if choice.lower() == "a":
            create_student()
        elif choice.lower() == "e":
            edit_student_handler()
        elif choice.lower() == "d":
            i = input("Student ID : ")
            display_student(i)
        elif choice.lower() == "da":
            display_students()
        elif choice.lower() == "x":
            break
        else:
            print("Please eneter a valid choice")


def teacher_menu_handler():
    while True:
        print("Select from the following")

        if is_master_mode:
            print("[A] Add new teacher")
        if is_master_mode:
            print("[E] Edit existing teacher")

        print("[D] Dispaly teacher records")
        print("[DA] Dispaly all teacher records")
        print("[X] Go back")
        choice = input("Enter your choice : ")

        if choice.lower() == "a":
            create_teacher()
        elif choice.lower() == "e":
            edit_teacher_handler()
        elif choice.lower() == "d":
            i = input("Teacher ID : ")
            display_teacher(i)
        elif choice.lower() == "da":
            display_teachers()
        elif choice.lower() == "x":
            break
        else:
            print("Please enter a valid choice")









# Driver function
def main():
    print("Program execution started")
    
    master_id = "5328"
    master_pass = "administrator"
    public_id = "public"
    public_pass = "public"
    
    id = input("Enter id:")
    password = input("Enter pass:")


    if id == master_id and password == master_pass:
        master_control()
    elif id == public_id and password == public_pass:
        public_control()
    else:
        print("Wrong ID or password:")

    print("Program execution ended")





# Start program
main()
