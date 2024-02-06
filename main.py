from course import Course
from university import University
from person import Person

farhad = Person("Farhad", "Bagheri", "Student")
kiarash = Person("Kiarash", "Firouzi", "Proffesor")
reza = Person("Reza", "Bazrafkan", "Student")
pouya = Person("Pouya", "Karbalaei", "Student")

Mathematics = Course("Mathematics", kiarash, 50012)
Differential_equation =  Course("Differential Equation", kiarash, 50036)
print(Mathematics)


Sharif = University("Sharif University of technology")
print(Sharif)
Sharif.add_course(Mathematics)
Sharif.add_course(Differential_equation)
print(Sharif.courses)

Mathematics.add_student(farhad)

Mathematics.add_student(reza)

Mathematics.add_student(pouya)

print(Mathematics.students)