import copy
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = copy.deepcopy(produtos)

novos_produtos = [
    {**produto, 'preco': round(produto['preco']*1.1,2)}
    for produto in copy.deepcopy(produtos)
]

print(*novos_produtos, sep='\n')
print()

produtos_ordenados_por_nome = copy.deepcopy(produtos)

produtos_ordenados_por_nome.sort(key=lambda p: p['nome'], reverse=True)
print(*produtos_ordenados_por_nome, sep='\n')
print()

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
    )

print(*produtos_ordenados_por_preco, sep='\n')
print()
print(*produtos, sep='\n')