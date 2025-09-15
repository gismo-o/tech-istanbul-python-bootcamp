
print("tech istanbul bootcamp")
"""
çok
satırlı
yorum

"""
#data types
print(type(23)) #int
print(type(5.2)) #float
print(type(True)) #boolean
print(type("tech istanbul")) #string
print(type([1,2])) #list
print(type({1, 2})) #set
print(type((1, 2))) #tuple
print(type({"name":"gizem"})) #dictionary

#operators
#aritmetik operatörler
print(8 + 5)
print(8 - 5)
print(8 * 5)
print(8 / 5)
print(5 ** 2) # 5*5
print(5 // 2) # tam bölme , 1
print(5 % 2) # mod
print("Tech" + "Istanbul")
print("python" * 3)

#karşılaştırma operatörleri
print("tech" == "istanbul") #false
print(9 != 5) #true
print(8 <= 5) #false
print(8 > 3) #true

#mantıksal operatörler
print((20 >= 18) and (0 >= 1)) #false
print((20 >= 70) or (5 >= 1)) #true
print(not(("x" == "y"))) #true

#atama operatörleri
num = 9
print(num)

num += 5 #num = num + 5
print(num)

# typecasting
num = int("35") #rakamlardan olustugundan bunu int'e cevirebiliriz
print(num, type(num))

num2 = 98 #int
rakamlar = str(num2)
print(rakamlar, type(rakamlar)) #str

# kullanıcıdan veri alma - input() method
#inputla gelen bilgi her zaman str
print("adınız nedir?")
ad = input() #str
print("memnun oldum", ad)

# ----------KİŞİSEL TANITIM KARTI-----------
ad=input("Adınız: ")
yas=int(input("Yaşınız: "))
sehir=input("Şehir: ")
hobi=input("Hobiniz: ")
boy = float(input("boyunuzu giriniz: "))
devam_durumu = bool(input("Devam durumunuz: ")) #boş veri false, dolu true

print("İsim: ", ad)
print("Yaş: ", yas)
print("Şehir: ", sehir)
print("Hobi: ", hobi)
print("Boy: ", boy)
print("Devam Durumu: ", devam_durumu)

