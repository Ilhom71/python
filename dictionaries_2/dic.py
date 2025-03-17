# l={"for":"bu sikil elementlar ni aylantirish uchun ishlatiladi",
#     "if" :"agar degan mano bildiradi u elemenlarni tarmoqlash uchun qo'llanadi",
#     "del":"list elementlarni o'chirish uchun qo'llanadigan metod",
#     "sorted":"list elementlarni o'zgartirmasdan tartiblaydi ",
#     "title":"bu textni bosh harif bilan yoz uchun qo'llanadi",
#     "tutle":"o'zgarmas ro'yxat",
#     "items()":"bu lug'at ichidagi elementlarni olib beradi",
#     "in ":"ichidda degan manoni bildiradi"

# }


# for key,val in l.items() :
#     print(f"key: {key}\n val: {val}")
####################################################################################3

# davlatlar={
#     "AQSH":"Vashington ",
#     "uzbekiston":"Toshkent",
#     "Fransiya":"parij",
#     "Ispaniya":"Madrid",
#     "rossiya":"moskova",
#     "yaponiya":"tokio",

# }

# print("davlatlar")
# for val in davlatlar.keys():
#     print(val)

# print("\npoytaxtlar\n")
# for val in davlatlar.values():
#     print(val)


# d=str(input("davlat kiriting \t"))


# for val in davlatlar.keys():

#     if d.lower() == val.lower():
#         print(f"{val}ning poytaxti {davlatlar[val]}") 
#     else :
#         print("bunda malumot topilmadi")

###########################################################################################

# taomlar={
#     "osh":25000,
#     "non":5000,
#     "choy":3000,
#     "manti":30000,
#     "shashlik":10000,
#     "somsa":10000,
#     "jaz":14000,
#     "norin":32000,
#     "halim":30000,
#     "gril":25000

# }


# print("3ta taom buyirtma berin")

# t1=str(input("1-toamni :\t"))
# t2=str(input("2-toamni:\t"))
# t3=str(input("3-toamni:\t"))

# h=0;


# b=[t1,t2,t3]

# for val in b:
#     if val.lower() in taomlar:
#         h+=taomlar[val]
#     else:
#         print(f"biz {val} yoq")    


# print("sizda " ,h," sum")        