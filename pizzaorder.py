from tkinter import *
from tkinter import Listbox, Tk
from PIL import ImageTk, Image

pizza=Tk()
pizza.geometry("600x800") #pencere boyutu
pizza.title("Global AI Pizza Order") #pencere başlığı
name_label=Label(pizza, text="Adınız:")
name_label.grid(row=1, column=0)
name_entry=Entry(pizza, width=30)
name_entry.grid(row=1, column=1)

adress_label=Label(pizza, text="Adres:")
adress_label.grid(row=2, column=0)
adress_entry=Entry(pizza, width=30)
adress_entry.grid(row=2, column=1)

phone_label=Label(pizza, text="Telefon:")
phone_label.grid(row=3, column=0)
phone_entry=Entry(pizza, width=30)
phone_entry.grid(row=3, column=1)

pizzas_label=Label(pizza, text="Pizzalar:")
pizzas_label.grid(row=5, column=0)

#pizza listesi
my_pizza_list=["Klasik", "Margarita","Türk Pizza", "Sade Pizza"]



pizza_list=Listbox(pizza, selectmode=MULTIPLE, bg="gray", fg="yellow") #çoklu seçimler için
pizza_list.grid(row=5, column=1)

for item in my_pizza_list:
    pizza_list.insert(0,item)


def add_pizza():
    result=""
    for item in pizza_list.curselection():
        result=result + str(pizza_list.get(item)) +" \n"

        add_lbl.config(text= "Pizza seçiminiz: " +" \n " + result)

add_lbl = Label(pizza, text="")
add_lbl.grid(row=6, column=1)

#pizza ekleme
add_button=Button(pizza, text="Ekle", command= add_pizza)
add_button.grid(row=6, column=0)


def check():
    text1= name_entry.get()
    new_lbl = Label(pizza, text="Sayın " + text1)
    new_lbl.grid(row=6, column=2)

    text2 = adress_entry.get()
    new_lbl2 = Label(pizza, text="Adres: " + text2)
    new_lbl2.grid(row=7, column=2)

    text3 = phone_entry.get()
    new_lbl3 = Label(pizza, text="Telefon: " + text2)
    new_lbl3.grid(row=8, column=2)

#onay butonu
check_button=Button(pizza,text="Onay", command=check)
check_button.grid(row=7, column=0)


#toplam  butonu
total_result_button=Button(pizza,text="Toplam")
total_result_button.grid(row=9, column=0)

def deleteme():
    pizza_list.delete(0,5)
#silme butonu
del_button=Button(pizza,text="Sil",command= deleteme)
del_button.grid(row=8, column=0)

pizza_pic=ImageTk.PhotoImage(Image.open("pizza.png"))
pic_lbl = Label(pizza, image= pizza_pic)

pic_lbl.grid(row=2, column=7)
pizza.mainloop()