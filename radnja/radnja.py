cena = 0
proizvodi = {
    "jakna" : 1500,
    "lopta" : 3000,
    "hleb" : 80,
    "telefon" : 150000,
    "tabla" : 850,
    "laptop" : 300000}
n = int(input("koliko ste proizvoda kupili? "))
for i in range(n):
    unos = (input("koji ste proizvod kupili "))
    cena = cena + proizvodi[unos]
if(n >= 10 and n <= 20):
    cena = cena * 0.9
if(n > 20):
    cena = cena * 0.8
print("vas racun je ",cena)
