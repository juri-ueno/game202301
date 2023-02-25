from cProfile import label
from pydoc import text
from random import random
import tkinter as tk
import random
import numpy as np
from tkinter import messagebox



'''メインウィンドウ'''
root=tk.Tk()
root.title('glawing')
root.geometry('1600x800')
root.configure(bg="black")  #グラフィック

background = tk.PhotoImage(file='skyc.png')
bg_img= background.zoom(2,2)
bg = tk.Label(root, image=bg_img)
bg.pack()



'''ヘッダー'''

label_header=tk.Label(root,text='≪ANIMAL GLAWING ≫ KUMA USA NEKO 　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　', 
                      font=('Helvetica',20,"bold"),fg='IndianRed' )
label_header.place(x=0,y=0)


'''動物選択'''
frame_dobutu = tk.Frame(root, width=340, height=150,bg='Linen', pady=5, padx=4,bd=1,)
frame_dobutu.place(x=750,y=60)

kumaimg  = tk.PhotoImage(file= 'bear.png' )
usaimg   = tk.PhotoImage(file= 'rabbit.png' )
nekoimg  = tk.PhotoImage(file= 'cat.png' )

くまimg  = kumaimg.subsample(6,6)
kuma_btn = tk.Button    (frame_dobutu, image=くまimg, command=btn_kuma)

うさimg  = usaimg.subsample(6,6)
usa_btn  = tk.Button    (frame_dobutu, image=うさimg, command=btn_usa)

ねこimg  = nekoimg.subsample(6,6)
neko_btn = tk.Button    (frame_dobutu, image=ねこimg, command=btn_neko)


label_dobutu=tk.Label   (frame_dobutu,text='a')

kuma_btn.place      (x=5,y=2)
usa_btn.place       (x=115,y=2)
neko_btn.place      (x=225,y=2)
label_dobutu.place  (x=10,y=120)

# 難易度設定
frame_nanido= tk.Frame(root, width=500, height=150, bg='Linen', pady=5, padx=4,bd=1,)
frame_nanido.place(x=20,y=60)


nanido_scl       = tk.Scale(frame_nanido, label = '難易度≳',     font=("游ゴシック"), orient ='horizontal',  from_=1,to =3, bg='AliceBlue')
btn_nanido       =tk.Button(frame_nanido, text='OK',                                                                        command=LEVELL)
label_難易度説明 =tk.Label (frame_nanido, text='1=低 2=中 3=高', font=("游ゴシック"),                                       bg='AliceBlue')
label_難易度説   =tk.Label (frame_nanido, text='0',                                                                         bg='AliceBlue')

nanido_scl.place      (x=8,y=2)
label_難易度説明.place(x=160,y=40)
btn_nanido.place      (x=65,y=100)
label_難易度説.place  (x=80,y=100)




# おしゃべり
frame_ohanasi = tk.Frame(root, width=640, height=250, bg='LightSteelBlue', pady=5, padx=4,bd=1,)
frame_ohanasi.place(x=20,y=200)


canvas=tk.Canvas(frame_ohanasi, width=200, height=200, bg='white')
canvas.place(x=80,y=28)



btn_situmon  =tk.Button(frame_ohanasi, text='おしゃべり', padx=5, pady=5, fg='White',     bg='SlateBlue',    activebackground='MediumPurple', command=say_situmon,                   )
label_situmon=tk.Label (frame_ohanasi, text='質問',       width=45,       fg='SlateBlue', bg='LemonChiffon', relief=tk.SOLID,                                                        )   

label_YOU    =tk.Label (frame_ohanasi, text='YOU:',       width=5,        fg='Indigo'                                                                                                ) 
ety_kaitou   =tk.Entry (frame_ohanasi,                    width=40,       fg='SlateBlue', bg='LemonChiffon'                                                                          )
btn_kaitou   =tk.Button(frame_ohanasi, text='OK',         padx=5, pady=5, fg='Indigo',                       activebackground='MediumPurple', command=say_hentou   ,state=tk.DISABLED)
label_hentou =tk.Label (frame_ohanasi, text='',           width=45,       fg='SlateBlue', bg='LemonChiffon', relief=tk.SOLID ,                                                       )
btn_oha_owari=tk.Button(frame_ohanasi, text='OK',         padx=5, pady=5, fg='Indigo',                       activebackground="MediumPurple", command=oha_owari,    state=tk.DISABLED)




btn_situmon.place  (x=10, y=10)
label_situmon.place(x=300,y=20)
label_YOU.place    (x=300,y=60)
ety_kaitou.place   (x=340,y=60)
ety_kaitou.insert  (tk.END,"ここに回答を入力してください")
btn_kaitou.place   (x=590,y=50)   
label_hentou.place (x=300,y=120)
btn_oha_owari.place(x=590,y=150)




# おやすみ
frame_oyasumi = tk.Frame(root, width=650, height=400,bg='Lavender', pady=5, padx=4,bd=1,)
frame_oyasumi.place(x=10,y=570)


def say_oyasumi():
    btn_okiru  ['state']=tk.NORMAL




btn_oyasumi  =tk.Button(frame_oyasumi, text='おやすみ', padx=5, pady=5, fg='White',     activebackground='SlateBlue',activeforeground='White', command=say_oyasumi, bg='DarkBlue')
label_oyasumi=tk.Label (frame_oyasumi, text='夢をみた', width=45,       fg='MediumBlue', relief=tk.SOLID)   

label_MUMUMU =tk.Label (frame_oyasumi, text='zzz....',  width=5,        fg='MediumBlue') 
btn_okiru    =tk.Button(frame_oyasumi, text='起きる',   padx=5, pady=5, fg='MediumBlue', activebackground="RoyalBlue", command=say_hentou,  state=tk.DISABLED )


'''位置'''
btn_oyasumi.place  (x=10, y=10)
label_oyasumi.place(x=300,y=10)
label_MUMUMU.place (x=300,y=50)
btn_okiru.place    (x=590,y=40)   




if n==level:
    messagebox.showinfo("GAME CLERE", "ℓℴℴk!!>>   You've got to the GOAL ,,,FANTASTIC!")


root.mainloop()





