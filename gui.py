from tkinter import *
from PIL import ImageTk , Image
import main

window = Tk()
window.geometry("600x400")

def refresh():
    price = "Bitcoin price : " +  str("{:.10f}".format(main.getPrice())) + " USD" 
    priceDispay["text"] = price
    
imgBitcoin = ImageTk.PhotoImage(Image.open("iconmonstr-bitcoin-3.png"))

priceDispay = Label(window , text = "", font = ("Helvetica" , 16))

priceDispay.pack()

imgLabel = Label(window , image=imgBitcoin)
imgLabel.image = imgBitcoin
imgLabel.pack()


refreshBtn = Button(window , text="refresh" , command=refresh )
refreshBtn.pack()




window.mainloop()