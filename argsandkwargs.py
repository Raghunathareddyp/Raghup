''' import base64
word = 'Hello raghu Hello how are you'
wordencode = base64.b64decode(word.encode('utf-8',errors='strict'))
#abc = word.encode('ASCII',errors='strict')
abc = word.encode('base64', errors='strict')
print(abc)
word = abc.decode('base64',errors='strict')
print(word)
base64. '''

def myfun(*args): 
    for arg in args:
        print(arg)

myfun(10,'abc',20,60)

array_names = {'firstname':'Raghunathareddy', 'secondname':'Peddahothuru'}


def fun2(**kwargs):
    for key, value in kwargs.items():
        print('key is {0} and value is {1}'.format(key,value))

fun2(firstname='Raghunathareddy', secondname='Peddahothuru')