class Person:
    def __init__(self,name):
        self.user = name

    def deleteUser(self, new_user):
        self.user = new_user


p = Person("aijaz")
ps = [Person("aijaz")]

print("person = ",p, "persons = ",ps)