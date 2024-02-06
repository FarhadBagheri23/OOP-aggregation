
class Course:
    def __init__(self, name, proffesor, course_number):
        self.name = name
        self.__proffesor = None
        self.proffesor = proffesor
        self.course_number = course_number
        self.students = []
        

    def __repr__(self):
        return str({
            'Course: ':self.name,
            'Proffesor': self.proffesor.name + self.proffesor.lname,
            'Course Number' : self.course_number
        })
    
    @property
    def proffesor(self):
        return self.__proffesor
    
    @proffesor.setter
    def proffesor(self, value):
        if value.role == "proffesor":
            self.__proffesor = value
            return self.proffesor
        else:
            raise ValueError("The selected person is not a proffesor!")
        
    def add_student(self, person):
        if person.role == "student":
            self.students.append(person)
        else:
            raise ValueError("Invalid person!")
        

