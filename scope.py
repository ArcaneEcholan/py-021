
# ========================= change global var =========================
num = 1
print(f"before func: {num}")
def func():
    global num
    num = num + 1
func()
print(f"after func: {num}")

# ========================= trying to use global var without declaring =========================
num = 1
print(f"before func: {num}")
def func():
    try:
        num = num + 1
    except BaseException as e:
        print(e) # local variable 'num' referenced before assignment
func()
print(f"after func: {num}")

# ========================= change scoped var =========================
def func():
    the_var = 1
    print(f"before inner: {the_var}")
    def inner():
        nonlocal the_var   # nonlocal关键字声明, support multiple nested structure
        the_var = 100
        print(the_var)
    inner()
    print(f"after inner: {the_var}")
func()

# ========================= trying to use scoped var without declaring =========================
def func():
    the_var = 1
    print(f"before inner: {the_var}")
    def inner():
        try:
            the_var = the_var + 100
        except BaseException as e:
            print(e)  # local variable 'the_var' referenced before assignment
    inner()
    print(f"after inner: {the_var}")
func()