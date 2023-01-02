class Student:
    pass
class Worker:
    pass
class Teacher:
    pass
class Factory:
    def get_person(self,type):
        if type=='w':
            return Worker()
        elif type=='t':
            return Teacher()
        else:
            return Student()