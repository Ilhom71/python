# family={"otam":"otamning ismi Imom,1979-yil, toshkent viloyat parkentda tug'ilgan","onam":"onamning ismi gulzoda 1982 -yil toshkent viloyat parkent tumanda tug'ilgan","bobom ":"bobomning ismi mirtoji 1949 - yil toshkent viloyatida tug'ilgan  "}

# print(family["otam"])

########################################################################################################################################

# s_taomlar={"bobom":"sho'rva ","dadam":"manti","onam":"chuchvara","opcham":"manti","men":"qozon-kabob","singlim":"chuchvara"}

# print("dadamning seveimli ovqati\t"+s_taomlar["dadam"])
# print("menning seveimli ovqati\t"+s_taomlar["men"])
# print("onamning seveimli ovqati\t"+s_taomlar["dadam"])

#############################################################################################################################################


p_l={"if":"agar degan ma'noni ifdalaydi","else":"aks holda degan mano beradi","range":"qator degani yoki sanoq uchun ishlatsa bo'ladi","elif":"agar aks holda shunday bo'lsin degan uchun ishlatiladi","or ":"yoki degani","and":"va degani","for":"bu sikil manosi ga degan manoni beradi ","append":"bu bir elemntga bola qilib beradi yoki qo'shadi","len":"uzunlik o'lcha uchun ishlatiladi","print":"chop etish degan mano kasb etdi va consolga malumotlarni chiqzadi","intger":"bu butun son tip","float":"bu o'nlik son tip","string":"matn tip","list ":"bu ro'yxatlar cuhun uishlaydi","input":"malumot kiritihs uchun ishlatiladi","remove":"bu malumotni olib tashlaydi0","del":"uchurishuchun ishlatiladi","get":"malumot ni kalit so'z boyicha oladi va malumotni chiqardi","title":"malumotni yozuvlarni bosh harifni katta qilib beradi","upper":"matn hammasini katta qiladi","lower":"matn hammasini kichik qiladi","capitlize":"nuqtadan keyingi hariflarni katta qiladi va boshni yam"}


l=str(input("nima kerak ?\t"))

ky=p_l.get(l,"bunday so'z yoq")
print(ky)
# if l in p_l:
#     print(p_l[l])
# else:
#     print("bunday so'z mavjud emas")    

