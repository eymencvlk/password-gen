# rastgele modülünü içeri aktardık.
import random
# Kullanıcının parolasının içerebileceği tüm karakterleri içeren bir değişken oluşturun
karakter_deposu = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# Bir değişken oluşturun ve kullanıcıdan parolanın uzunluğunu girmesini isteyin
uzunluk = int(input("Parolanın Uzunluğunu Giriniz: "))
# Programın oluşturulan parolayı saklayacağı bir değişken oluşturun
parola = ""
# Kullanıcnın belirlediği uzunluk kadar tekrar eden bir döngü oluşturun.
for i in range(uzunluk):
    # Karakter Depomuzdan rastgele bir tane karakter seçilecek.
    karakter = random.choice(karakter_deposu)
    #Seçilen rastgele karakteri parola adlı değişkene eklemem gerkiyor.
    parola += karakter
# Elde edilen parolayı konsola yazdırın
print(parola)
