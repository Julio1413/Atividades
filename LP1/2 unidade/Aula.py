import Professor

class Aula:
    def __init__(self,professor,aluno,horas):
        self.professor = professor
        self.aluno = aluno
        self.horas = horas  

    def calcularValorAula(self):
        if self.professor.valorHora * self.horas <100:
            return 100
        else: return self.professor.valorHora * self.horas


    def calcularDesconto(self, desconto=0.2):
        print(self.calcularValorAula() * (1-desconto))


    def exibir(self):
        print('-'*20)
        print(self.professor.nome)
        print(self.aluno)
        print(self.horas)
        print(self.calcularValorAula())
        print(self.calcularDesconto())
        print('-'*20) 

    
    