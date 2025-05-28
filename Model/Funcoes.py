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
    
    
    def calcular_expressoes(self, expressao):
    
        try:
            if "+" in expressao:
                partes_numericas =  expressao.split("+")
                return self.soma(float(partes_numericas[0], partes_numericas[1]))
            elif "-" in expressao:
                partes_numericas =  expressao.split("-")
                return self.subtrair(float(partes_numericas[0], partes_numericas[1]))
            elif "*" in expressao:
                partes_numericas =  expressao.split("*")
                return self.multiplicar(float(partes_numericas[0], partes_numericas[1]))
            elif "//" in expressao:
                partes_numericas =  expressao.split("//")
                return self.dividir(float(partes_numericas[0], partes_numericas[1]))
            else:
                print(F"Erro nos operaddores")
            
        except ValueError:
            return "Erro: Digite números válidos!"
        except ZeroDivisionError:
         return "Erro: Divisão por zero!"
        except Exception as e:
         # Log para desenvolvedor 
         print(f"Erro interno: {str(e)}")  # Isso pode ser registrado em um log
         return "Erro: Ocorreu um problema inesperado"
        