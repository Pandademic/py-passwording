# -*- coding: utf-8 -*-
import tkinter as tk
import random

root = tk.Tk()
root.geometry("400x400")
root.title("the password generator")


gen_label = tk.Label(root)
gu = tk.Label(root)
addt = tk.Entry(root)

pos1 = [[['5','1','8','3','4','1','7'],["one","two","six"],["a","c","d","e","f","g","i","j","k","l","m","n","o"]]]
pos2 = [[['!','@','$',':',',','<','/'],['~:&','^=`','|%+'],[';','*','{','}','[',']','.',',','(',')','_','-','"']]]
def generate():
     num_1 = random.randint(0,6)
     num_2 = random.randint(0,2)
     num_3 = random.randint(0,12)
     section_1 = str(pos1[0][0][num_1])
     section_2 = (pos1[0][1][num_2])
     section_3 = (pos1[0][2][num_3])
     section_4 = (pos2[0][0][num_1])
     section_5 = (pos2[0][1][num_2])
     section_6 = (pos2[0][2][num_3])
     passwd = section_6+ "" +section_2[2] + "" + section_5 +""+section_1 +""+ section_2[1] +""+section_3 + "" +section_4 +""+section_2[1]
     gen_label["text"] = passwd

def add():
   gu["text"] += " "+str(addt.get())
   
add_btn = tk.Button(root,command=add,text="add to guesed passwords",bg="red",fg="white")
btn = tk.Button(root,command=generate,text="Generate a (new) password",bg="blue",fg="white")

addt.pack()
add_btn.pack()
gu.pack()
btn.pack()
gen_label.pack()
root.mainloop()
