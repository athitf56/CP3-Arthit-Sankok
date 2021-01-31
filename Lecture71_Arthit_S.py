menulist = []
menuprice = []

def showBill():
    Count = 0
    print("---ThitShop---")
    for number in range(len(menulist)):
        print(menulist[number], menuprice[number])
        Count +=  menuprice[number]
    print("Total =", Count, "Bath")


while True :
    menuName = input("กรุณาใส่ชื่อเมนู : ")
    if(menuName.lower() == "exit" ):
        break
    else:
        menuPrice = int(input("กรุณาใส่ราคาเมนู : "))
        menulist.append(menuName)
        menuprice.append(menuPrice)

showBill()
