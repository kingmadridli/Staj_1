import numpy as np


# Soru 1)   (10,15,30,45,60)  değerlerine sahip numpy dizisi oluştur.
numbers_1 = np.array([10,15,30,45,60])

# Soru 2)    5-15 sayıları arasında numpy dizisi oluştur.
numbers_1 = np.arange(5,15)

# Soru 3)  50-100 arasında 5' er artarak bir dizi oluştur
numbers_1 = np.arange(50,100,5)

# Soru 4)   4 elemanlı 0 lardan oluşan biri dizi oluştur.
numbers_1 = np.zeros(4)

# Soru 5)   10 elemanlı 1 lerden oluşan bir dizi oluştur.
numbers_1 = np.ones(10)

# Soru 6)   0-100 arasında eşit aralıklı 5 sayı üret
numbers_1 = np.linspace(0,100,5)

# Soru 7)   10-30 arasında rastgele 5 tane tam sayı üret
numbers_1 = np.random.randint(10,30,5)

# Soru 8)   -1 ile 1 arasında 10 adet sayı üret
numbers_1 = np.random.randn(10)

# Soru 9)   3x5 boyutlarında 10-50 arasında rastgele bir matris oluştur.
numbers_1 = np.random.randint(10,50,15)
result = numbers_1.reshape(3,5)


# Soru 10)  Üretilen matrisin satır ve sütün toplamlarını hesapla.
# row_total = result.sum(axis=1)
# col_total = result.sum(axis=0)
# print(row_total)
# print(col_total)

# Soru 11)   Üretilen matrisin en büyük, en küçük  ve ortalama değerleri ne
# print(result.max())
# print(result.min())
# print(result.mean())

# Soru 12)  Üretilen matrisin en büyük değerinin indeksi kaç
# print(result.argmax())


# Soru 13)   (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seç
numbers_1 = np.arange(10,20)
result = numbers_1[0:3]

# Soru 14)   Üretilen dizinin elemanlarını tersten yazdır
result = numbers_1[::-1]

# Soru 15)   Üretilen matrisin ilk satırını seç
numbers_1 = np.random.randint(-50,50,15)
result = numbers_1.reshape(3,5)
# print(result[0,:])

# Soru 16)    Üretilen matrisin 2.satır 3.sütünundaki elemanı nedir
# print(result[1,2])

# Soru 17)    Üretilen matrisin tüm satırlardaki ilk elemanını seç
# print(result[:,0])

# Soru 18)   Üretilen matrisin her bir elemanın karesini alınız
kare = result ** 2
# print(kare)

# Soru 19)   Üretilen matris elemanlarının hangisi pozitif hangisi çift sayıdır.

ciftler = result[result % 2 == 0]
sonuc = ciftler[ciftler>0]
print(sonuc)



print(30*"-")
# print(numbers_1)
print(result)