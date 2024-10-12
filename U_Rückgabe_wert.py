def steuer(x):
    if x > 2500:
        steuer = 0.22*x
        x -= steuer
        return x
        
    else:
        steuer = 0.18*x
        x -= steuer
        return x

Gehalt = int(input("Bitte Geben Sie ihre Gehaltsumme"))

print("Ihr Nettoeinkommen ist",steuer(Gehalt))