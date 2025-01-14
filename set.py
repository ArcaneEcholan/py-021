import traceback
import logging
import inspect
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")

the_set = set()
the_set.add(1)
the_set.add(56)
print(the_set)

try:
    the_set.remove(2)
except BaseException as e:
    t = traceback.format_exc()
    logging.error(f"{t}, the err: {e}")

# the_set.discard(2)

class CustomError(Exception):
    """Custom exception with an optional message."""
    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(self.message, "other message")

# Example usage
try:
    raise CustomError("Something went wrong!")
except CustomError as e:
    print(dir(e))
    print(f"Caught an exception: {repr(e)}")
    print(f"Caught an exception: {str(e)}")
    print(f"Caught an exception: {(e)}")
    # inspect.getsource(e.__str__)
    # inspect.getsource(e.__repr__)

class Person:
    # def __str__(self):
    #     return ("jfalsjd")
    def __repr__(self):
        return ("__repr__ version: jfalsjd")
print(f"hello :{Person()}")
print(f"hello :{Person()}")
