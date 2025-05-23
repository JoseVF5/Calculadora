import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# Cria a aplicação
myapp = App()

#
# aqui estão as chamadas de método para a classe do gerenciador de janelas
#
myapp.master.title("Meu Aplicativo Que Faz Nada")
myapp.master.maxsize(1000, 400)

# inicia o programa
myapp.mainloop()






