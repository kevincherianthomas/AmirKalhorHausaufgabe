

def Parabel_min(a,b,c):
    x = (-b)/(2*a)
    y = a*(-b/2*a)**2 + b*(-b/2*a) + c 
    return x, y 


constant_a = int(input("Geben Sie a:"))
constant_b = int(input("Geben Sie b:"))
constant_c = int(input("Geben Sie c:"))

print(Parabel_min(constant_a,constant_b,constant_c))