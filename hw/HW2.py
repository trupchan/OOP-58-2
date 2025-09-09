
class ProgrammingCourse:
    def __init__(self, course_name, duration_months, level):
        self.course_name = course_name
        self.duration_months = duration_months
        self.level = level

    def description(self):
        return f"Курс: {self.course_name}, уровень: {self.level}, длительность: {self.duration_months} мес."

    def start_course(self):
        return f"Курс {self.course_name} начинается! удачи ;) "

class Course(ProgrammingCourse):
    def __init__(self, course_name, duration_months, level, mentor_name):
        super().__init__(course_name, duration_months, level)
        self.mentor_name = mentor_name

    def start_course(self):
        return f"Добро пожаловать на курсы в школе {self.course_name}! Ваш ментор: {self.mentor_name}."

    def description(self):
        return f"Курс: {self.course_name}, уровень: {self.level}, длительность: {self.duration_months} мес, ментор: {self.mentor_name}"

basic_course = ProgrammingCourse("Python", 12, "новичок")
print(basic_course.description())
print(basic_course.start_course())

geeks_course = Course("Geeks", 6, "средний", "Арзыбек Абдурахманов")
print(geeks_course.description())
print(geeks_course.start_course())