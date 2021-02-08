print("กรุณาใส่เลือกค่าเงินแลกเปลี่ยน")
print("0. IDR = 13625.0" , "1. BGN = 1.7433", "2. ILS = 3.8794", "3. GBP = 0.68641")
print("4. DKK = 6.6289", "5. CAD = 1.3106" , "6. JPY = 110.36" , "7. HUF =  282.36")
print("8. RON = 4.0162", "9. MYR = 4.081", "10. SEK = 8.3419", "11. SGD = 1.3815")
print("12. HKD = 7.7673", "13. AUD = 1.3833" , "14. CHF = 0.99144" , "15. KRW = 1187.3")
print("16. CNY = 6.5475", "17. TRY = 2.9839", "18. HRK = 6.6731", "19. NZD = 1.4777")
print("20. THB = 35.73", "21. EUR = 0.89135", "22. NOK = 8.3212", "23. RUB = 66.774")
print("24. INR = 67.473", "25. MXN = 18.41" , "26. CZK = 24.089" , "27. BRL = 3.5473")
print("28. PLN = 3.94" , "29. PHP = 46.775", "30. ZAR = 15.747" , "31. USD= 30.0")
print("-------------------------------------------------------------")


list_forex = [['IDR', 13625.0], ['BGN', 1.7433], ['ILS', 3.8794], ['GBP', 0.68641]
 , ['DKK', 6.6289], ['CAD', 1.3106], ['JPY', 110.36], ['HUF', 282.36]
 , ['RON', 4.0162], ['MYR', 4.081], ['SEK', 8.3419], ['SGD', 1.3815]
 , ['HKD', 7.7673], ['AUD', 1.3833], ['CHF', 0.99144], ['KRW', 1187.3]
 , ['CNY', 6.5475], ['TRY', 2.9839], ['HRK', 6.6731], ['NZD', 1.4777]
 , ['THB', 35.73], ['EUR', 0.89135], ['NOK', 8.3212], ['RUB', 66.774]
, ['INR', 67.473], ['MXN', 18.41], ['CZK', 24.089], ['BRL', 3.5473]
 , ['PLN', 3.94], ['PHP', 46.775], ['ZAR', 15.747] , ['USD', 30.0]]

def Money_Exchange():
    Money = int(input("จำนวนเหรีญนเงิน : "))
    Select_Value = int(input("เลื่อกค่าเงินที่มี : "))
    Input_Select_Value  = list_forex[Select_Value][1]
    Value_Money = float(Money * Input_Select_Value)
    print("ค่าเงินที่มี : " , float(Value_Money))

    Select_Value_Change = int(input("เลื่อกค่าเงินที่ต้องการแลก : "))
    Input_Select_Value_Change = list_forex[Select_Value_Change][1]
    Value_Money_Change = float(Value_Money/Input_Select_Value_Change)
    print("ค่าเงินที่ต้องการแลก :" ,float(Value_Money_Change))


while True :
    print("โหมดแลกเงินกด 1 : โหมดหาค่าเฉลี่ยกด 2")
    if int(input('')) == 1 :
        Money_Exchange()




