def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Called function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 4)

# 2

def exception_handler_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in function {func.__name__}: {e}")
    return wrapper

@exception_handler_decorator
def divide(a, b):
    return a / b

divide(4, 0)
