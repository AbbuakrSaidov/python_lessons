            # 8-DARS #          # 8-DARS #          # 8-DARS #
    # .sort() <--- METHODI #   sort methodi - list ichidagi elementlarni Alifbo tartibida qiladi #
cars = ['bmw', 'mersedes benz', 'volvo', 'tesla', 'audi', 'lamborghini']
cars.sort()
print(cars,'\n')

cars = ['bmw', 'mersedes benz', 'volvo', 'tesla', 'audi', 'lamborghini'] 
cars.sort(reverse=True)
print(cars,'\n')

mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat: ", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi: ",mehmonlar,'\n')
print(sorted(mehmonlar, reverse=True),'\n')
        # <----------------------> #
ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True),'\n')
        # RO'YXATNI AYLANTIRISH
    # .reverse() <--- METHODI #   reverse methodi - listni  aylantiradi (boshini ohiriga, ohirini boshiga) 
fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
fruits.reverse()
print(fruits,'\n')
    # len() <--- FUNCTIONI #   len fuctioni - listni uzunligni (ichidagi elementlarni sonini aniqlaydi)
fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
print("Elementlarni soni:",len(fruits),'\n')
    # range() <--- FUNCTIONI #   range functioni - ma'lum oraliqdagi sonlar ketma-ketligini yaratadi
sonlar = list(range(0,10))
print(sonlar,'\n')
        # <-----------------------------> #
juft_sonlar = list(range(0,20,2))
toq_sonlar = list(range(1,20,2))
print("Juft sonlar:",juft_sonlar)
print("Toq sonlar:",toq_sonlar,'\n')
    # max() min () sum() <--- FUNCTIONLAR #   max() - eng katta sonni bilish uchun  # min() - eng kichik sonni bilish uchun  # sum() - sonlar yig'indisini bilish uchun #
narxlar = [12000, 22500, 38700, 5600, 99748, 32465]
print(narxlar)
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print("Eng arzoni:",arzon,". Eng qimmati:",qimmat,". Jami bo'lib:",jami,'.\n')
        # <-----------------------> #
cars = ['bmw', 'mersedes benz', 'volvo', 'tesla', 'audi', 'lamborghini']
my_cars = cars[0:3]
print(my_cars)
print(cars[2:5])
print(cars[:4])
print(cars[2:],'\n')
        # <----------------------> #
sonlar = [1,2,3,4,5]
sonlar2 = sonlar[:] # [:] to'liq ro'yxatni ko'chirib oladi 
sonlar2.append(6)
sonlar2.append(7)
print("Bu sonlar ro'yxati:",sonlar)
print("Bu sonlar2 ro'yxati:",sonlar2,'\n')
    # TUPLES <--- O'ZGARMAS RO'YXAT #   list[] <-> tuples() 
tomonlar = (20,30,55.2)
print(tomonlar)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'pop it', 'lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])
        # <--------------------> #
#toys = ('bus', 'car', 'bear', 'dino', 'snake', 'pop it', 'lizard')
#toys[3] = 'dragon'
        # <--------------------> #
toys = ('bus', 'car', 'bear', 'dino', 'snake', 'pop it', 'lizard')
toys = list(toys)
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys)
print(toys,'\n')

                # AMALIYOT #
davlatlar = ['America', 'Rossiya', 'Japan', 'Dubai', 'Portugal', 'Ispain', 'Germany', 'Saudia Arabiya']
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar,'\n')
        # <--------------------> #
numbers = list(range(120,1201,2))
print(numbers,'\n')
print("120dan 1200gacha bo'lgan juft sonlar yig'indisi:",sum(numbers))
print("Eng katta son:",max(numbers))
print("Eng kichin son:",min(numbers))
print("Ro'yxatta:",len(numbers),"ta son bor\n")
print("Ro'yxat boshidan 20ta son:",numbers[:20])
print("Ro'yxat o'rtasidan 20ta son:",numbers[100:121])
print("Ro'yxat oxiridan 20ta son:",numbers[520:],'\n')
        # <----------------------> #
taomlar = ['osh', 'honim', "lag'mon", 'mastava', 'hot-dog']
nonushta = taomlar[:]
nonushta.append('qaymoq')
nonushta.append('sariyog')
nonushta.append('qahva')
nonushta.append('makaron')
nonushta.append('tovuq')
print("Taomlar:",taomlar)
print("Nonushta:",nonushta,'\n')
#nonushta = tuple(nonushta)
#nonushta[0] = "qaymoq va non"












