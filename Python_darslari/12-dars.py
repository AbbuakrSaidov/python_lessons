            # 12-DARS #          # 12-DARS #          # 12-DARS #
            # XATOLAR BILAN ISHLASH #
            
        # SyntaxError - Sinteks XATOLIK #
#print "Hello World!"
    # EOL va EOF xatolik #
#print("Hello Wolrd!
#print("Hello World!"

        # IndentataionError - JOY TASHLASHDA XATOLIK #
#  print("Hello World!")

#print("O'ngacha sanaymiz")
#for n in range(10):
#print(n+1)

#son = 50
#if son >= 0:
#    print("Musbat son")
#else:
#print("Manfiy son")

        # RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK #
    # TypeError #
#son = input("Istalgan son kiriting: ")
#print(f"{son} ning kvadrati {son**2} ga teng")
    # NameError #
#prit("Hello World!")

#mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
#for meva in mvalar:
#    print(meva)
    # ValueError #
#son = int(input("Istalgan son kiriting: "))
#if son >= 0:
#    print("Musbat son")
#else:
#    print("Manfiy son")

    # IndexError #
#mevalar = ['olma', 'anor', 'uzum']
#print(mevalar[3])

    # ZeroDivisionError #
#x, y = 50, 50
#z = 250/(x-y)

    # MANTIQIY XATOLAR #
#radius = 5
#pi = 4.14   # pi <--- ning qiymati - 3.14
#aylana_yuzasi = pi*radius**2
#print(aylana_yuzasi)

#son = float(input("Istalgan son kiriting: "))
#ildiz = son**1/2    # ildiz = son**(1/2)
#print(f"{son} ning ildizi {ildiz} ga teng")

#mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
#for meva in mevalar:
#    print(meva)
#    print("Dastur tugadi")  # printni chiziqtan yozish kerak edi


        # AMALIYOT #
son = int(input("Juft son kiriting: "))
if son%2==1:        # bu yerda ==0 emas ==1 qilish kerak
    print("Bu son juft emas.")      # bu yerda " <- qolib ketkan 
else:
    print("Rahmat")    # bu yerda 1ta qovs ortiqcha 
print('\n')

yosh = int(input("Yoshingizni kiriting: "))      # bu yerda sonni bilish uchun -> int <- qolib ketkan 

    # <---------> #
if yosh <= 4 or yosh >=60:
    narx = 0
elif yosh <18:
    narx = 10000
else:
    narx = 20000
print(f"Chipta {narx} so'm\n")    # bu yerda kodni chiziqtan yozish kerak

    # <----------> #
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x} = {y}")
elif x<y:
    print(f"{x} < {y}")     # bu yerda " <- ni orniga ' bolib qolgan
else:       # bu yerda ikki nuhta qolib ketkan -> : <-
    print(f"{x} > {y}")
print('\n')

    # <----------> #
mahsulotlar = ['un', "yog'", 'sovun', 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']  # bu yerda qovus yopilmagan -> ]         
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))     # bu yerda savat degan yangi list ochilmagan
if savat :
    for mahsulot in savat:      # bu yerda ikki nuhta qolib ketkan -> :
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do;konimizda {mahsulot} yo'q")
else:
    print("Savatchangiz bo'sh")
print('\n')

    # <---------> #
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))  # bu yerda yoki qoshtirnoq qilish kerak edi, yoki qo\'shing diyish kerak edi
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)    # bu yerda qovs ichidagi -> mahsulot so'zi notog'ri yozilgan
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulot yo'q: ")
for mahsulot in mavjud_emas:
    print(mahsulot)
if savat==bor_mahsulotlar:      # bu yerda else ning o'rniga if qilib savatni bor_mahsulotga tenglashtirish kerak edi
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
print('\n')

    # <----------> #
users = ['alisher1983', 'aziza', 'yasina' 'umar']   # bu yerda tutuq belgisi estan chiqqan va ikta ism birga bo'lib qolgan
login = input("Yangi login tanlang: ")  # bu yerda qoshtirnoq o'rniga 1tirnoq bo'lib qolipti
if login in users:
    print('Login band, yangi login tanlang!')   # bu yerda tanlang so'zi notog'ri yozilgan
else:
    print("Xush kelibsiz!")





