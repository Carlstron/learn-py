import os
import json

PATH_FILE = '.\movendo_instancias_por_json\Pessoa.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Jim', 23)

with open(PATH_FILE, 'w', encoding='utf8') as file:
    json.dump(vars(p1), file, indent=2)
