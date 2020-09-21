n=6382
print("Ultima cifra a numarului n este", n%10)
print("Penultima cifra a numarului n este", (n%100)//10)
print("Catul impartirii numarului n la 9 este", n//9)
print("Restul impartirii numarului n la 9 este", n%9)
print("Suma cifrelor numarului n este", (n//1000)+((n%1000)//100)+((n%100)//10)+(n%10))
print("Rasturnatul numarului n este ", n%10, (n%100)//10, (n%1000)//100, n//1000, sep='')