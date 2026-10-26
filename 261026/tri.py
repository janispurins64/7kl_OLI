import math

def peri(a=0,b=0,c=0):
    perimetrs = a + b + c
    return perimetrs    
def lauk(a=0,b=0,c=0):
    pp = peri(a,b,c)/2
    laukums = math.sqrt(pp*(pp-a)*(pp-b)*(pp-c))
    return laukums    

print("Mana pirma programma")
mala_a = 3
mala_b = 6
mala_c = 5
if mala_c<(mala_b+mala_a) and mala_b<(mala_c+mala_a) and mala_a<(mala_b+mala_c):
    # Šeit darbības, ja ir Jā
    print(f"{mala_a}, {mala_b}, {mala_c}")
    print(f"Perimetrs={peri(mala_a,mala_b,mala_c):.2f}")
    print(f"Laukums={lauk(mala_a,mala_b,mala_c):.2f}")
else:
    # Šeit darbības, ja ir Nē    
    print("Trissturi nevar izveidot")

# otrs trissturis
mala_a = 4
mala_b = 6
mala_c = 5
if mala_c<(mala_b+mala_a) and mala_b<(mala_c+mala_a) and mala_a<(mala_b+mala_c):
    # Šeit darbības, ja ir Jā
    print(f"{mala_a}, {mala_b}, {mala_c}")
    print(f"Perimetrs={peri(mala_a,mala_b,mala_c):.2f}")
    print(f"Laukums={lauk(mala_a,mala_b,mala_c):.2f}")
else:
    # Šeit darbības, ja ir Nē    
    print("Trissturi nevar izveidot")

