import random

list1 = []

class Parabell:
    def Schnittpunkt(self,a,b,c):
        schnittpunkt_1 = (-b+((b**2-4*a*c)**1/2))/(2*a)
        schnittpunkt_2 = (-b-((b**2-4*a*c)**1/2))/(2*a)
        print("Die Schnittpunkte sind",schnittpunkt_1,schnittpunkt_2)
        
    def Scheitelpunkt(self,a,b,c):
        x = 0 
        d = (b**2)-(4*a*c)
        scheitelpunkt = [-b/2*a , -d/4*a]
        print("The Scheitelpunkte sind:", scheitelpunkt)


class polynom_ableitung:
    def polynom_ableitung(self): 
        print("f´(x) = ", end="")
        for i in range(0,len(list1)):
            if i==0:
                print(f"{list1[i]*0} + ",end="")
            else:
                print(f"{list1[i]*i}*x^{i-1} + ",end="")
            i =+ 1



class gerade:
    def gerade_funktion(self):
        m = int(input("Was ist die Steigung?"))
        c = int(input("Was ist c ?"))
        print(f"die Gerade ist y = {m}x + {c}")
        ableitung_gerade = m
        schnittpunkt_gerade = [0,c] , [-c/m,0] 
        print("Die Schnittpunkte sind:",schnittpunkt_gerade ," Und die Ableitung der Gerade ist:","f´(y)",ableitung_gerade)


#Parabell
pb1 = Parabell()
constant_a = int(input("Geben Sie a:"))
constant_b = int(input("Geben Sie b:"))
constant_c = int(input("Geben Sie c:"))
pb1.Scheitelpunkt(constant_a,constant_b,constant_c)
pb1.Schnittpunkt(constant_a,constant_b,constant_c)


#Polynom
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


#gerade 
gp = gerade()
gp.gerade_funktion()



