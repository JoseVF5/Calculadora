from Model.Funcoes import Operaçoes 

class CalucaldorApp:
    
    def __init__(self, View):
       self.operaçoes = Operaçoes()
       self.View = View() # recebe a view para poder interagir
       
    def calcular(self):
        try:
            num1 = float(self.View.entrada_num1.get())
            num2 = float(self.View.entrada_num2.get())
            operador = self.View.operador_var.get()

            resultado = self.operaçoes.calcular(num1, num2, operador)

            self.view.exibir_resultado(resultado)

        except ValueError as e:
            self.view.exibir_erro(str(e))
        except Exception as e:
            self.view.exibir_erro(f"Erro inesperado: {e}")