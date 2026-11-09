import math

def peri(a=0,b=0,c=0):
    perimetrs = a + b + c
    return perimetrs    
def lauk(a=0,b=0,c=0):
    pp = peri(a,b,c)/2
    laukums = math.sqrt(pp*(pp-a)*(pp-b)*(pp-c))
    return laukums
def istriss(a=0,b=0,c=0):
    if c<(b+a) and b<(c+a) and a<(b+c):
        return True
    else: return False

def trek(a, b, c):
    if a.isnumeric:
        if istriss(a,b,c):
        # Šeit darbības, ja ir Jā
            print(f"{a}, {b}, {c}")
            print(f"Perimetrs={peri(a,b,c):.2f}")
            print(f"Laukums={lauk(a,b,c):.2f}")
        else:
        # Šeit darbības, ja ir Nē    
            print("Trissturi nevar izveidot")    


print("Mana pirma programma")

tri1 = [3, 6, 5]  # i=0 - mala a, i=1 - mala b, i=2 - mala c

trek(tri1[0],tri1[1],tri1[2])

# otrs trissturis
tri2 = [4, 6, 5]  # i=0 - mala a, i=1 - mala b, i=2 - mala c
trek(tri2[0],tri2[1],tri2[2])

tri1[0] = 7

trek(tri1[0],tri1[1],tri1[2])

tri1[1] = "Diena"

trek(tri1[0],tri1[1],tri1[2])

