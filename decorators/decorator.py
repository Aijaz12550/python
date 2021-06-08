def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def splitting_text(func):
    def wrapper():
        return func().split()
    return wrapper