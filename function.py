
#Criar as funções de operações

class OperacoesBasicas:
    @staticmethod
    def soma(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero!")
        return a / b
 
#Entrada de dados
try:
    a = float(input("Escolha um número de ponto flutuante: "))
    b = float(input("Escolha outro número de ponto flutuante: "))
except ValueError:
    print("Por favor, digite números válidos!")
    exit()
    
#Perguntar ao usuário qual operação vai relizar
print("\nOperações disponíveis:")
print("0 - Multiplicação")
print("1 - Adição")
print("2 - Subtração")
print("3 - Divisão")

op = int(input("Qual será a operação a ser realizada de 0-3? ").strip())

try:
    if op == 0: 
        resultado = OperacoesBasicas.multiplicar(a, b)
        print(f"\n O resultado para é: {resultado:.2f}")
    elif op == 1:
        resultado = OperacoesBasicas.soma(a, b)
        print(f"\n O resultado para é: {resultado:.2f}")
    elif op == 2:
        resultado = OperacoesBasicas.subtrair(a, b)
        print(f"\n O resultado para é: {resultado:.2f}")
    elif op == 3:
        resultado = OperacoesBasicas.dividir(a, b)
        print(f"\n O resultado para é: {resultado:.2f}")
    else:
        print("Operação inválida")
    exit()

except ValueError as e:
    print(f"\nErro: {e}")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")