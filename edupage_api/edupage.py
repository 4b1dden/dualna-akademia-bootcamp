from edupage_api import Edupage, BadCredentialsException, LoginDataParsingException, EduStudent

edupage = Edupage("smnd", "KristianCabala", "TP3P8ZTHLW")

try:
    edupage.login()
    # Note: This list doesn't have to be sorted!
    
    students = edupage.get_students()
    print(students)

    students.sort(key = EduStudent.__sort__)

    for student in students:
        print(f"{student.number_in_class}: {student.fullname}")
except BadCredentialsException:
    print("Wrong username or password!")
except LoginDataParsingException:
    print("Try again or open an issue!")