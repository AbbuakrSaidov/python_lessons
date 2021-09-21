            # 11-DARS #             # 11-DARS #           # 11-DARS #

yosh = int(input("Yoshingizni kiriting: "))
if yosh <= 4:
    print("Sizga kirish bepul.")
elif yosh <= 12:
    print("Sizga kirish 5000 so'm")
else:
    print("Sizga kirish 10000 so'm")
print('\n')
    # Osonroq usuli #
yosh = int(input("Yoshingizni kiriting: "))
if yosh <= 4:
    narx = 0
elif yosh <=12:
    narx = 5000
else:
    narx = 10000

print(f"Sizga kirish {narx} so'm")
print('\n')
  
        # <--------------------------> #
    # and or OPERATORLARI #

kun = input("Bugun nima kun: ")
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    print("Bugun dam olish kuni!")
else:
    print("Bugun ish kuni!")
print('\n')
    # <---------> #
kun = input("Bugun nima kun: ")
harorat = float(input("Havo harorati qanday: "))
if kun.lower() == 'yakshanba' and harorat >= 30:
    print("Cho'milishga ketdik :)")
elif kun.lower() == 'yakshanba' and harorat <= 30:
    print("Uyda dam olamiz :(")
print('\n')
    # <---------> #
kun = input("Bugun nima kun: ")
harorat = float(input("Havo harorati qanday: "))
if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat >= 30:
    print("Toqqa chiqmaymizmi ?")
elif (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat <= 30:
    print("Uyda issiqda qolamiz")
print('\n')

        # <-----------------------------> #
    # BOOLEAN MA'LUMOTLAR TURI #

narx = 24000
choy = True
salat = False

if choy and salat:
    narx = narx + 9000
elif choy or salat:
    narx = narx + 5000
print(f"Jami bo'lib {narx} so'm\n")
    # <-----------> #
narx = 24000
choy = True
salat = False
non = True
kompot = True
assorti = False
if choy:
    print("Mijoz choy oldi")
    narx = narx + 3000
if salat:
    print("Mijoz salat oldi")
    narx = narx + 5000
if non:
    print("Mijoz non oldi")
    narx = narx + 2500
if kompot:
    print("Mijoz kompot oldi")
    narx = narx + 9000
if assorti:
    print("Mijoz assorti oldi")
    narx = narx + 19500
print(f"Jami {narx} so'm bo'ldi!\n")    

        # <-----------------------------> #
    # in OPERATORI #

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
print('manti' in menu)
print('osh' in menu,'\n')
    # <----------> #
menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input("Nima ovqat yeysiz: ")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi.")
else:
    print("Afsuski bizda bunday ovqat yo'q.")
print('\n')
    # <---------> #
menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
print('manti' not in menu)
print('osh' not in menu,'\n')
    # <---------> #
menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input("Nima ovqat yeysiz: ")
if ovqat.lower() not in menu:
    print("Afsuski bizda bunday taom yo'q")
else:
    print("Buyurtma qabul qilindi.")
print('\n')

        # <--------------------------------> #
    # IKKI RO'YXATNI SOLISHTIRISH #

menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik', 'shorva']
for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} mavjud.")
    else:
        print(f"Kechirasiz, menuda {taom} mavjud emas.")
print('\n')
    # <---------> #
menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik', 'shorva']
if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor.")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q.")
else:
    print("Savatchangiz bo'sh!")
print('\n')

        # <-------------------------------> #
    # AMALIYOT #

print("     AMALIYOT    \n")
juft_son = int(input("Juft son kiriting: "))
if juft_son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu juft son emas!")
print('\n')
    # <--------> #
yosh = int(input("Yoshingizni kiriting: "))
if yosh <= 4 or yosh >= 60:
    print("Kirish bepul!")
elif yosh <= 18:
    print("Kirish 10000 so'm")
elif yosh >= 18:
    print("Kirish 20000 so'm")
print('\n')
    # <--------> #
son1 = int(input("1-chi son kiriting: "))
son2 = int(input("2-chi son kiriting: "))
if son1 == son2:
    print(f"{son1} = {son2}")
elif son1 > son2:
    print(f"{son1} > {son2}")
elif son1 < son2:
    print(f"{son1} < {son2}")
print('\n')

    # <--------> #

mahsulotlar = ['non', 'Pepsi', 'muzqaymoq', 'kit-kat', 'sut', 'qaymoq', 'kalbasa', 'pishloq', 'Suv', 'banan', 'saryoq']
bor_mahsulotlar = []
yoq_mahsulotlar = []
savat = []
savat.append(input("Savatga 1-chi mahsulotni qo'shing: ")) 
savat.append(input("Savatga 2-chi mahsulotni qo'shing: "))
savat.append(input("Savatga 3-chi mahsulotni qo'shing: "))
savat.append(input("Savatga 4-chi mahsulotni qo'shing: "))
savat.append(input("Savatga 5-chi mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        yoq_mahsulotlar.append(mahsulot)
if yoq_mahsulotlar:
    print("Do'konimizda quyidagi mahsulotlar yo'q: ")
    for mahsulot in yoq_mahsulotlar:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar mavjud")
print('\n')
    # <---------> #  
foydalanuvchilar = ['S.A.F.', 'SAF_17', 'Simple_boy', 'SAF17', 'S.A.F.17']
login = input("Yangi login kiriting: ")
if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {login.title()}")
print('\n')

    # <---------> #
son = int(input("Istalgan butun son kiriting: "))
for n in range(2,11):
    if not(son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi." )
print('\n')

























