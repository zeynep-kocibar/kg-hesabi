from tkinter import* 
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter.ttk import*

ekran=Tk() 
ekran.title("manav hesabı")
ekran.geometry("600x600")

ürünçeşit=["elma","armut","muz"]

ürüntürü=Label(text="ürünün yerli mi ithal mi olduğunu seçiniz")
ürüntürü.grid(column=0,row=0)

üçeşit=Label(text="hangi meyveyi alacağınızı seçiniz")
üçeşit.grid(column=0,row=2)

kaçkilo=Label(text="kaç kilo meyve aldığınızı giriniz")
kaçkilo.grid(column=0,row=4)

tür=["yerli","ithal"]

kilogram=Entry()
kilogram.grid(column=0,row=5)

def calıstır2(event):
    global yi
    if ürtür.get()=="yerli":
        yi=1
    elif ürtür.get()=="ithal":
        yi=2


def calıstır(event):
    global fiyat
    if meyve.get()=="elma" and yi==1:
        fiyat=6
    elif meyve.get()=="elma" and yi==2:
        fiyat=8
    elif meyve.get()=="armut" and yi==1:
        fiyat=5
    elif meyve.get()=="armut" and yi==2:
        fiyat=7
    elif meyve.get()=="muz" and yi==1:
        fiyat=9
    elif meyve.get()=="muz" and yi==2:
        fiyat=16


def bul():
    kg=(int(kilogram.get()))

    toplam=int(fiyat)*int(kg)+(int(fiyat)*int(kg))*18/100
    yazi["text"]=str(toplam) +str( "  kdv dahil fiyatı")

    if toplam > 100:
        toplam=toplam*90/100


meyve=ttk.Combobox()
meyve['values']=ürünçeşit
meyve.bind('<<ComboboxSelected>>',calıstır)
meyve.current(1)
meyve.grid(column=0,row=3)

ürtür=ttk.Combobox()
ürtür['values']=tür
ürtür.bind('<<ComboboxSelected>>',calıstır2)
ürtür.current(1)
ürtür.grid(column=0,row=1)

hesapla=Button(text="HESAPLA",command=bul)
hesapla.grid(column=0,row=6)

yazi=Label(text="..........." )
yazi.grid(column=0,row=7)

        


