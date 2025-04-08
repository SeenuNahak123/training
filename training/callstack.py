def functionthree():
    print('third')

def functiontwo():
    functionthree()
    print('second')

def functionone():
    functiontwo()
    print('one')

functionone()




def deco(func):
    def wrapper():
        print('before hi')
        func()
        print('after hi')
        func()
    return wrapper

@deco
def hi():
    print('hello')

hi()