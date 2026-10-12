import math

print("Mana pirma programma")
mala_a = 60
mala_b = 6
mala_c = 5
if mala_c<(mala_b+mala_a) and mala_b<(mala_c+mala_a) and mala_a<(mala_b+mala_c):
    # Šeit darbības, ja ir Jā
    perimetrs = mala_a + mala_b + mala_c
    print(f"{mala_a}, {mala_b}, {mala_c}")
    print(f"Perimetrs={perimetrs}")
    pp = perimetrs/2
    laukums = math.sqrt(pp*(pp-mala_a)*(pp-mala_b)*(pp-mala_c))
    print(f"Laukums={laukums:.2f}")
else:
    # Šeit darbības, ja ir Nē    
    print("Trissturi nevar izveidot")

a = 3
aa = a  * a
print(a, aa, math.sqrt(a))
gg = math.pi
print(f"Sis ir pi={gg}")