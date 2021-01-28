def vatCalculate(totalPrice) :
    result = totalPrice + (totalPrice*0.07)
    return result
price = int(input("Number :"))
print(vatCalculate(price))