import random 


list1 = []


def polynom_ableitung():
    print("f´(x) = ", end="")
    for i in range(0,len(list1)):
        if i==0:
            print(f"{list1[i]*0} + ",end="")
        else:
            print(f"{list1[i]*i}*x^{i-1} + ",end="")
        i =+ 1






x = int(input("Welches Gerade soll ihre Python haben?"))
print("Ihre random generierte Python ist:")

for i in range(x+1): 
    random_number = random.randint(-100,100)
    list1.append(random_number)

print("f(x) = ", end="")
for i in range(len(list1)):
    print(f"{list1[i]}*x^{i} + ",end="")
    i =+ 1


print("")
print("Die Ableitung ist:")
polynom_ableitung()
