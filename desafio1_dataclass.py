from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
    notas: list

    def calcular_media(self, indice=0):
        if indice == len(self.notas):
            return 0
        else:
            return self.notas[indice] + self.calcular_media(indice + 1)

    def imprimir_media(self):
        if len(self.notas) == 0:
            return 0
        else:
            media = self.calcular_media() / len(self.notas)
            print(f"Nome: {self.nome}, Média: {media:.2f}")

if  __name__ == "__main__":
    aluno1 = Aluno("Raphael", 39, [9.5, 8.7, 7.2])
    aluno2 = Aluno("Caroline", 30, [6.8, 7.5, 8.9])

    aluno1.imprimir_media()
    aluno2.imprimir_media()
