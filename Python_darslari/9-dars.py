               # 9-DARS #      # 9-DARS #      # 9-DARS #
        # LOOP (for) <--- operatori
mehmonlar = ['Ali', 'Vali', 'Hasan', "Husan", 'Aziz']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 27chi Avgust kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Saidovlar oilasi.\n")
        # <------------------> #
#mehmonlar = ['Ali', 'Vali', 'Hasan', "Husan", 'Aziz']
#for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon}, sizni 27chi Avgust kuni nahorga oshga taklif qilamiz")
#print("Hurmat bilan, Saidovlar oilasi.")

    # for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH #
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng\n")
        # <----------------> #
sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)

print(sonlar)
print(sonlar_kvadrati,'\n')
    # for va input() #
cars = []
print("5ta yahshi ko'rgan mashina modelini yozing")
for n in range(5):
    cars.append(input(f"{n+1}-mashinani nomini kiriting: "))
print(cars,'\n')
        # AMALIYOT #
ismlar = ['Smith', 'Windston', 'John Wick', 'Makentosh', 'Gatsby']
for ism in ismlar:
    print(f"Kino olamiga Hush kelibsiz Mr.{ism}\n")
print("Kod {} marta takrorlandi.".format(len(ismlar)),'\n')
        # <---------------------> #
toq_sonlar = list(range(11,101,2))
for toq_son in toq_sonlar:
    print(toq_son**3,'\n')
        # <-----------------------------> #
kinolar = []
print("5ta eng sevimli kinolaringizni yozing")
for kino in range(5):
    kinolar.append(input(f"{kino+1} kinoning nomi: "))
print("Sizning sevimli kinolaringiz: ",kinolar,'\n')
        # <----------------------------> #
odamlar = []
mens = int(input("Bugun necha kishi bilan suhbat qildingiz? : "))
for odam_soni in range(mens):
    odamlar.append(input(f"{odam_soni+1}-suhbat qilgan odamingiz kim edi: "))
print(odamlar)
    




















