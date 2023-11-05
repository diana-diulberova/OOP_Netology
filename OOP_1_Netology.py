class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _rate_lecturer(self, lecturer, course, rates_lecturer):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.rates_lecturer:
                lecturer.rates_lecturer[course] += [rates_lecturer]
            else:
                lecturer.rates_lecturer[course] = [rates_lecturer]
        else:
            return 'Ошибка'

    def get_middle_grade(self):
        sum_grades = 0
        len_grades = 0
        for grades in self.grades.values():
            for grade in grades:
                sum_grades += grade
                len_grades += 1
        if len_grades == 0:
            result_grades = 'Нет оценок'
        else:
            result_grades = round(sum_grades/len_grades, 1)
        return result_grades

    def __str__(self):

        result_grades = self.get_middle_grade()

        name_str = f'Имя: {self.name}\n'
        surname_str = f'Фамилия: {self.surname}\n'
        grades_str = f'Средняя оценка за домашние задания: {result_grades}\n'
        courses_in_progress_str = f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
        finished_courses_str = f'Завершенные курсы: {",".join(self.finished_courses)}'
        return name_str+surname_str+grades_str+courses_in_progress_str+finished_courses_str

    def __eq__(self, other):
        result_grades = self.get_middle_grade()
        other_grades = other.get_middle_grade()
        return result_grades == other_grades

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.rates_lecturer = {}

    def get_middle_rate(self):
        sum_rate = 0
        len_rate = 0
        for rates in self.rates_lecturer.values():
            for rate in rates:
                len_rate += 1
                sum_rate += rate

        if len(self.rates_lecturer) == 0:
            middle_rate = 'У лектора нет оценок'
        else:
            middle_rate = sum_rate/len_rate
        return round(middle_rate, 1)

    def __str__(self):

        middle_rate = self.get_middle_rate()

        name_str = f'Имя: {self.name}\n'
        surname_str = f'Фамилия: {self.surname}\n'
        average = f'Средняя оценка за лекции:{middle_rate}'
        return name_str+surname_str+average

    def __eq__(self, other):
        result_middle_rate = self.get_middle_rate()
        other_middle_rate = other.get_middle_rate()
        return result_middle_rate == other_middle_rate

class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)

    def _rate_hw(self, student, course, grade):
        if isinstance(student, Student)  and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name_str = f'Имя: {self.name}\n'
        surname_str = f'Фамилия: {self.surname}'
        return name_str+surname_str

def average_grade_students(students, course):
    middle_grade = 0
    count_students = 0
    for student in students:
        if course in student.courses_in_progress:
            middle_grade += Student.get_middle_grade(student)
            count_students +=1

        if count_students == 0:
            result = 'На этом курсе у студентов нет оценок'
        else:
            result = round(middle_grade/count_students, 1)

    return result

def average_grade_lecturers(lecturers, course):
    middle_grade = 0
    count_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            middle_grade += Lecturer.get_middle_rate(lecturer)
            count_lecturers +=1

        if count_lecturers == 0:
            result = 'На этом курсе у лекторов нет оценок'
        else:
            result = round(middle_grade/count_lecturers, 1)

    return result

student_1 = Student('Ivan', 'Ivanov', 'male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Java']

student_2 = Student('Svetlana','Sidorova','female')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Java']

lecturer_1 = Lecturer('Petr','Semenov')
lecturer_1.courses_attached += ['Python']
student_1._rate_lecturer(lecturer_1,'Python',9)
student_1._rate_lecturer(lecturer_1,'Python',7)
student_1._rate_lecturer(lecturer_1,'Python',10)

lecturer_2 = Lecturer('Alla','Vasina')
lecturer_2.courses_attached += ['Python']
student_2._rate_lecturer(lecturer_2,'Python',5)
student_2._rate_lecturer(lecturer_2,'Python',7)
student_2._rate_lecturer(lecturer_2,'Python',6)

reviewer_1 = Reviewer('Nina', 'Petrova')
reviewer_1._rate_hw(student_1, 'Python', 10)
reviewer_1._rate_hw(student_1, 'Python', 9)
reviewer_1._rate_hw(student_1, 'Python', 7)

reviewer_2 = Reviewer('Semen','Kozlov')
reviewer_2._rate_hw(student_2, 'Python', 6)
reviewer_2._rate_hw(student_2, 'Python', 7)
reviewer_2._rate_hw(student_2, 'Python', 9)

students = []
students += [student_1]
students += [student_2]

lecturers = []
lecturers += [lecturer_1]
lecturers += [lecturer_2]


print('Средняя оценка студентов на курсе Python: ', average_grade_students(students,'Python'))
print('Средняя оценка лекторов на курсе Python: ', average_grade_lecturers(lecturers,'Python'))

print()
print("Студенты:")
print()
print(student_1)
print()
print(student_2)
print()
print()
print("Лекторы:")
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print()
print("Эксперты:")
print()
print(reviewer_1)
print()
print(reviewer_2)
print()

print(student_2==student_1)
print(lecturer_1==lecturer_2)
