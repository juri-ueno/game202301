from cProfile import label
from pydoc import text
from random import random
import tkinter as tk
import random
import numpy as np
from tkinter import messagebox


class Animal():
    '''要素'''
    def __init__(self,animal,CARAnp,CARAimg,INFOnp):
        self.name     =animal  #動物の名前
        self.serif_np =CARAnp  #＜おしゃべり＞動物のセリフの行列
        self.serif_img=CARAimg #＜おしゃべり＞動物のセリフの画像
        self.jouho_np =INFOnp  #＜おやすみ　＞動物のヒントの行列
    
    def get_animal(self,animal):
        animal
        print('{}です',format(self))



        


n=0
level=0

kuma=Animal('くま',kuma_ohanasi , 'CARAimg',kuma_oyasumi, )

'''代入＝動物＆難易度選択'''
def btn_kuma():      
    kuma_btn['state']=tk.DISABLED
    usa_btn ['state']=tk.DISABLED
    neko_btn['state']=tk.DISABLED
    label_dobutu['text']='くまですね'


def btn_usa():
    kuma_btn['state']=tk.DISABLED
    usa_btn ['state']=tk.DISABLED
    neko_btn['state']=tk.DISABLED
    animal=2
    if animal==1:
        label_dobutu['text']='くまですね'
    elif animal==2:
        label_dobutu['text']='うさぎですな'
    elif animal==3:
        label_dobutu['text']='ねこですか'

def btn_neko():
    kuma_btn['state']=tk.DISABLED
    usa_btn ['state']=tk.DISABLED
    neko_btn['state']=tk.DISABLED
    animal=3
    if animal==1:
        label_dobutu['text']='くまですね'
    elif animal==2:
        label_dobutu['text']='うさぎですな'
    elif animal==3:
        label_dobutu['text']='ねこですか'



def LEVELL():
    level= nanido_scl.get()
    label_難易度説['text']=level
    


def say_situmon():
    ety_kaitou.delete(0,tk.END)
    a=random.randint(0,len(kuma_ohanasi[0]))
    situmon=kuma_ohanasi[0,a]
    label_situmon['text']=situmon
    btn_kaitou['state']=tk.NORMAL  

def say_hentou():
    b=random.randint(0,len(kuma_ohanasi[0]))
    hentou=kuma_ohanasi[random.randint(1,2),b]
    label_hentou['text']=hentou
    ety_kaitou.delete(0,tk.END)
    btn_oha_owari['state']=tk.NORMAL
#    (kaitou_kisou, + "回目：", + ety_kaitou.get() )

def oha_owari():
    label_situmon['text'] = ()
    label_hentou ['text'] = () 
    btn_kaitou   ['state']=tk.DISABLED
    btn_oha_owari['state']=tk.DISABLED
    situmon=0
    hentou=0
    return situmon,hentou,
 


nn=nanido_scl.get()
if   nn==1:
      level=5
elif nn==2:
      level=10
elif nn==3:
      level=15


if n==level:
    messagebox.showinfo("GAME CLERE", "ℓℴℴk!!>>   You've got to the GOAL ,,,FANTASTIC!")

