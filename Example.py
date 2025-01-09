 
# list1 = []
# list2 = []
# s = int(input("Wie viele Nummern brauchen Sie:"))
# for i in range(s):
#     x = int(input("Geben Sie die Nummer ein:"))
#     list1.append(x)

# for i in list1:
#     if i%3 == 0:
#         list2.append(i)
# print(list1)
# print(list2)


def pallindrom(a):
    if a[::-1] == a:
        print("Ja das ist ein Pallindrom")
    else:
        print("Nein das ist kein Pallindrom")
     

x = input("Geben Sie ein:")
pallindrom(x)