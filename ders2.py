name = input("isminizi giriniz: ")

if name == "Gizem":
    print("adaşız",name)

if name != "Gizem":
    print("adaş değiliz",name)

if name == "gizem" or "ilayda":
    print("adınız",name)

if not (name == "gizem" or "ilayda"):
    print("adınız",name)

cevap = int(input("Kursa katıldın mı 1/0 "))
sonuc = bool(cevap)

if sonuc:
    print("belge alabilirsiniz")

# yaş hesaplama
dogum_yili=int(input("Doğum yılınızı giriniz: "))
yas = 2025-dogum_yili

if yas>=18:
    print("ehliyet alabilirsiniz")
else:
    print("ehliyet alacak yaşta değilsiniz !")
    print(18-yas, "yıl sonra ehliyet alabilirsiniz")
    print(f" ehliyet almak için {18-yas} yıl beklemeniz gerekir.")
    print(f"ehliyet alamazsınız çünkü {yas} yaşındasınız")

# hız sınırı
yol = float(input("ne kadar yol gittiniz"))
zaman = float(input("ne kadar zamanda gittiniz"))
hiz=yol/zaman

if hiz >= 132:
    print(f"hız sınırını aştınız. Hızınız: {hiz}")
    print(f"hız sınırınız {hiz - 132} kadar aştınız. Hızınız:{hiz} ")
else:
    print(f"hız sınırını aşmadını. Hızınız {hiz}")
    print("hız kurallarına uyduğunuz için teşekkürler")

# birden fazla karşılaştırma
# yemek siparişi
yemek = input("yemek giriniz: ")
icecek = input("icecek bilgisi giriniz: ")

if yemek=="pizza":
    print("pizza geçerli yemek siparişi")
    if icecek == "kola" or icecek == "ayran":
        print("geçerli sipariş")
        print("afiyet olsun")
    else:
        print("içecek iade olacak")
else:
    print(f"{yemek} - {icecek} ikilisi doğru sipariş değil")

# belge kontrolü
puan = int(input("ortalamanızı giriniz: "))
'''
if puan<0:
    print("hatalı puan girişi yaptınız")
else:
    if puan < 70:
        print("Belge almaya puanınız yeterli değil")
    else:
        if puan < 85:
            print("teşekkür alabilirsiniz tebrikler")
        else:
            if puan <= 100:
                print("tebrikler ! takdir aldınız")
            else:
                print("lütfen geçerli bir puan giriniz")
'''
# else + if -> elif

if puan<0:
    print("hatalı puan girişi yaptınız")
elif puan < 70:
    print("Belge almaya puanınız yeterli değil")
elif puan < 85:
    print("teşekkür alabilirsiniz tebrikler")
elif puan <= 100:
    print("tebrikler ! takdir aldınız")
else:
    print("lütfen geçerli bir puan giriniz")

# sınıf seviyesi kontrolü
sinif = int(input("hangi sınıfa gidiyorsun: "))

if sinif == 0:
    print("okul öncesi")
elif 1 <= sinif <= 4:
    print("ilkokul")
elif 5 <= sinif <= 8:
    print("ortaokul")
elif 9 <= sinif <= 12:
    print("ortaöğretim")
else:
    print("geçerli bir sınıf seviyeniz yok")

# çok değişkenlerin yazımı
'''
a = 5
b = 6
c = 85
'''
a, b, c=5, 6, 85
print(a + b + c)
print(a * b * c)




a, b = 9, 15
print(a, b)
'''
sayi1 = a
sayi2 = b

a= sayi2
b= sayi1
'''
a,b = b,a
print(a,b)




a = 2
if a <= 4:
    sonuc = "kücüktür"
else:
    sonuc = "büyüktür"

print(sonuc)
sonuc = "kücüktür" if a<=4 else "büyüktür"
# a 4'den küçükse 'küçüktür' değilse 'büyüktür' yaz
print(sonuc)

print("kücüktür" if a<=4 else "büyüktür")


# haftanın kaçıncı günündeyiz ?
gun = int(input("haftanın kaçıncı günündeyiz"))

'''
if gun == 1:
    print("pazartesi")
elif gun == 2:
    print("salı")
elif gun == 3:
    print("çarşamba")
elif gun == 4:
    print("perşembe")
elif gun == 5:
    print("cuma")
elif gun == 6:
    print("cumartesi")
elif gun == 7:
    print("pazar")
else:
    print("hatalı gün girişi")
'''

if gun == 1 or gun == 3 or gun == 6:
    print("Python Bootcamp var")
elif gun == 2 or gun == 4 or gun == 5 or gun == 7:
    print("bugün bootcamp yok")
else:
    print("hatalı gün girişi")

# match case
'''
match gun:
    case 1:
        print("pazartesi")
    case 2:
        print("salı")
    case 3:
        print("çarşamba")
    case 4:
        print("perşembe")
    case 5:
        print("cuma")
    case 6:
        print("cumartesi")
    case 7:
        print("pazar")
    case _ :
        print("hatalı gün girişi")
'''
match gun:
    case 1 | 3 | 6:
        print("bugün bootcamp var")
    case 2 | 4 | 5 | 7:
        print("bugün bootcamp yok")
    case _ :
        print("hatalı gün girişi")

#string
isim = "gizemilaydakoz"
boyut = len(isim)
print(boyut)
print(isim[0])
print(isim[13])

#print(isim[baslangiç:bitiş:artış])
print(isim[0:6]) #gizemi
print(isim[:6]) #gizemi
print(isim[:6:1]) # 1'er arttır. gizemi



ad1="gizem"
ad2="ilayda"
surname="koz"

print(ad1 + ad2 + surname)
print(f"{ad1} {ad2} {surname}")

metin = "Merhaba Sayın {} Python Bootcampine Hoşgeldiniz"

print(metin.format(ad1))
print(metin.format(ad2))

metin2 = "yarışmamızın 1.si {}, 2.si {}"
print(metin2.format(ad1,ad2))
print(metin2.format(ad2,ad1))

print(metin2.count("s"))

# print(help(len))  -> len komutu hakkında bilgi yazdırır

print("gizem", "ilayda", sep = "\t") # kelimeler arasına 1tab boşluk bırakır

import random
sayi = random.randint(1,10)
# 1-10 aralığında rastgele sayı üretir
print(sayi)

#sayı tahmini
tutulan_sayi = random.randint(1,10)
tahmin = int(input("bir sayı tahmin ediniz"))

if tahmin == tutulan_sayi:
    print("bildiniz tebrikler!")
else:
    print("tekrar deneyiniz")
    print("tutulan sayı: ",tutulan_sayi)