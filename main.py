import tkinter as tk
from View.Interface import Tela_principal
from Controller.Data import CalucaldoraApp


if __name__ == "__main__":

    # Inicializa primeiro a view como None, depois cria o controller com a view
    view = None
    controller = CalucaldoraApp(view)
    view = Tela_principal(controller)

    # Atualiza a view no controller (ajuste necessário)
    controller.View = view

    view.janela.mainloop()