def function1():
    print("I am learning functions")

function1()
print(function1())
print(function1) #Gives location of the function 

#Functions taking arguments
def function2(arg1,arg2):
    print(arg1," ",arg2)

function2(10,20)
print(function2(10,20))

def function3(x):
    return x*x

print(function3(12))



#Varargs function takes n arguments
def function4(*args): 
    result  =0 
    for x in args:
        result = result + x
    return result

print(function4(1,2,3,4,5))

