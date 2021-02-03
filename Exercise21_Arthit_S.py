from tkinter import *
import math

def leftClickButton(event):
    scale = float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2)
    print(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    lableResult.configure(text =float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))

    if scale >= 30.0 :
        lableScale.configure(text = "อ้วนมาก")
    elif 25.0 <= scale and scale <= 29.9 :
        lableScale.configure(text = "อ้วน")
    elif 23.0 <= scale and scale  <= 24.9 :
        lableScale.configure(text = "น้ำหนักเกิน")
    elif 18.6  <= scale and scale <= 22.9 :
        lableScale.configure(text = "น้ำหนักปกติ เหมาะสม")
    else:
        lableScale.configure(text = "ผอมเกินไป")


main = Tk()
lableHight = Label(main,text = "ส่วนสูง (Cm.)")
lableHight.grid( row = 0 , column = 0)

textBoxHight = Entry(main)
textBoxHight.grid(row = 0 , column = 1)

lableWeight = Label(main,text = "น้ำหนัก (Kg.)")
lableWeight.grid( row = 1 , column = 0)

textBoxWeight = Entry(main)
textBoxWeight.grid(row = 1 , column = 1)

calculateButton = Button(main,text = "คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row = 2, column = 0 )

lableResult = Label(main,text = "BMI")
lableResult.grid( row = 2 , column = 1)

lableScale = Label(main,text = "Scale")
lableScale.grid( row = 2 , column = 2)

main.mainloop()