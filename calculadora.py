from unittest import TestCase, main, result
import abc


class Calculadora(object):
    def calcular(self, val1, val2, operator):
        operatorFabrica = OperatorFabrica()

        operator = operatorFabrica.criar(operator)

        if operator == None:
            return 0
        else:
            result = operator.execucao(val1, val2)

            return result



class OperatorFabrica(object):
    def criar(self, operator):
        if operator == 'somar':
            return Soma()
        elif operator == 'subtrair':
            return Subtracao()
        elif operator == 'dividir':
            return Divisao()
        elif operator == 'multiplicar':
            return Multiplicacao()



class Operator(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def execucao(self, val1, val2):
        pass



class Soma(Operator):
        def execucao(self, val1, val2):
            result = val1 + val2

            return result



class Subtracao(Operator):
    def execucao(self, val1, val2):
        result = val1 - val2

        return result



class Divisao(Operator):
    def execucao(self, val1, val2):
        result = val1 / val2

        return result



class Multiplicacao(Operator):
    def execucao(self, val1, val2):
        result = val1 * val2

        return result



class Testador(TestCase):
    def testarSoma(self):
        calculadora = Calculadora()

        result = calculadora.calcular(5, 7, 'somar')

        self.assertEqual(result, 12)
    

    def testarSubtracao(self):
        calculadora = Calculadora()

        result = calculadora.calcular(8, 5, 'subtrair')

        self.assertEqual(result, 3)
            
            
    def testarMultiplicacao(self):
        calculadora = Calculadora()

        result = calculadora.calcular(5, 5, 'multiplicar')

        self.assertEqual(result, 25)
                
            
    def testarDivisao(self):
        calculadora = Calculadora()

        result = calculadora.calcular(15, 3, 'dividir')

        self.assertEqual(result, 5)



chamarTeste = Calculadora()

testarSoma = chamarTeste.calcular(2, 5, 'somar')
testarSubtracao = chamarTeste.calcular(7, 5, 'subtrair')
testarMultiplicacao = chamarTeste.calcular(6, 4, 'multiplicar')
testarDivisao = chamarTeste.calcular(12, 6, 'dividir')

print(testarSoma)
print(testarSubtracao)
print(testarMultiplicacao)
print(testarDivisao)

if __name__ == '__main__':
    main()