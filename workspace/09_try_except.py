   #two kind
   #Error - syntax errors
   #Exception - ZeroDivisionError
def divide(x, y):
    try:
        result = x // y
        print("The result is ",result)
    except ZeroDivisionError:
        print('call 1-800')
    

if __name__ == "__main__":
    divide(3,0)