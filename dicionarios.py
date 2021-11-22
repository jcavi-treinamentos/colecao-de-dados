## Dicionário não possui noção de indices.
# E não pode ser fatiado em indices
# Dicionario é mutavel pode adicionar ou remover elementos

dicionario = {'chave':'valor'}

## Exemplo de dicionario

estados_siglas = {

    "SC":"Santa Catarina",
    "PR":"Parana",
    "RS":"Rio Grande do Sul",
    "SP": "São Paulo",

}

print(estados_siglas)

for uf in estados_siglas.items():
    print(uf)


