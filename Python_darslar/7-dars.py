                # 7-DARS #      # 7-DARS #      # 7-DARS #
                              # LISTLAR # 
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narxlar = [24000, 12000, 22900, 15000, 38000, -27, 3.14]
sonlar = ['bir', 'ikki', 3, 4, 5]
ismlar = []
        # INDEX #
print("Birinchi meva:",mevalar[0])
print("Ikkinchi meva:",mevalar[1],'\n')
        # METHODLAR BILAN ISHLASH #
print("Birinchi meva:",mevalar[0].title())
print("Ikkinchi meva:",mevalar[1].upper(),'\n')
        # SONLARNI BIR BIRIGA QOSHISH #
print(narxlar[2] + narxlar[5])
print(narxlar[3] + narxlar[-1],'\n')
        # ELEMENTNI O'ZGARTIRISH #
narxlar = [13000, 20000, 10700, 22000]
narxlar[0] = 11000
narxlar[1] = 1000
narxlar[2] = 500000
narxlar[3] = -412
print(narxlar,'\n')
        # METHODLAR #       # METHODLAR #       # METHONDLAR #
    # .append() <--- METHODI #   append methodi - listni ohiridan yangi element qoshadi #
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append('tarvuz')
print(mevalar,'\n')
    # <----------------------->
cars = []
cars.append("Lamborghini")
cars.append("Bugatti")
cars.append("BMW")
print(cars,'\n')
    # .insert() <--- METHODI #   insert methodi - listni hohlagan joyimizdan yangi element qoshadi #
cars = ['Lamborghini', 'Bugatti', 'BMW']
cars.insert(0, 'Malibu')
print(cars,'\n')
cars.insert(2, "Spark")
print(cars,'\n')
    # del ...[] <--- METHODI #   del methodi - listni ichidan hohlagan elementni o'chirib tashalaydi #
cars = ['Gentra', 'Nexia 3', 'Cobalt']
del cars[1]
print(cars,'\n')
    # .remove() <--- METHODI #   remove methodi - list ichidagi elementni nomini yozsak o'chirib tashalydi #
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.remove('shaftoli')
print(mevalar,'\n')
       # <----------------------> #       
hayvonlar = ['kuchuk', 'mushuk', 'quyon', 'tovuq', 'ot', 'mushuk']
hayvonlar.remove('mushuk')
print(hayvonlar,'\n')
    # .pop() <--- METHODI #   pop methodi - list ichjidagi hohlagan elementimizni sug'irib oladi #
bozorlik = ['piyoz', 'un', 'banan', 'Pepsi', "'go'sht"]
mahsulot = bozorlik.pop(3)
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ",bozorlik,'\n')

                        # AMALIYOT #
ismlar = ['Abbos', 'Abdumannon', 'Ibrohim']
print(ismlar[0],", bugun fudbol bo'ladimi ?")
print("Kechqurun tennisga borasanmi?",ismlar[1])
print("Kecha",ismlar[2],"bilan mashina haydadik.\n")
        # <-----------------> #
sonlar = [10, 25000, -27, 500, 36.6]
print(sonlar)
sonlar[0] =  12500
sonlar.insert(4, 27000)
print(sonlar)
sonlar[2] += 28
print(sonlar,'\n')
        # <-------------------> #
t_shaxslar = ['Amir Temur', 'Steve Jobs', 'Pushkin.']
z_shaxslar = ['Mike Tyson', 'Mark Zuckerberg', 'Saud Abdulwahed.']
print("Tarixiy shaxslar:",t_shaxslar,"\nZamonaviy shaxslar:",z_shaxslar,'\n')

t_shaxs = t_shaxslar.pop(1)
z_shaxs = z_shaxslar.pop(2)
print("'Apple' kompaniyasi asoschisi: " + t_shaxs + '.')
print("Meni dasturlash boyicha ustozim:",z_shaxs,'\n')
        # <-----------------> #
friends = []
friends.append('Abbos')
friends.append('Abdumannon')
friends.append('Baxodir')
friends.append('Amir')
friends.append('Alo')
friends.append('Muzaffar')
print(friends)
friends.remove('Muzaffar')
friends.remove('Amir')
print(friends,'\n')
friends.append('Shaxboz')
friends.insert(0, 'Mark')
friends.insert(3, 'Steve')
print(friends,'\n')

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(3))
print(mehmonlar)
print(friends)






















