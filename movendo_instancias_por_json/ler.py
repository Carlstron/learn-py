import os
import json
from salvar import Pessoa, PATH_FILE


with open(PATH_FILE, 'r', encoding='utf8') as file:
    p1 = Pessoa(**json.load(file,))

print(vars(p1))