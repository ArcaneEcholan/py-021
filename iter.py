class Person:
    def __init__(self, name="", age=0):
        self.__name = name
        self.__age = age

    def __repr__(self):
        return f"I'm {self.__name}, {self.__age} years old"


class Family:
    def __init__(self):
        self.__members = []

    def add(self, p):
        self.__members.append(p)

    def get_all_members(self):
        return self.__members

    def __repr__(self):
        return f"These are the memebers of the family: {self.__members}"

    def __iter__(self):
        return Fi(self)

class Fi:
    def __init__(self, f = None):
        self.__f = f
        self.__idx = -1
    def __next__(self):
        self.__idx += 1
        if self.__idx < len(self.__f.get_all_members()):
            return self.__f.get_all_members()[self.__idx]
        raise StopIteration

family = Family()
family.add(Person(name="john", age=12))
family.add(Person(name="bob", age=16))

print(family)

for member in family:
    print(member)
