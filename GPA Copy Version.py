#Programmer: Mitchell DeCesare
#Program: Multiphase Project
#Date: 2/17/21
#Version: 1.0

SENTINEL = '00000000'
    

MAX_CREDIT = 5
MIN_CREDIT = 1

MAX_GRADE = 4.0
MIN_GRADE = 0.0

COURSE_ID = 0
COURSE_HOUR = 1
COURSE_NUM = 2
COURSE_LETTER = 3

def main():

    std_count = 0 

    total_grade = 0.0

    current_semester = input('Enter the current semester: ')

    student_banner_id = input('Enter your banner ID (type in 00000000 to stop): ')

 

    while student_banner_id != SENTINEL:
        student_last_name = input('Enter your last name: ')
        student_first_name = input('Enter your first name: ')

        num_course = int(input('Enter the amount of classes you are taking this semester: '))

        courses = [] 

        for count in range(num_course):
            s_course = [0, 0, 0, 0]
            s_course[COURSE_ID] = input('Enter your course ID: ')
            s_course[COURSE_HOUR] = get_credit_hour()
            s_course[COURSE_NUM] = get_number_grade()
            s_course[COURSE_LETTER] = get_letter_grade(s_course[COURSE_NUM])
            courses.append(s_course)

        gpa = final_gpa(courses)

        std_count += 1 #Updates student counter

        total_grade += gpa #Updades gpa 
        
        display_report_header(current_semester, student_banner_id, student_last_name, student_first_name)
        for s_course in courses:
            display_course_info(s_course[COURSE_ID], s_course[COURSE_HOUR], s_course[COURSE_LETTER])

        display_report_footer(gpa)    

        student_banner_id = input('Enter your banner ID (type in 00000000 to stop): ')

    display_report_totals(std_count, total_grade)


def get_credit_hour():
    credit = int(input('Enter credit hours for course: '))
    good_data = MIN_CREDIT <= credit <= MAX_CREDIT
    while not good_data: #This is only executed if bad data is entered
        print('Information is out of range')
        credit = int(input('Enter credit hours for course: '))
        good_data = MIN_CREDIT <= credit <= MAX_CREDIT    
    return credit

def get_number_grade():
    num = float(input('Enter your number grade from course: '))
    good_data = MIN_GRADE <= num <= MAX_GRADE
    while not good_data:
        print('Information is out of range')
        num = float(input('Enter your number grade from course: '))
        good_data = MIN_GRADE <= num <= MAX_GRADE    
    return num    

def get_letter_grade(num_grade): #Parameters are used to pass data in a function 
    if num_grade == 4.0:
        return 'A'
            
    elif num_grade >= 3.0:
        return 'B'
            
    elif num_grade >= 2.0:
        return 'C'
            
    elif num_grade >= 1.0:
        return 'D'
            
    else:
        return 'F'
def final_gpa(courses):       
    grade_point = 0.0 
    credit_hours = 0
    for s_course in courses:
        grade_point += s_course[COURSE_HOUR] * s_course[COURSE_NUM] 
        credit_hours += s_course[COURSE_HOUR] 

    return (grade_point)/(credit_hours)            

def display_report_header(current_semester, student_banner_id, student_last_name, student_first_name):
    print()
    print()
    print(' '* 13,'Gateway Community College')
    print(' '* 20,'Grade Report')
    print(' '* 20, current_semester)

    print('=============================================')
    print('Student Banner ID:' ,student_banner_id)
    print('Student Name: ' ,student_last_name, student_first_name)
    print('=============================================')

    print(format('', '4') ,format('Course ID', '10') ,format('Credit Hours', '13') ,format('Letter Grade', '10'))
    

    

def display_course_info(course, credit_hours_1, letter_grade_1):        
     
    print(format('', '4') ,format(course, '10') ,format(credit_hours_1, '7') ,format('', '11') ,format(letter_grade_1))

def display_report_footer(gpa):
    print('=============================================')
    print('GPA:', format(gpa, '.1f'))
    print('=============================================')
    print()
    print()  

def display_report_totals(std_count, total_grade):
    if std_count != 0:
        print()
        print('Total number of students', std_count)
        print('Average GPA', format(total_grade/std_count, '.1f'))
main()
