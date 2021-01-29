def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput != "arthit904" or passwordInput != "0860256015":
        print("False")
        return login()
    else:
        print("Welcome")
        showMenu()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print(priceCalculator())

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1*50 + price2*25)

login()
