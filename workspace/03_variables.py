# Variables 
x=10
print('The value of x is',x)
# String
a="10"
# Integer
b = int(a)
print('The value of b is',b,type(b))
k = None
print(type(k))

def add_number(a ,b):
    return a+b

y=add_number(2,3)
print(y)

# String is immutable sequence of characters

y = '"Yes",he said ,"I like python"'
print(y)

z="first" "second"

print(z)
# Usage of '''
a = ''' sdkjfhlkdh^%$^@%#^E%$!^#%@$#^% 
" dfhksjhdfkjsdhkjfhsd '''

print(a)

#Escape sequences
path = ' This is \n song from latest \n album '
print(path)

a = """ \ """

print (a)

s=4
r = '4'

print(s != r)

x = 10
print("string type "+str (x)) #casting

print("this is line 52 "+a)

#understanding global variable
def someFunction():
    global a 
    a = "100"  
    print("this is line 52 "+a)

someFunction()

print("this is line 52 "+a)

del a
print("this is line 61 "+a)


