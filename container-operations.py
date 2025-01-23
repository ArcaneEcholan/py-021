# * traverse
# * find
# * sort
# * insert, remove
# * slice
# str: split, join, substring, lower, upper

class Item:
    def __init__(self, name="", age=-1):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<name: {self.name}, age: {self.age}>"

    def __gt__(self, other):
        return self.name > other.name

    def __eq__(self, other):
        return self.name == other.name


item1 = Item("john", 23)
item2 = Item("wok", 31)
item3 = Item("merry", 10)
item4 = Item("xiaoming", 21)
item5 = Item("abc", 22)
item6 = Item("abc", 14)

itemm = Item("itemn", 88)
itemn = Item("itemn", 90)

"""
list
"""

list_of_items = [item1, item2, item3, item4, item5, item6]

# ========================= traverse =========================
for idx, item in enumerate(list_of_items):
    print(idx)
    print(item)

# ========================= find =========================
itemx = [x for x in list_of_items if x.name == "abc"]
if len(itemx) == 0:
    print("not found")
else:
    print(itemx[0])

itemx = list(filter(lambda x: x.name == "abc", list_of_items))
if len(itemx) == 0:
    print("not found")
else:
    print(itemx[0])

# ========================= sort =========================
sorted_list = sorted(list_of_items)  # need to overwrite __gt__ (>) or __lt__ (<)
print(sorted_list)

sorted_list = sorted(list_of_items, key=lambda x: x.name, reverse=True)
print(sorted_list)

sorted_list = sorted(list_of_items, key=lambda x: (x.name, x.age), reverse=True)
print(sorted_list)

# ========================= insert =========================
list_of_items.insert(1, itemm)
print(list_of_items)

list_of_items.insert(1, itemn)
print(list_of_items)

list_of_items.insert(-100, itemn)  # won't error, equal to 0
print(list_of_items)

list_of_items.insert(100, itemn)  # won't error, equal to last
print(list_of_items)

# ========================= remove =========================
list_of_items.remove(itemn)
list_of_items.remove(itemn)
list_of_items.remove(itemn)
list_of_items.remove(itemn)
# list_of_items.remove(itemn) # ValueError, if no more items in the list
print(list_of_items)

# list_of_items.pop(100) # IndexError
list_of_items.pop(0)
print(list_of_items)

copy_of_list = list_of_items.copy()
copy_of_list.clear()
print(copy_of_list)

# list_of_items.pop(-1) # IndexError
# list_of_items.pop(100) # IndexError

"""
dict
"""

dict_of_items = {1: item1, 2: item2, 3: item3, 4: item4, 5: item5}

# ========================= traverse =========================
for k, v in dict_of_items.items():
    print(k)
    print(v)

# ========================= find =========================
# by key
itemx = [x for x in dict_of_items.items() if x[0] == 2]
print(itemx)

# by value
itemx = [x for x in dict_of_items.items() if x[1].name == "abc"]
print(itemx)

# ========================= sort =========================
# by key
sorted_dict = dict(sorted(dict_of_items.items(), key=lambda x: x[0]))
print(sorted_dict)

# by value
sorted_dict = dict(sorted(dict_of_items.items(), key=lambda x: x[1]))
print(sorted_dict)

# ========================= insert =========================


# ========================= remove =========================
# dict_of_items.pop(23) # KeyError
dict_of_items.pop(2)
print(dict_of_items)

dict_of_items = dict([x for x in dict_of_items.items() if x[0] != 2])
print(dict_of_items)

copy_of_dict = dict_of_items.copy()
copy_of_dict.clear()
print(copy_of_dict)

"""
str
"""



string = "This is a string..."
decimal_string = "1231"
# ========================= traverse =========================
for idx, ch in enumerate(string):
    print(f"type: {type(ch)} ch: {ch}, is lower: {ch.islower()} lower: {ch.lower()}, upper: {ch.upper()}")

print(f"{decimal_string} is decimal: {decimal_string.isdecimal()}")
# ========================= find =========================

# find ch
chs = [ch for ch in string if ch.isalpha()]
print(chs)
chs = [ch for ch in string if ch.islower()]
print(chs)

# find substring
idx_of_sub = string.find("hello world")
print(idx_of_sub)
idx_of_sub = string.find("This")
print(idx_of_sub)
idx_of_sub = string.find(" ")
print(idx_of_sub)

upper_string = "".join(map(lambda ch: ch.upper(), string))
print(upper_string)
# ========================= sort =========================
sorted_string = "".join(sorted(string))
print(sorted_string)

# ========================= insert =========================
# does not natively support
def insert_string(original_string, position, insert_string):
    new_string = list(original_string)
    new_string.insert(position, insert_string)
    return ''.join(new_string)

string = "  Hello World  "
new_string = insert_string(string, 5, ", ")
print(new_string)

# ========================= remove =========================

# remove substring
pos = 1
string = string[:pos] + string[pos + 1:]
print(string)

# trim
string = string.rstrip()
print(string)
string = string.lstrip()
print(string)
string = string.strip()
print(string)


