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

# sort list with 2 methods

# in-place
list = [3, 2, 4, 42, 1, -345]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

# specify compare function
list = [Person(name = "wc"), Person(name = "john"), Person(name = "merry")]
print(list)
list.sort(key = lambda x: x.get_name())
print(list)

#
# # return a copy
# sl = sorted(list)
# print(sl)
# print(type(sl))
#
# print(dir(Person))
#
# person_list = [Person()]
# print(person_list)
# import inspect
#
# # init = in
# # spect.getsource(getattr(Person, "__str__"))
# init = getattr(Person, "__str__")
# print(init)
