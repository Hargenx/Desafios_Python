from dataclasses import dataclass
from typing import List

@dataclass
class Aluno:
    nome: str
    idade: int
    notas: List[float]

    def calcular_media(self):
        if not all(isinstance(nota, (int, float)) for nota in self.notas):
            raise ValueError("A lista de notas deve conter apenas números.")
        
        if not self.notas:
            return 0

        return sum(self.notas) / len(self.notas)

    def imprimir_media(self):
        media = self.calcular_media()
        print(f"Nome: {self.nome}, Média: {media:.2f}")

if  __name__ == "__main__":
    aluno1 = Aluno("Raphael", 39, [9.5, 8.7, 7.2])
    aluno2 = Aluno("Caroline", 30, [6.8, 7.5, 8.9])

    aluno1.imprimir_media()
    aluno2.imprimir_media()