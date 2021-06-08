
from decorator import * 

@splitting_text
@uppercase_decorator
def say_hi():
    return 'hello there'

result = say_hi()

print("result ===>", result)