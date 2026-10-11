class CourseGroup:
    def __init__(self, student, classmates):
        self.student = student
        self.classmates = classmates

    def __str__(self):
        classmates_str = ", ".join(str(c) for c in self.classmates)
        return f"{self.student} учится вместе с: {classmates_str}"
