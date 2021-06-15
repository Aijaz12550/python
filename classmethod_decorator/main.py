import json

class hello_class:
    def __init__(self,name):
        self.name = name
        
    @classmethod
    def hello_world(cls, name):
        return cls(name)


result = hello_class.hello_world("llll")

print("result",result.name)