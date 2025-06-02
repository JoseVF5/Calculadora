#Criar as funções de operações
class Operacoes:
    
   def calcular(self, numero1, numero2, operador):
        if operador == '+':
            return numero1 + numero2
        elif operador == '-':
            return numero1 - numero2
        elif operador == '*':
            return numero1 * numero2
        elif operador == '/':
            if numero2 == 0:
                raise ValueError("Divisão por zero.")
            return numero1 / numero2
        elif operador == '%':
            try:
             expressao = self.valor_atual.replace('x', '*').replace('÷', '/')
             resultado = eval(expressao) / 100
             self.valor_atual = str(resultado)
            except:
             self.valor_atual = "Erro"
             self.atualizar_display()
        else:
            raise ValueError("Operador inválido.")
           