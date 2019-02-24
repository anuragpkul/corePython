class Something : 
    def run(self):# what is self ,is there this keyword in python ? what is 'this' ? what is 'this' vs 'self'?
        print("run")

    def walk(self):
        print("walk")

#Inheritance
class myClass(Something):
    def method1(self):
        print("myclass method 1")
        
    def method2(self, someargs):
        print(super().run()) #Calling superclass
        print("myclass method 2 :"+someargs)

class anotherClass(myClass):
    def method3(self):
        print("another Class method3")

    def method4(self):
        myClass.method1(self)
        print("another Class method4")

def main():
    cat = Something()
    cat.run()
    cat.walk()

    cls1 = myClass()
    cls1.method1()
    cls1.method2("Python is fun")

    cls2 = anotherClass()
    cls2.method4()
    

if __name__ == "__main__":
    main()




 


