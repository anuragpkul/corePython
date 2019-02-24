def main():
    x = 0
    #while loop
    while (x < 11):
        print(x)
        x+=1

    #For loop
    for x in range(1,11): #excludes last value
        print(x)
        if(x == 6):break
        
    
    students = ["Sue","Kathy","sekar","Bryan"]
    for s in students:
        print(s)

    #Using enumeration
    for i,s in enumerate(students):
        print(i,s)

if __name__ == "__main__":
    main()