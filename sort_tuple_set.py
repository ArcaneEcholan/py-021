class Person:
    def get_name(self):
        return self.__name

    def __init__(self, age=0, name=""):
        self.__age = age
        self.__name = name  # def __repr__(self):  #     return f"Person(name={self.__name}, age={self.__age})"  # def __str__(self):  #     return f"Person(name={self.__name}, age={self.__age})"

    def __repr__(self):
        return f"I'm {self.__name}, {self.__age} years old."

    def __str__(self):
        return f"Isssss'm {self.__name}, {self.__age} years old."

t = (3, 34, 1)

st = sorted(t)
print(type(st))  # sorted result type
print(type(st[0]))
print(st)  # sorted result value
print(tuple(st))  # convert back to tuple

t = (Person(name="merry"), Person(name="john"), Person(name="wc"),)
print(t)
t = sorted(t, key=lambda x: x.get_name(), reverse=True)  # sort by specific key
print(t)  # sorted result value
print(type(t))
print(tuple(t))  # convert back to tuple

s = {3, 1, 2}
sorted_set = sorted(s)
print(sorted_set)  # sorted result value
print(set(sorted_set))  # convert back to set

s = "python"
sorted_chars = sorted(s)  # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted_chars)  # sorted result value
print(''.join(sorted_chars))  # convert back to set
