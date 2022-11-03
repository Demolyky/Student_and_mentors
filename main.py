class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self. finish_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached\
           and course in self.courses_in_progress:
            mentor.grades.append(grade)

    def __str__(self):
        view_name = f'Имя: {self.name}'
        view_surname = f'Фамилия: {self.surname}'
        sum_raiting, values = 0, 0
        courses = []
        for course, rate in self.grades.items():
            courses.append(course)
            sum_raiting += sum(rate)
            values += len(rate)
        view_raiting = f'Средняя оценка за домашние задания: {round(sum_raiting/values, 1)}'
        view_cources_in_progress = f'Курсы в процессе изучения: {", ".join(courses)}'
        view__finish_courses = f'Завершенные курсы: {", ".join(self.finish_courses)}'
        return f'{view_name}\n{view_surname}\n{view_raiting}\n{view_cources_in_progress}\n{view__finish_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached\
           and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.average_rating = 0.0

    def __str__(self):
        self.view_name = 'Имя: ' + self.name
        self.view_surname = 'Фамилия: ' + self.surname
        view_rate = 'Средняя оценка за лекции: ' + str(round(sum(self.grades)/len(self.grades), 1))
        return f'{self.view_name}\n{self.view_surname}\n{view_rate}'

    def __eq__(self, lecturer):
        return self.comparison(lecturer, 'eq')

    def __lt__(self, lecturer):
        return self.comparison(lecturer, 'lt')

    def __gt__(self, lecturer):
        return self.comparison(lecturer, 'gt')

    def comparison(self, lecturer, command='eq'):
        self.average_rating = round(sum(self.grades)/len(self.grades), 1)
        lecturer.average_rating = round(sum(lecturer.grades)/len(lecturer.grades), 1)
        match command:
            case 'eq':
                return self.average_rating == lecturer.average_rating
            case 'lt':
                return self.average_rating < lecturer.average_rating
            case 'gt':
                return self.average_rating > lecturer.average_rating


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Mikhail', 'Volf', 'men')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finish_courses += ['English for developer']

cool_mentor = Lecturer('Ivan', 'Petrov')
cool_mentor.courses_attached += ['Python', 'Git']

cool_lecturer = Lecturer('Mikhail', 'Pavlov')
cool_lecturer.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Git', 6)
cool_mentor.rate_hw(best_student, 'Git', 5)

best_student.rate_hw(cool_mentor, 'Python', 10)
best_student.rate_hw(cool_mentor, 'Python', 7)
best_student.rate_hw(cool_mentor, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Python', 9)

print(best_student.grades)
print(f'Средняя оценка за лекции: {cool_mentor.grades}')
print(cool_mentor)
print(best_student)
print(cool_lecturer)
print(cool_mentor < cool_lecturer)
