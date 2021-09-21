                # 5-DARS #      # 5-DARS #      # 5-DARS #

ism = "Anvar"

shahar = "Қўқон"
viloyat = 'Фарғона'

matn = "Men yangi 📱 oldim"
print(matn)

    # STRING USTIDA AMMALAR #
ism = "Ahmad"
print("Mening ismim " + ism)

ism = "Abubakr"
familiya = "Saidov"
print(ism + familiya)
print(ism + ' ' + familiya)

    # f-STRING #
ism = "Abubakr"
familiya = "Saidov"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = "John"
familiya = "Wick"
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

    # MAHSUS BELGILAR #
print("Hello world!")
print("\tHello\tworld!")
print("Hello \nworld!""\n")

    # STRING METODLAR #
ism = "JohN"
familiya = "WicK"
ism_familiya = f"{ism} {familiya}"
print(ism_familiya.upper())
print(ism_familiya.lower())
print(ism_familiya.title())
print(ism_familiya.capitalize(),"\n")

meva = "    Olma    "
print(meva)
print("Men " + meva.lstrip() + " ni yahshi ko'raman")
print("Men " + meva.rstrip() + " ni yahshi ko'raman")
print("Men " + meva.strip() + " ni yahshi ko'raman")
print("Men " + meva + " ni yahshi ko'raman\n")

    # UNPUT #
ism = input("Ismingiz nima? ")
print("Salom "+ ism +". Hush kelibsiz!")

ism = input("Ismingizni kiriting: ")
print("Salom "+ ism.title() +". Hush kelibsiz!\n")

    # AMALIYOT #
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati.")

kocha = input("Ko'changizni nomini kiriting: ")
mahalla = input("Mahallangizni nomini kiriting: ")
tuman = input("Tumaningizni nomini kiriting: ")
viloyat = input("Qaysi shaharda turishingizni kiriting: ")
manzil = f"{kocha} {mahalla} {tuman} {viloyat} "
print("\n",kocha.title()  + " ko'chasi,\n " + mahalla.lower() + " mahallasi,\n " + tuman.capitalize() + " tumani,\n " + viloyat.upper() + " shahri.")

 






