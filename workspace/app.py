#Packages and accessibility of the functions

def main():
    print('confidential info')
    print_hello()
    second_print_hello()

def print_hello():
    print('Hello from app')

def second_print_hello():
    print('Test second')

# The global variable __name__  in the app module is compred with __main_ which is entry point,
#  so python execution
# First comes to line 12 and verifies 
# What is significance of __name__ == "__main__" ?

if __name__ == "__main__": #To avoid calling each and every function when imported and protect accidental invocation  of funtion
    main()