class Parabell:
    a = []
    b = []
    c = []
    def Schnittpunkt(self,a,b,c):
        self.a = a 
        self.b = b 
        self.c = c 
        schnittpunkt_1 = (-b+((b**2-4*a*c)**1/2))/(2*a)
        schnittpunkt_2 = (-b-((b**2-4*a*c)**1/2))/(2*a)
        print("Die Schnittpunkte sind",schnittpunkt_1,schnittpunkt_2)
        
    def Scheitelpunkt(self,a,b,c):
        self.a = a 
        self.b = b 
        self.c = c 
        x = 0 
        d = (b**2)-(4*a*c)
        scheitelpunkt = [-b/2*a , -d/4*a]
        print("The Scheitelpunkte sind:", scheitelpunkt)

    
pb1 = Parabell()
constant_a = int(input("Geben Sie a:"))
constant_b = int(input("Geben Sie b:"))
constant_c = int(input("Geben Sie c:"))
pb1.a.append(constant_a)
pb1.b.append(constant_b)
pb1.c.append(constant_c)


pb1.Scheitelpunkt(constant_a,constant_b,constant_c)
pb1.Schnittpunkt(constant_a,constant_b,constant_c)
