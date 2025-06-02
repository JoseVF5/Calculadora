from Model.Funcoes import Operacoes

class CalucaldoraApp:
    
    def __init__(self, view):
       self.View = view # recebe a view para poder interagir
       self.model = Operacoes() 
       self.valor_atual = ""
       
    def entrada_dados(self):            
        try:
            num1 = float(self.View.get_entrada_Num1())
            num2 = float(self.View.get_entrada_Num2())
            operador = self.View.get_operador()

            resultado = self.model.calcular(num1, num2, operador)
            self.View.exibir_resultado(str(resultado))

        except Exception as e:
            self.View.exibir_resultado("Erro: " + str(e))
       
       
    def inserir_valor(self, valor):
       self.valor_atual += str(valor)
       self.View.atualizar_display(self.valor_atual)
    
    def calcular_o_resultado(self):
        try:
         resultado = str(eval(self.valor_atual.replace('x', '*').replace('÷', '/')))
         self.valor_atual = resultado 
         self.View.atualizar_display(self.valor_atual)
        except:
          self.valor_atual = "Erro"
          self.View.atualizar_display()  # <- tem que atualizar após calcular  
        
    # Criando as funções para apagar e limpar
    def limpar(self):  
        self.valor_atual = ""
        self.View.atualizar_display()

    def apagar(self):
        self.valor_atual = self.valor_atual[:-1]
        self.View.atualizar_display()    
    
  