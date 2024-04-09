class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def pozdrav(self):
        print(f'Ahoj já jsem: {self.name}')
        print(f'A jsem {self.gender}')

student_pavel = Student('Pavel', 'Muž')
print(student_pavel.pozdrav())