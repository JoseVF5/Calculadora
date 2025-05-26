from tkinter import *
from tkinter import ttk

#Criação da janela
janela = Tk()
janela.title("Calculadora em Python")
janela.geometry("318x490")
janela.config(bg="darkolivegreen1", bd=400)
janela.iconbitmap("imagens/Tittle Icon/Python.ico")

#definindo tamanho máximo e mínimo da janela 
janela.resizable(False, False)

#Criação do widgets e conteiners 

janela.mainloop()