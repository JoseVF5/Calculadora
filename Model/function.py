#Criar as funções de operações
class Operaçoes:

    def soma(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero!")
        return a / b
 
    def calcular_expressão():
    
        try:
            a = float(input("Escolha um número de ponto flutuante: "))
            b = float(input("Escolha outro número de ponto flutuante: "))
        except ValueError:
            print("Por favor, digite números válidos!")
            exit()
        