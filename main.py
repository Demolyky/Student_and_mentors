# Класс студент
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finish_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Выставление оценок за лекции
    def rate_hw(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached\
           and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Вывод информации о студенте
    def __str__(self):
        view_name = f'Имя: {self.name}'
        view_surname = f'Фамилия: {self.surname}'
        view_rating = f'Средняя оценка за домашние задания: {average_rating(self)}'
        view_cources_in_progress = f'Курсы в процессе изучения: {", ".join(self.courses_in_progress) if self.courses_in_progress else "отсутствуют"}'
        view__finish_courses = f'Завершенные курсы: {", ".join(self.finish_courses) if self.finish_courses else "отсутствуют"}'
        return f'{view_name}\n{view_surname}\n{view_rating}\n{view_cources_in_progress}\n{view__finish_courses}'

    # Операторы сравнения
    def __eq__(self, student):
        return average_rating(self) == average_rating(student)

    def __lt__(self, student):
        return average_rating(self) < average_rating(student)

    def __gt__(self, student):
        return average_rating(self) > average_rating(student)


# Класс Ментор
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # Метод выставления оценок студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached\
           and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Класс лектор (наследован от лектора)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Функция вывода информации о классе
    def __str__(self):
        self.view_name = 'Имя: ' + self.name
        self.view_surname = 'Фамилия: ' + self.surname
        view_rate = f'Средняя оценка за лекции: {average_rating(self)}'
        return f'{self.view_name}\n{self.view_surname}\n{view_rate}'

    # Операторы сравнения
    def __eq__(self, lecturer):
        return average_rating(self) == average_rating(lecturer)

    def __lt__(self, lecturer):
        return average_rating(self) < average_rating(lecturer)

    def __gt__(self, lecturer):
        return average_rating(self) > average_rating(lecturer)


# Класс лектор (наследован от лектора)
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Функция сравнения оценок по курсам у перечня классов,
# универсальная для всех классов
def comparison_course(all_people, course):
    all_rating, number_people = 0, 0
    for people in all_people:
        if course in people.grades.keys():
            all_rating += average_rating(people, course)
            number_people += 1
    return f'По курсу {course} средняя оценка: {all_rating/number_people}'


# Функция сравнения оценок между учениками или преподавателями,
# универсальная для всех классов
def average_rating(Class, course=''):
    course = list(Class.grades.keys()) if course == '' else course
    sum_rating, values = 0, 0
    for class_courses in Class.grades.keys():
        if class_courses in course:
            sum_rating += sum(Class.grades[class_courses])
            values += len(Class.grades[class_courses])
    if Class.grades:
        return round(sum_rating/values, 1)
    else:
        return 0


# Заполнение Базы примеров
def main():
    student_Evgeniya = Student('Evgeniya', 'Daranovski', 'woman')
    student_Evgeniya.courses_in_progress += ['Python', 'Git']
    student_Mikhail = Student('Mikhail', 'Volf', 'man')
    student_Mikhail.courses_in_progress += ['Python', 'Git']
    student_Vasilii = Student('Vasilii', 'Pupkin', 'man')
    student_Vasilii.courses_in_progress += ['Git']

    lector_Grigori = Lecturer('Grigoriy', 'Sandrikov')
    lector_Grigori.courses_attached += ['Python']
    lector_Natali = Lecturer('Natali', 'Bayer')
    lector_Natali.courses_attached += ['Git']

    reviewer_Serj = Reviewer('Serj', 'Garden')
    reviewer_Serj.courses_attached += ['Git']

    student_Evgeniya.rate_hw(lector_Grigori, 'Python', 9)
    student_Evgeniya.rate_hw(lector_Natali, 'Git', 9)
    student_Mikhail.rate_hw(lector_Grigori, 'Python', 10)
    student_Mikhail.rate_hw(lector_Natali, 'Git', 7)
    student_Vasilii.rate_hw(lector_Natali, 'Git', 10)
    lector_Grigori.rate_hw(student_Evgeniya, 'Python', 9)
    lector_Grigori.rate_hw(student_Evgeniya, 'Python', 8)
    lector_Grigori.rate_hw(student_Mikhail, 'Python', 10)
    lector_Grigori.rate_hw(student_Mikhail, 'Python', 10)
    lector_Natali.rate_hw(student_Mikhail, 'Git', 8)
    lector_Natali.rate_hw(student_Evgeniya, 'Git', 9)
    lector_Natali.rate_hw(student_Vasilii, 'Git', 10)
    reviewer_Serj.rate_hw(student_Mikhail, 'Git', 4)
    reviewer_Serj.rate_hw(student_Evgeniya, 'Git', 10)

    all_student = [student_Mikhail, student_Evgeniya]
    all_mentors = [lector_Grigori, lector_Natali]

    print(student_Mikhail < student_Evgeniya)
    print(average_rating(student_Evgeniya, 'Python'))
    print(average_rating(student_Mikhail, 'Python'))
    print(comparison_course(all_student, 'Git') + ' за ДЗ')
    print(comparison_course(all_mentors, 'Git') + ' за лекции')
    print(lector_Grigori > lector_Natali)
    print(student_Evgeniya < student_Mikhail)

    
main()
