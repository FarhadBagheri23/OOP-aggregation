
class Person:
    def __init__(self, name:str , lname:str, role:str):
        self.name = name
        self.lname = lname
        self.__role = None
        self.role = role
    
    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, value):
        if value.lower() == "proffesor" or value.lower() == "student":
            self.__role = value.lower()
        else:
            raise ValueError("Invalid Role !")

    def __repr__(self):
        return str({
            'Name': self.name,
            'Lastname': self.lname,
            'Role' : self.__role
        })
