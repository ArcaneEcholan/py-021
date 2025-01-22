class MyCtxManager:
    def __enter__(self):
        print("enter context")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)

with MyCtxManager():
    print("hello")
    raise NameError("nameerror")

print("after math")