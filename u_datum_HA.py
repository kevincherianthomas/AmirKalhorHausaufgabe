
b = [11,4,6,9]

x = int(input("Tag des Datums eingeben:"))
if x < 1 or x > 31:
    print("Ungültiges Datum")
else:
    print(x)
    y = int(input("Monat des Datums eingeben:"))
    if y < 1 or y > 12:
        print("Ungültiges Datum")       
    else:
        print(y)
        z = int(input("Jahr des Datums eingeben:"))
        print(z)  
        if z%4 == 0:
            print("Schaltjahr!")
            if y == 2:
                print("Letzter Tag:29")  
                print("Gültiges Datum")
            else:
                if y in b:    
                    print("Letzter Tag:30 ")
                    print("Gültiges Datum")
                else:
                    print("Letzter Tag:31")
                    print("Gültiges Datum")
        else:
            if y == 2:
                print("Letzter Tag:28")
                print("Gültiges Datum")
            else:
                if y in b:    
                    print("Letzter Tag:30 ")
                    print("Gültiges Datum")
                else:
                    print("Letzter Tag:31")
                    print("Gültiges Datum")
















