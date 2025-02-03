try:
    1 / 0  # 这里会引发 ZeroDivisionError
except ZeroDivisionError as e:
    raise ValueError("数学计算失败")  # 这里又引发了新的异常

# 上面抛出来的e:__cause__ = None; __context__ = e; __suppress_context__ = False

# Traceback (most recent call last):
#   File "/home/chaowen/projects/py021/ex.py", line 2, in <module>
#     1 / 0  # 这里会引发 ZeroDivisionError
# ZeroDivisionError: division by zero
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "/home/chaowen/projects/py021/ex.py", line 4, in <module>
#     raise ValueError("数学计算失败")  # 这里又引发了新的异常
# ValueError: 数学计算失败

try:
    1 / 0  # 这里会引发 ZeroDivisionError
except ZeroDivisionError as e:
    raise ValueError("数学计算失败") from e  # 这里又引发了新的异常

# 上面抛出来的e:__cause__ = e; __context__ = e; __suppress_context__ = True

# Traceback (most recent call last):
#   File "/home/chaowen/projects/py021/ex.py", line 3, in <module>
#     1 / 0  # 这里会引发 ZeroDivisionError
# ZeroDivisionError: division by zero
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "/home/chaowen/projects/py021/ex.py", line 5, in <module>
#     raise ValueError("数学计算失败") from e  # 这里又引发了新的异常
# ValueError: 数学计算失败
