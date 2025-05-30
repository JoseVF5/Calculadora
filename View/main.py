import tkinter as tk
from View.Interface import Tela_principal
from Controller.Data import CalucaldorApp


if __name__ == "__main__":
    janela = tk.Tk()

    # Inicializa primeiro a view como None, depois cria o controller com a view
    view = None
    controller = CalucaldorApp(view)
    view = Tela_principal(janela, controller)

    # Atualiza a view no controller (ajuste necessário)
    controller.View = view

    janela.mainloop()