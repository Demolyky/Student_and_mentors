class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finish_courses = []
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
        if values:
            view_raiting = f'Средняя оценка за домашние задания: {round(sum_raiting/values, 1) if values!=0 else "0"}'
        else:
            view_raiting = 'Оценки отсутствуют'
        view_cources_in_progress = f'Курсы в процессе изучения: {", ".join(self.courses_in_progress) if self.courses_in_progress else "отсутствуют"}'
        view__finish_courses = f'Завершенные курсы: {", ".join(self.finish_courses) if self.finish_courses else "отсутствуют"}'
        return f'{view_name}\n{view_surname}\n{view_raiting}\n{view_cources_in_progress}\n{view__finish_courses}'

    def __eq__(self, student):
        return self.__comparison(student, 'eq')

    def __lt__(self, student):
        return self.__comparison(student, 'lt')

    def __gt__(self, student):
        return self.__comparison(student, 'gt')

    def __comparison(self, student, command='eq'):
        for rate in self.grades.values():
            self.all_grades += rate
        self.average_rating = round(sum(self.all_grades)/len(self.all_grades), 1)
        for rate in student.grades.values():
            student.all_grades += rate
        student.average_rating = round(sum(student.all_grades)/len(student.all_grades), 1)
        match command:
            case 'eq':
                return self.average_rating == student.average_rating
            case 'lt':
                return self.average_rating < student.average_rating
            case 'gt':
                return self.average_rating > student.average_rating


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
        if self.grades:
            view_rate = f'Средняя оценка за лекции: {str(round(sum(self.grades)/len(self.grades), 1))}'
        else:
            view_rate = "Оценки отсутствуют"

        return f'{self.view_name}\n{self.view_surname}\n{view_rate}'

    def __eq__(self, lecturer):
        return self.__comparison(lecturer, 'eq')

    def __lt__(self, lecturer):
        return self.__comparison(lecturer, 'lt')

    def __gt__(self, lecturer):
        return self.__comparison(lecturer, 'gt')

    def __comparison(self, lecturer, command='eq'):
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


def main():
    student_Evgeniya = Student('Evgeniya', 'Daranovski', 'woman')
    student_Evgeniya.courses_in_progress += ['Python', 'Git']

    student_Mikhail = Student('Mikhail', 'Volf', 'man')
    student_Mikhail.courses_in_progress += ['Python']

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
    lector_Grigori.rate_hw(student_Evgeniya, 'Python', 9)
    lector_Grigori.rate_hw(student_Evgeniya, 'Python', 8)
    lector_Grigori.rate_hw(student_Mikhail, 'Python', 10)
    lector_Grigori.rate_hw(student_Mikhail, 'Python', 10)
    lector_Natali.rate_hw(student_Mikhail, 'Git', 8)
    lector_Natali.rate_hw(student_Evgeniya, 'Git', 9)
    reviewer_Serj.rate_hw(student_Mikhail, 'Git', 4)
    reviewer_Serj.rate_hw(student_Evgeniya, 'Git', 10)


    print(student_Evgeniya)
    print(student_Mikhail)
    print(lector_Grigori > lector_Natali)

main()
