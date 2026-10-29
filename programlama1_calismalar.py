#Ege Cicibaş
#260501047
#Bilgisayar Mühendisliği

ogrenci_adi = "Ege Cicibaş"
ogrenci_no = "260501047"
ogrenci_bolumu = "Bilgisayar Mühendisliği"

print(ogrenci_adi , ogrenci_no , ogrenci_bolumu)

isim = "Ege Cicibaş"
yas = "18"
print("{} {} yasindadir".format(isim , yas))

ornek = "29-10-2026"
print(len(ornek))       #kaç kelimeden oluştuğunu gösterir
print(ornek[:2])        #ilk 2 karakteri gösterir
print(ornek[2:5])       #3. ve 4. karakterleri gösterir
print(ornek[5:])        #5. karakterden sonraki tüm karakterleri gösterir
print(ornek[::3])       #3er 3er atlayarak gösterir
print(ornek[::-1])      #tüm metni ters çevirir
print(ornek [2])        #3. karakteri gösterir(mantıken 9'u göstermesi lazım ama pythonda ilk kelime 0 ile başlar)

kelime = "yarin_ders_yok"
print(kelime.upper())     #tüm harfleri büyür
print(kelime.lower())     #tüm harfleri küçültür
print(kelime.capitalize()) #ilk harfi büyültür
print(kelime.title())     #her kelimenin ilk harfini büyültür (Yarin_Ders_Yok yazar)
print()         #satır atlar (birşey yazılmadan gönderilir)

ornek_ad = "efe"
ornek_soyad = "cicibas"
print(f"{ornek_ad} {ornek_soyad}") #.format yerine kullanılır daha kısa hali

sayi1 = 12
sayi2 = 3.2
print(type(sayi1)) #sayi1'in nasıl olduğunu gösterir ==> integer'dir.
print(type(sayi2)) #sayi2'nin nasıl olduğnu gösterir ==> float'dır.
print("-" * 32) #32 tane çizgi çizer

#matematik işlemleri
sayi1 = 12
sayi2 = 3.2
print(sayi1 + sayi2) #toplama işlemi
print(sayi1 - sayi2) #çıkarma işlemi
print(sayi1 * sayi2) #çarpma işlemi
print(sayi1 / sayi2) #bölme işlemi
print(sayi1 % sayi2) #mod alma işlemi
print(sayi1 ** sayi2) #üs alma işlemi
print(sayi1 // sayi2) #tam sayı bölme işlemi
