#import time
#def memo(f):
#   def wrapper(x):
#       return f(x)
#   return wrapper
#def calculate(x):
#   time.sleep(5)
#   return x ** 4
#d={}
#print(calculate (4))
#print(calculate (4))
#print(calculate (4))

#---------->OUTPUT:
#$ python decorator-time-memo-wrapper-return-function.py
#256
#256
#256
#(venv) Mohammads-iMac:python-class mohammadtahir$

#--------------------
# using dictionary function, to check if x value is available in dictionary, if there, just return value, if not, create entry in dictionary and return d[x] value.


import time


# memoization
def memo(f):
    d = {}

    def wrapper(x):
        if x not in d:
            d[x] = f(x)
        return d[x]

    #        if x in d:
    #            return d[x]
    #        else:
    #            d[x] = f(x)
    #            return d[x]
    return wrapper


# def memo(f):
#    def wrapper(x):
#        return f(x)
#    return wrapper

@memo
def calculate(x):
    time.sleep(5)
    return x ** 4


# d = {}
s = time.time()
print(calculate(4))
# d = {4: 256}
print(calculate(4))
# d = {4: 256}
print(calculate(4))
# d = {4: 256}
print(calculate(5))
# d = {4: 256, 5:625}
print(calculate(5))
e = time.time()
print("Took:", e - s, "seconds")

# OUTPUT:
#$ python decorator-time-memo-wrapper-return-function.py
#256
#256
#256
#625
#625
#Took: 10.002835988998413 seconds
