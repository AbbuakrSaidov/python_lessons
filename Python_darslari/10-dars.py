            # 10-DARS #         # 10-DARS #         10-DARS #
        # if else OPERATORI #

avtolar = ['audi', 'bmw', 'hyundai', 'volvo', 'bugatti']
for avto in avtolar :
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title(),)

    # <---------------------> #
ism = input("\nIsmingizni kiriting: ")
if ism.lower() != 'ali':
    print(f"Uzr, {ism.title()}, biz Alini kutyapmiz.")
else: 
    print("Salom Ali.")

    # <----------------------> #
javob = float(input("12 * 6 nechiga teng: "))
if javob != 72:
    print("Javob xato!")
else:
    print("To'gri javob!")

    # <---------------------------> #
yosh = int(input("Yoshingizni kiriting: "))
if yosh >= 18:
    print("Xush kelibsiz!")
else:
    print("Kirish mumkin emas!")
    
    # <--------------------------> #
login = input("Yangi login kiriting: ")
if len(login) <= 5:
    print("Login 5ta belgidan ko'proq bo'lishi kerak!")
else:
    print("Xush kelibsiz!")

    # <------------------------> #
yil = int(input("Tug'ilgan yilingizni kiriting: "))
if 2021-yil < 18:
    print(f"Yoshingiz {2021-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz")

    # <--------------------------> #
yosh = int(input("Yoshingizni kiriting: "))
if yosh > 65: print("Siz Covid-19 risk guruhida ekansiz")

    # <--------------------------> #
x, y = 25, 50
print("\nx>y") if x>y else print("\nx<y")


            # AMALIYOT #

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
print('\n')
        # <----------------------> #
        
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
print('\n')
        # <------------------> #
login = input("Login kiriting: ")
if login == 'admin':
    print("Hush kelibsiz Admin. Foydalanuvchilar ro'yxatini korasizmi ?")
else:
    print("Hush kelibsiz", login)
print('\n')
        # <------------------------> #
son1 = int(input("1-chi son kiriting: "))
son2 = int(input("2-chi son kiriting: "))
if son1 == son2:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")
print('\n')
        # <----------------------------> #
son = int(input("Son kiriting: "))
if son >= 0:
    print("Siz musbat son kiritingiz")
else:
    print("Siz manfiy son kiritingiz")
print('\n')

        # <----------------------> #
son = float(input("Son kiriting: "))
if son > 0:
    print(son**(1/2))
else:
    print("Musbat son kiriting")









