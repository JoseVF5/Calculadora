import tkinter as tk
from View.Interface import Tela_principal
from Controller.Data import CalucaldoraApp


if __name__ == "__main__":

    # Inicializa primeiro a view como None, depois cria o controller com a view
    view = Tela_principal() # Cria a view sem controller
    controller = CalucaldoraApp(view)
    view = Tela_principal(controller)
    view.controller = controller # Passa o controller para a view
    view.frames_botoes()
    view.criar_botoes() 
    view.janela.mainloop()