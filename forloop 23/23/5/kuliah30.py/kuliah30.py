# no 2 3
def salam(nama):
  print(f'selamat datang {nama}')

salam("putri")

# no 4
def hitungLuas(panjang, lebar):
  luas = panjang*lebar
  return luas

print(hitungLuas(4,5))
print(hitungLuas(2,5))
print(hitungLuas(4,3))
print(hitungLuas(5,5))
print(hitungLuas(4,1))

# no 5
phi = 20
def hitungLuas(jari):
    phi= 3.14
    print('variable di dalam fungsi (lokal)',phi)
    luas = (jari**2)*phi
    return luas

luasLingkaran = hitungLuas(4)
print(luasLingkaran)
print('variable diluar fungsi (global)', phi)

def ganjilGenap(bilangan):
    if bilangan % 2==0 :
        return 'genap'
    else :
        return 'ganjil'

bilangan1 = ganjilGenap(9)
bilangan2 = ganjilGenap(4)
bilangan3 = ganjilGenap(5)
bilangan4 = ganjilGenap(7)
bilangan5 = ganjilGenap(8)

while True:
    masukan = input("masukan angka ")
    bilangan = ganjilGenap (int(masukan))
    print(bilangan)
