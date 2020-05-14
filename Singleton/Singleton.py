# Como clase base
class Singleton(object):
    _instances = {}
    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]

class Logger(Singleton):
    @classmethod
    def logAction(cls, action : str):
        print(action)

# Como metaclase

class SingletonMetaClass(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMetaClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class LoggerMetaClass(metaclass=SingletonMetaClass):
    @classmethod
    def logAction(cls, action : str):
        print(action)

class noSingleton():
    pass

a = Logger().logAction("User entry")

b = Logger.logAction("User out")

c = Logger.logAction("Failed payment because of fraud")

x = LoggerMetaClass().logAction("User entry")

y = LoggerMetaClass().logAction("User out")

z = LoggerMetaClass().logAction("Failed payment because of fraud")

j = noSingleton()

k = noSingleton()

# Base Class
print("Base Class")
print(a==b)
print(c==b)
# Metaclass
print("Metaclass")
print(x==y)
print(z==y)
# No Singleton
print("No Singleton")
print(j==k)
