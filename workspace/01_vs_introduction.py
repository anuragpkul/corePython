def hello():
    print('hello world')
# hello()

def main():
    message()


import platform
def message():
   print('This is python version {}'.format(platform.python_version()))

if __name__ == "__main__":
    main()
    
