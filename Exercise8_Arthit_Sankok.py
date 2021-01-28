username = input("Username :")
password = input("Password :")



if username == "arthit904" and password == "0860256015" :
    print("ยินดีต้อนรับ")
    print("!-----------------------------!")
    print("thit Shop")
    print("!-----------------------------!")
    print("Item")
    print("1.Water       :         10  THB")
    print("2.Snack       :         20  THB")
    print("3.Coco        :         40  THB")
    print("4.Coffee      :         45  THB")
    print("!-----------------------------!")
    SelectItem = int(input("selectItem>>>"))
    if SelectItem == 1 :
        item = int(input("Price (item) :"))
        price1 = int(input("Price 10 (THB) : "))
        vat = 0.07
        result = price1*item+(vat*price1*item)
        print(float(result))

    elif SelectItem == 2 :
        item = int(input("Price (item) :"))
        price2 = int(input("Price 20 (THB) : "))
        vat = 0.07
        result =price2*item+(vat*price2*item)
        print(float(result))
    elif SelectItem == 3:
        item = int(input("Price (item) :"))
        price3 = int(input("Price 40 (THB) : "))
        vat = 0.07
        result = price3*item+(vat*price3*item)
        print(float(result))

    elif SelectItem == 4 :
        item = int(input("Price (item) :"))
        price4 = int(input("Price 45 (THB) : "))
        vat = 0.07
        result = price4*item+(vat*price4*item)
        print(float(result))
