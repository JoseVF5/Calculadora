import tkinter as tk
from tkinter import *


# Criação da janela 
class Tela_principal:

    # Criação da janela principal e chamado as operações
    def __init__(self): 
        self.janela = tk.Tk()
        self.valor_atual = ""
        # Execução dos metódos
        
        self.config_tela()
        #self.atualizar_display()
        self.conteiner_display_e_tela()
        self.centralizar_app()
        self.enquadramento()     
        self.janela.mainloop()
        
    def config_tela(self):
        self.janela.title("Calculadora em Python")
        self.janela.geometry("318x430")
        self.janela.config(bg="darkolivegreen1", bd=0)
        self.janela.iconbitmap("View/imagens/Tittle Icon/Python.ico")
        
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
        self.frame_display = Frame(self.janela, 
                                   width=318, 
                                   height=90, 
                                   bg="green") # Cor original darkgreenlight1
        self.frame_display.place(x=0, y=0)
        
        # Criando o label do display 
        #(label é um widget usado para implementar caixas de exibição onde você pode inserir texto ou imagens)

        self.label_display = Label(self.frame_display,
                                   text=self.valor_atual, 
                                   font="Arial 28", 
                                   width=14,  
                                   height=2 , 
                                   padx=1, 
                                   pady=6, 
                                   relief=FLAT,
                                   anchor="e",
                                   justify="right",
                                   bg="green",
                                   fg="white")
        self.label_display.place(x=0, y=0)
    
    # Criando a função para atualizar o Display
    #def atualizar_display(self):
        #self.label_display.config(text=self.valor_atual)
     
    # Função para inserir valores e operadores       
    def inserir_valor(self, valor):
        self.valor_atual += str(valor)
        self.atualizar_display()
    
    def Calcular_o_resultado(self):
        try:
            resultado = str(eval(self.valor_atual.replace('x', '*').replace('÷', '/')))
            self.valor_atual = resultado
        except:
            self.valor_atual = "Erro"
            self.atualizar_display()   
        
    # Criando as funções para apagar e limpar
    def limpar(self):  
        self.valor_atual = ""
        self.atualizar_display()

    def apagar(self):
        self.valor_atual = self.valor_atual[:-1]
        self.atualizar_display()    
    
    # Criando a função porcentagem
    def porcentagem(self):
        try:
            resultado = eval(self.valor_display) / 100
            self.valor_display = str(resultado)
            self.label_display.config(text=self.valor_display)
        except:
            self.label_display.config(text="Erro")
            self.valor_display = ""    
            
                           
        # Criação do container do corpo
        self.frame_tela = Frame(self.janela, 
                                width=318, 
                                height=410)
        self.frame_tela.place(x=0, y=490)

        # Criação dos containers dos botões
        self.frame_botão_clear = Frame(self.janela,
                                       relief="groove", 
                                       width=90,
                                       height=70, 
                                       borderwidth=0.6,
                                       bg="cornsilk1")
        self.frame_botão_clear.place(x=0, y=90)
        
        self.frame_porcentagem = Frame(self.janela, 
                                  relief="groove",
                                  width=90, 
                                  height=70,
                                  borderwidth=0.6, 
                                  bg="cornsilk1")
        self.frame_porcentagem.place(x=78, y=90)
        
        self.frame_apaga = Frame(self.janela, 
                                       relief="groove", 
                                       width=90, 
                                       height=70,
                                       borderwidth=0.6,
                                       bg="cornsilk1")
        self.frame_apaga.place(x=160, y=90)
        
        self.frame_divisão = Frame(self.janela,
                                    relief="groove", 
                                    width=90, height=70, 
                                    borderwidth=0.6, 
                                    bg="cornsilk1")
        self.frame_divisão.place(x=240, y=90)
        
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
        
        self.frame_multiplicação = Frame(self.janela, 
                                relief="groove", 
                                width=90, 
                                height=60, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_multiplicação.place(x=240, y=158)
        
        self.frame_num6 = Frame(self.janela, 
                                relief="groove", 
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num6.place(x=0, y=226)
        
        self.frame_num5 = Frame(self.janela, 
                                relief="groove",
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num5.place(x=78, y=226)
        
        self.frame_num4 = Frame(self.janela, 
                                relief="groove", 
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num4.place(x=160, y=226)
        
        self.frame_subtração = Frame(self.janela, 
                                relief="groove",
                                width=90, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_subtração.place(x=240, y=226)
        
        self.frame_num3 = Frame(self.janela, 
                                relief="groove", 
                                width=80, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num3.place(x=0, y=294)
        
        self.frame_num2 = Frame(self.janela, 
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num2.place(x=78, y=294)
        
        self.frame_num1 = Frame(self.janela, 
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num1.place(x=160, y=294)
        
        self.frame_soma = Frame(self.janela, 
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_soma.place(x=240, y=294)
              
        self.frame_num0 = Frame(self.janela, 
                                relief="groove", 
                                width=159, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_num0.place(x=0, y=362)
        
        self.frame_virgula = Frame(self.janela,
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_virgula.place(x=160, y=362)
        
        self.frame_resultado = Frame(self.janela, 
                                relief="groove", 
                                width=84, 
                                height=70, 
                                borderwidth=0.6, 
                                bg="cornsilk1")
        self.frame_resultado.place(x=240, y=362)
     
    # Garantindo que os botões preencham os Frames
    def enquadramento(self):
        self.botão_clear = tk.Button(self.frame_botão_clear,
                                     text="Clear", 
                                     width=10, 
                                     height=4, 
                                     font="Arial 9",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = self.limpar)
        self.botão_clear.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_clear.pack(pady=0) # Adiciona espaço vertical ao Frame

        self.botão_porcentagem = tk.Button(self.frame_porcentagem,
                                     text="%", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 13",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = self.porcentagem)
        self.botão_porcentagem.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_porcentagem.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_apaga = tk.Button(self.frame_apaga,
                                     text="←", 
                                     width=9, 
                                     height=4, 
                                     font="Arial 10",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2", 
                                     command = self.apagar)
        self.botão_apaga.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_apaga.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_divisão = tk.Button(self.frame_divisão,
                                     text="÷", 
                                     width=7, 
                                     height=3, 
                                     font="Arial 12 bold",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="orange",
                                     command=lambda: self.inserir_valor("÷"))
        self.botão_divisão.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_divisão.pack(pady=0) # Adiciona espaço vertical ao Frame 
        
        self.botão_num9 = tk.Button(self.frame_num9,
                                     text="9", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 12",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = lambda: self.inserir_valor(9))
        self.botão_num9.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_num9.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_num8 = tk.Button(self.frame_num8,
                                     text="8", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 12",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = lambda: self.inserir_valor(8))
        self.botão_num8.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_num8.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_num7 = tk.Button(self.frame_num7,
                                     text="7", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 12",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = lambda: self.inserir_valor(7))
        self.botão_num7.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_num7.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_multiplicação = tk.Button(self.frame_multiplicação,
                                     text="x", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 13",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="orange",
                                     command=lambda: self.inserir_valor("x"))
        self.botão_multiplicação.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_multiplicação.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_num6 = tk.Button(self.frame_num6,
                                     text="6", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 12",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = lambda: self.inserir_valor(6))
        self.botão_num6.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_num6.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_num5 = tk.Button(self.frame_num5,
                                     text="5", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 12",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = lambda: self.inserir_valor(5))
        self.botão_num5.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_num5.pack(pady=0) # Adiciona espaço vertical ao Frame

        self.botão_num4 = tk.Button(self.frame_num4,
                                     text="4", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 12",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2", 
                                     command = lambda: self.inserir_valor(4))
        self.botão_num4.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_num4.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_subtração = tk.Button(self.frame_subtração,
                                     text="-", 
                                     width=7, 
                                     height=3, 
                                     font="Arial 13 bold",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="orange",
                                     command=lambda: self.inserir_valor("-"))
        self.botão_subtração.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_subtração.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_num3 = tk.Button(self.frame_num3,
                                     text="3", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 12",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = lambda: self.inserir_valor(3))
        self.botão_num3.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_num3.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_num2 = tk.Button(self.frame_num2,
                                     text="2", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 12",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = lambda: self.inserir_valor(2))
        self.botão_num2.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_num2.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_num1 = tk.Button(self.frame_num1,
                                     text="1", 
                                     width=8, 
                                     height=3, 
                                     font="Arial 12",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = lambda: self.inserir_valor(1))
        self.botão_num1.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_num1.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_soma = tk.Button(self.frame_soma,
                                     text="+", 
                                     width=7, 
                                     height=3, 
                                     font="Arial 13 bold",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="orange",
                                     command = lambda: self.inserir_valor("+"))
        self.botão_soma.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_soma.pack(pady=0) # Adiciona espaço vertical ao Frame
         
        self.botão_num0 = tk.Button(self.frame_num0,
                                     text="0", 
                                     width=17, 
                                     height=3, 
                                     font="Arial 12",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2",
                                     command = lambda: self.inserir_valor(0))
        self.botão_num0.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_num0.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_virgula = tk.Button(self.frame_virgula, # Vou utilizar ponto no lugar da vírgula, já que é o separador decimal em python
                                     text=".", 
                                     width=7, 
                                     height=3, 
                                     font="Arial 13 bold",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="antiquewhite2", 
                                     command = lambda: self.inserir_valor("."))
        self.botão_virgula.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_virgula.pack(pady=0) # Adiciona espaço vertical ao Frame
        
        self.botão_resultado = tk.Button(self.frame_resultado,
                                     text="=", 
                                     width=7, 
                                     height=3, 
                                     font="Arial 13 bold",
                                     relief=RAISED,
                                     overrelief="ridge",
                                     bg="orange")
        self.botão_resultado.pack(fill="both", 
                              expand=True) # Garante que o botão preencha o Frame
        self.botão_resultado.pack(pady=0) # Adiciona espaço vertical ao Frame
    
#Mantem a janela aberta
Tela_principal()