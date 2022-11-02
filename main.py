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

    def __str__(self):
        self.view_name = 'Имя: ' + self.name
        self.view_surname = 'Фамилия: ' + self.surname
        self.rate = 'Средняя оценка за лекции: ' + str(round(sum(self.grades)/len(self.grades), 1))
        return f'{self.view_name}\n{self.view_surname}\n{self.rate}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Mikhail', 'Volf', 'men')
best_student.courses_in_progress += ['Python']

cool_mentor = Lecturer('Ivan', 'Petrov')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 3)
cool_mentor.rate_hw(best_student, 'Python', 8)

best_student.rate_hw(cool_mentor, 'Python', 10)
best_student.rate_hw(cool_mentor, 'Python', 6)
best_student.rate_hw(cool_mentor, 'Python', 9)

print(best_student.grades)
print(f'Средняя оценка за лекции: {cool_mentor.grades}')
print(cool_mentor)