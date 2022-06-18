# no 1
def faktorial(n):
 print(f'menghitung faktorial {n}')
 if n == 1:
   print('nilai balik 1, iterasi berakhir')
   return 1
 else:
   hasil = faktorial(n-1)
   print(f'return {n} dikalikan dengan fungsi faktorial({n-1}) = {hasil}')
   return n * hasil
print(faktorial(10))


# # no 2
def fib (n):
 if n == 0:
    return 0
 elif n == 1:
    return 1
 else:
   hasil = fib(n-1) + fib(n-2)
   return hasil
 
print(fib(5))


# no 3
pohonAngka = [5, [10,8], [20, [255,40,45], [12, 23,34]]]
 
def tampilkanAngka(pohon):
 if isinstance(pohon, list) :
   for angka in pohon :
     tampilkanAngka(angka)
 else :
   print(f'angka {pohon}')
 
tampilkanAngka(pohonAngka)

# no 4
from math import inf as infinity
 
pohonAngka = [5, [10,8], [20, [255,40,45], [12, 23,34]]]
 
def angkaTerbesar(pohon, terbesar=-infinity):
 if isinstance(pohon, list) :
   terbesarInLoop = 0
   for angka in pohon :
     hasil = angkaTerbesar(angka, terbesar)
     if(hasil > terbesarInLoop) :
       terbesarInLoop = hasil
   return terbesarInLoop   
 else :
   if(pohon > terbesar) :
     return pohon
   else :
     return terbesar
 
print(angkaTerbesar(pohonAngka))
