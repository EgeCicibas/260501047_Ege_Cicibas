#Ege Cicibaş
#260501047
#Bilgisayar Mühendisliği

ogrenci_adi = "Ege Cicibaş"
ogrenci_no = "260501047"
ogrenci_bolumu = "Bilgisayar Mühendisliği"

print(ogrenci_adi , ogrenci_no , ogrenci_bolumu)

isim = "Ege Cicibaş"
yas = "18"
print(f"{isim} , {yas}") #f-string ile yazdırma (Ege Cicibaş , 18 sonucu gelir)

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
print(kelime.swapcase()) #büyük harfleri küçültür, küçük harfleri büyültür
print(kelime.casefold()) #büyük harfleri küçültür, küçük harfleri büyültür (swapcasein aynısı)
print()  #satır atlar (birşey yazılmadan gönderilir)

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
print(sayi1 % sayi2) #mod alma işlemi
print(sayi1 ** sayi2) #üs alma işlemi
print(sayi1 // sayi2) #tam sayı bölme işlemi
print(abs(sayi1)) #sayi1'in mutlak değerini alır (pozitif olduğu için düz yazdı ama eksili sayı olsaydı artılı şeklinde yazacaktı)
print(round(sayi2)) #sayi2'yi yuvarlar ==> 3.2 olduğu için 3 yazar
print(round(sayi2, 2)) #sayi2'yi 2 basamak yuvarlar ==> 3.2 olduğu için 3.20 yazar

#integer , float , round ve string ifadeleri
herhangi_sayi = 12.33
print(int(herhangi_sayi)) #12 yazılır çünkü int ondalık kısmı almaz
print(float(herhangi_sayi)) #12.33 yazılır çünkü float ondalık kısmı alır
print(round(herhangi_sayi)) #12 yazılır çünkü round ondalık kısmı yuvarlar (eğer 12.5ve daha büyük olsaydı 13 yazacaktı)
print(str(herhangi_sayi)) #12.33 yazılır çünkü str ondalık kısmı alır ve string olarak yazar
herhangi_sayi = str(herhangi_sayi) #herhangi_sayi artık string oldu
print(type(herhangi_sayi)) #herhangi_sayi'nin tipini gösterir ==> string olur
#herhangi_sayi artık string olduğu için herhangi_sayi + 1 yazarsak hata verir çünkü string ile integer toplanamaz
