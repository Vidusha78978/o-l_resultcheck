name = input("Enter your name :- ")
age = int(input("Enter your age :- "))

if age<18:
    exit("You have not permission")
else:
    subjects = ["sinhala","English","Tamil","Science","Maths","Health","Budhism"]
    marks = []
    result = []
    for x in subjects:
        mark = int(input("Enter your "+ x +" marks :- "))
        marks.append(mark)
    def resul(marks):
        if marks>=75:
            result.append("A")
        elif marks>=65:
            result.append("B")
        elif marks>=55:
            result.append("C")
        elif marks>=35:
            result.append("S")
        else:
            result.append("W")

    print("\n")
    print("\n")
    print("\t" + name + " your results are ")
    print("\n")
    print('\n')


    for i in subjects:
        o = 0
        resul(mark)
        print(i + " = " + result[o] + "\n")
        o = o+1
        
        

            

