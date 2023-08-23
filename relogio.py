import tkinter as tk
from tkinter import *
import os
from time import strftime
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Relógio lindu')
window.geometry('600x320')
window.maxsize(600, 300)
window.minsize(600, 300)
window.configure(background="#1d1d1d")

largura = 50
altura = 50
light = Image.open('sol.png')
light_resize = light.resize((largura, altura))
light = ImageTk.PhotoImage(light_resize)
dark = Image.open('lua2.png')
dark_resize = dark.resize((largura, altura))
dark = ImageTk.PhotoImage(dark_resize)


def toggle_mode():
    if window['bg'] == "#1d1d1d":
        window['bg'] = 'white'
        tela['bg'] = 'white'
        saudacao['bg'] = 'white'
        data['bg'] = 'white'
        hora['bg'] = 'white'
        dark_mode_button['image'] = light
        dark_mode_button['bg'] = 'white'
    else:
        window['bg'] = '#1d1d1d'
        tela['bg'] = '#1d1d1d'
        saudacao['bg'] = '#1d1d1d'
        data['bg'] = '#1d1d1d'
        hora['bg'] = '#1d1d1d'
        dark_mode_button['image'] = dark
        dark_mode_button['bg'] = '#1d1d1d'

def getSaudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text = 'Olá Mundo!! Bem vinda ' + nome_usuario)

def getData():
    data_atual = strftime(' %a, %d %b %Y')
    data.config(text = data_atual)

def getHora():
    hora_atual = strftime('%H:%M:%S')
    hora.config(text = hora_atual)
    hora.after(1000, getHora)

dark_mode_button = Button(window, command=toggle_mode)
dark_mode_button.config(image=dark, bd=0, bg='#1d1d1d')
dark_mode_button.pack(pady=10)
tela = tk.Canvas(window, width=600, height=20, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
tela.pack()
saudacao = Label(window, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 16))
saudacao.pack()
data = Label(window, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 14))
data.pack(pady=2)
hora = Label(window, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 64, 'bold'))
hora.pack(pady=2)

getSaudacao()
getData()
getHora()

window.mainloop()