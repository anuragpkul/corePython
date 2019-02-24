#List - mutable sequence of objects
#Zero based index position
def main():
    students = ["Sue","Kathy","sekar","Bryan"]

    s1 = ["Sue","Kathy","sekar","Bryan"]

    #add items to list use append
    students.append("Steve")
    students.append(s1)
    print(students)
    print(students[0])

    del students[0]

    print(students[0])

#Immutable list: Tuple: Sequence of immutable python objects.Same as lists but they can not be changed.
    tup1 = ("Sue","Kathy","sekar","Bryan")
    tup3 = ("Ryan",)
    #Accessing values from Tuple
    print(tup1[0])

    #update tuples and list
    students[0] = "brown"

    tup4 = tup1 + tup3
    print(tup4)

if __name__ == "__main__":
    main()