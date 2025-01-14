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

# in-place
d = {'b': 3, 'a': 2, 'c': 1}

# sort by key

print(type(d.items()))  # <class 'dict_items'>
sorted_items = sorted(d.items(), key=lambda x: x[0])
print(type(sorted_items))  # <class 'list'>
print(type(sorted_items[0]))  # <class 'tuple'>
print(dict(sorted_items))  # convert list of tuples to dict

# sort by value

sorted_items = sorted(d.items(), key=lambda x: x[1])
print(dict(sorted_items))  # convert list of tuples to dict
