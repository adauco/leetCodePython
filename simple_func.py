
# @some_decorator
def simple_func(name = "jose"):
    print("Simple func executed")

    def greet():
        return '\t greet func inside hello'

    def welcome():
        return '\t inside welcome'

    print("print a function")

    if name == "jose":
        return greet()
    else:
        return welcome()


hola = simple_func()
print(hola)
hola = simple_func("Juan")
print(hola)



def other(some_def_func):
    def wrapit():
        print("other codigo")
        some_def_func()
    return wrapit

@other
def hello():
    print("hola juan")

hello()
