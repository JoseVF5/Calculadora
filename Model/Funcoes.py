#Criar as funções de operações
class Operaçoes:
    
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
        else:
            raise ValueError("Operador inválido.")
           