class University:
    def __init__(self, name: str):
        self.__name = name
        self.__courses = []

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return str(self.__name)
    
    def add_course(self, University_course):
        self.__courses.append(University_course)

    @property
    def courses(self):
        return self.__courses
    
