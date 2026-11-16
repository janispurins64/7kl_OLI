skaitlis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summa = 0
for i in skaitlis:
    summa = summa + i
print(summa)

sar2 = ["Otto","Maris","Juris","Vilis"]
summa = 0
for i in sar2:
    print(i)

skaitlis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summa = 0
indekss = 0
while indekss<10:
    summa = summa + skaitlis[indekss]
    indekss = indekss + 1
print(summa)

summa = 0
indekss = 0
while True:
    summa = summa + skaitlis[indekss]
    indekss = indekss + 1
    if indekss>9:
        break
print(summa)

while True:
    ke = input("Ievadi:")
    if ke[0] == 'Y' or ke[0] == 'y':
        break
    print(f"-->{ke}  {sorted(ke)}")

print(f"Tika ievadīts: {ke}")
