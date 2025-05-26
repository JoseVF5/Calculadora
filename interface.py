import tkinter as tk
from tkinter import PhotoImage
from tkinter import *


# Criação da janela 
class Tela_principal():
    
    # Criação da janela principal
    def __init__(self,): 
        # Atributos
        self.janela = tk.Tk()

        # Execução dos metódos
        self.config_tela()
        self.conteiner_display_e_tela()
        self.centralizar_app()
        self.enquadramento()
        self.janela.mainloop()
        
    def config_tela(self):
        self.janela.title("Calculadora em Python")
        self.janela.geometry("318x430")
        self.janela.config(bg="darkolivegreen1", bd=0)
        self.janela.iconbitmap("imagens/Tittle Icon/Python.ico")
        
        self.janela.resizable(False, False)
        
    def centralizar_app(self):
        # Tamanho fixo da janela
        largura_janela = 318
        altura_janela = 430
        
        # Obtém dimensões da tela do usuário
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        
        # Calcula a posição central
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        
        # Configura geometria para centralizar a aplicação na tela do usuário
        self.janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
       
    def conteiner_display_e_tela(self): 
        # Criação do container do display
        self.frame_display = Frame(self.janela, width=318, height=90, bg="darkolivegreen1")
        self.frame_display.place(x=0, y=0)
        
        # Criação do container do corpo
        self.frame_tela = Frame(self.janela, width=318, height=410)
        self.frame_tela.place(x=0, y=490)
        
        self.frame_botão_clear = Frame(self.janela,
                                       relief="groove", 
                                       width=90,
                                       height=70, 
                                       borderwidth=0.6,
                                       bg="cornsilk1")
        self.frame_botão_clear.place(x=0, y=90)
        
        self.frame_apagar = Frame(self.janela, 
                                  relief="groove",
                                  width=90, 
                                  height=70,
                                  borderwidth=0.6, 
                                  bg="cornsilk1")
        self.frame_apagar.place(x=78, y=90)
        
        self.frame_porcentagem = Frame(self.janela, 
                                       relief="groove", 
                                       width=90, 
                                       height=70,
                                       borderwidth=0.6,
                                       bg="cornsilk1")
        self.frame_porcentagem.place(x=160, y=90)
        
        self.frame_potência = Frame(self.janela,
                                    relief="groove", 
                                    width=90, height=70, 
                                    borderwidth=0.6, 
                                    bg="cornsilk1")
        self.frame_potência.place(x=240, y=90)
        
        self.frame_num9 = Frame(self.janela, 
                                relief="groove",
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num9.place(x=0, y=158)
        
        self.frame_num8 = Frame(self.janela, 
                                relief="groove", 
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num8.place(x=78, y=158)
        
        self.frame_num7= Frame(self.janela, 
                               relief="groove",
                               width=90, 
                               height=70, 
                               borderwidth=0.6, 
                               bg="cornsilk1")
        self.frame_num7.place(x=160, y=158)
        
        self.frame_num6 = Frame(self.janela, 
                                relief="groove", 
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num6.place(x=240, y=158)
        
        self.frame_num5 = Frame(self.janela, 
                                relief="groove", 
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num5.place(x=0, y=226)
        
        self.frame_num4 = Frame(self.janela, 
                                relief="groove",
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num4.place(x=78, y=226)
        
        self.frame_num3 = Frame(self.janela, 
                                relief="groove", 
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num3.place(x=160, y=226)
        
        self.frame_num2 = Frame(self.janela, 
                                relief="groove",
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num2.place(x=240, y=226)
        
        self.frame_num1 = Frame(self.janela, 
                                relief="groove", 
                                width=80, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num1.place(x=0, y=294)
        
        self.frame_num0 = Frame(self.janela, 
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num0.place(x=78, y=294)
        
        self.frame_num0 = Frame(self.janela, 
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num0.place(x=160, y=294)
        
        self.frame_num0 = Frame(self.janela, 
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num0.place(x=240, y=294)
        
        self.frame_num1 = Frame(self.janela, 
                                relief="groove", 
                                width=80, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num1.place(x=0, y=362)
        
        self.frame_num0 = Frame(self.janela, 
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num0.place(x=78, y=362)
        
        self.frame_num0 = Frame(self.janela,
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num0.place(x=160, y=362)
        
        self.frame_num0 = Frame(self.janela, 
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num0.place(x=240, y=362)
      
       # Funções para os botões
    def enquadramento(self):
        self.botão_clear = tk.Button(self.frame_botão_clear,
                                     text="Clear", 
                                     width=10, 
                                     height=4, 
                                     font="Arial 9",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2")
        self.botão_clear.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_clear.pack(pady=0) # Adiciona espaço vertical ao Frame
        
#Mantem a janela aberta
Tela_principal()

      