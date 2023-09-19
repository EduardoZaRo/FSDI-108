def test1():
    students = []
    students.append("Glenda")
    students.append("Eduardo")
    students.append("Irvin")
    
    print(students)
    print(len(students))
    print(students[0])
    
    for student in students:
        print(student)
        
def test2():
    prices = [12,43,2,4,67,132,7,45,13,7,56,3,63,56,40,72]
    for price in prices:
        print(price)
    print("___________________________________")
    for price in prices:
        if price < 50:
            print(price)
# test1()
test2()