first = input("Please enter the name of the first student: ")
second = input("Please enter the name of the second student: ")
third = input("Please enter the name of the third student: ")
fourth = input("Please enter the name of the fourth student: ")
fifth = input("Please enter the name of the fifth student: ")
sixth = input("Please enter the name of the sixth student: ")
seventh = input("Please enter the name of the seventh student: ")
eighth = input("Please enter the name of the eighth student: ")


print("1. {0}".format(first))
print("2. {0}".format(second))
print("3. {0}".format(third))
print("4. {0}".format(fourth))
print("5. {0}".format(fifth))
print("6. {0}".format(sixth))
print("7. {0}".format(seventh))
print("8. {0}".format(eighth))


select = int(input("Please select a student to edit: "))
new_name = input("Please enter their new name: ")

if select == 1:
    first = new_name
elif select == 2:
    second = new_name
elif select == 3:
    third = new_name
elif select == 4:
    fourth = new_name
elif select == 5:
    fifth = new_name
elif select == 6:
    sixth = new_name
elif select == 7:
    seventh = new_name
elif select == 8:
    eighth = new_name
else:
    print("Wrong input")

print("1. {0}".format(first))
print("2. {0}".format(second))
print("3. {0}".format(third))
print("4. {0}".format(fourth))
print("5. {0}".format(fifth))
print("6. {0}".format(sixth))
print("7. {0}".format(seventh))
print("8. {0}".format(eighth))
