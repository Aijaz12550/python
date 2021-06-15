import logging

logging.basicConfig(level=logging.INFO)

def func(*args, **kwargs):
    logging.info("args",args, "===",kwargs)



func(1,2,3,4,5, name="aijaz")
    