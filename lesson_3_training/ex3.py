from student import Student
from coursegroup import CourseGroup

student = Student("Аркадий", "Росс", 22, "Инженер по тестированию")
classmates1 = Student("Роберт", "Шляйхер", 25, "Инженер по тестированию")
classmates2 = Student("Иван", "Иванов", 24, "Инженер по тестированию")
classmates3 = Student("Фёдор", "Лапкин", 27, "Инженер по тестированию")

course_group = CourseGroup(student, [classmates1, classmates2, classmates3])

print(course_group)
