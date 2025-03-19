# adabiyot=[
#     {"ism":"Abu abdulloh muhammad ibn Ismoil",
#     "yil":810,
#     "joy":"buxoroda",
#     "umir":60
#     }
#     ,
#     {
#         "ism":"abdulla qodiriy",
#         "yil":1894,
#         "joy":"toshkent",
#         "umir":44
#     },
#     {
#         "ism":"erkin vohidov",
#         "yil":1936,
#         "joy":"farg'ona",
#         "umir":80,
#     },
#     {
#         "ism":"alisher navoiy",
#         "yil":1441,
#         "joy":"Xirod",
#         "umir":60
#     }

# ]



# for val in adabiyot:
#     print(f"{val["ism"].title()} {val["yil"]}-yilda {val["joy"]} tavvalud topgan.{val["umir"]} yil umir ko'rgan \n" )
##################################################################################################################################################


# adabiyot=[
#     {"ism":"Abu abdulloh muhammad ibn Ismoil",
#     "yil":810,
#     "joy":"buxoroda",
#     "umir":60,
#     "asarlar":["al-jome as - sahih","al-adab al - mufrad","at-tarix al-kabir","at-tarix as-sag'r"]
#     }
#     ,
#     {
#         "ism":"abdulla qodiriy",
#         "yil":1894,
#         "joy":"toshkent",
#         "umir":44,
#         "asarlar":["o'kgan kunlar","mehrobdan chayon","obid ketmon"]
#     },
#     {
#         "ism":"erkin vohidov",
#         "yil":1936,
#         "joy":"farg'ona",
#         "umir":80,
#         "asarlar":["tong nafasi","qo'shiqlarim sizga","o'zbegim","qiziquvchan matmusa"]
#     },
#     {
#         "ism":"alisher navoiy",
#         "yil":1441,
#         "joy":"Xirod",
#         "umir":60,
#         "asarlar":["xamsa","lison ut - tayr","mahbub al - qulub","munoiot"]
#     }

# ]



# for val in adabiyot:
#      print(val["ism"],"ning mashxur asarlari")
#      for v in val["asarlar"]:
#         print(v) 


##################################################################################################################################################



# friends=[
#     {"ism":"ali",
#     "kino":["rembo","titnic","terminator"]
#     },
#     {"ism":"ilhom",
#     "kino":["qasoskorlar","qatiyat","matrix "]},
#     {
#         "ism":"alisher",
#         "kino":["aqil va yurka","devi jons ","king kong"]
#     }
# ]


# for val in friends:
#     print(val["ism"],"ning sevimli kinosi")
#     for v in val['kino']:
#         print(v,"ning sevimli kinos")
#     print("\n")   
# 
# 
# 
  
##################################################################################################################################################



# davlatlar=[
#     {
#         "davlat":"uzbekiston",
#         "shahri":"toshkent",
#         "hududi":448978,
#         "aholi":33,
#         "pul":"sum"
#     }
#     ,
#     {

#         "davlat":"rossiya",
#         "shahri":"moskva",
#         "hududi":17098246,
#         "aholi":144,
#         "pul":"rubil"
#     },
#     {
#         "davlat":"aqsh",
#         "shahri":"vashington",
#         "hududi":9631418,
#         "aholi":327,
#         "pul":"dollor"
#     }
#     ,
#     {
#         "davlat":"malayziya",
#         "shahri":"kuala-Lumpur",
#         "hududi":329750,
#         "aholi":25,
#         "pul":"rinngit"
#     }

# ]


# for val in davlatlar:
#     print(f"{val["davlat"]}ning poytaxti {val["shahri"]}\n hududi:{val["hududi"]} kv.km \n aholisi:{val["aholi"]}000000\n pul birligi:{val["pul"] }\n")


#########################################################################################################################################################################



davlatlar=[
    {
        "davlat":"uzbekiston",
        "shahri":"toshkent",
        "hududi":448978,
        "aholi":33,
        "pul":"sum"
    }
    ,
    {

        "davlat":"rossiya",
        "shahri":"moskva",
        "hududi":17098246,
        "aholi":144,
        "pul":"rubil"
    },
    {
        "davlat":"aqsh",
        "shahri":"vashington",
        "hududi":9631418,
        "aholi":327,
        "pul":"dollor"
    }
    ,
    {
        "davlat":"malayziya",
        "shahri":"kuala-Lumpur",
        "hududi":329750,
        "aholi":25,
        "pul":"rinngit"
    }

]



name=str(input("davlatni kiritin>>\t"))

# for val in davlatlar:
#     if name.lower() == val["davlat"].lower():
#          print(f"{val["davlat"]}ning poytaxti {val["shahri"]}\n hududi:{val["hududi"]} kv.km \n aholisi:{val["aholi"]}000000\n pul birligi:{val["pul"] }\n")
# if name.lower not in davlatlar:
#     print("bunday davlat topilmadi !!!!")   



