elemento = {
    'z': 3,
    'nome': 'litio',
    'grupo': 'metais'
}

print(f'Elemto: {elemento['nome']}')

#atualizar
elemento['grupo' ] = 'alcalinos'
print(elemento)

#add 9elemento ['periodo'] = 1
print(elemento)

#tirar
del elemento['periodo']
print(elemento)

#limpar 
elemento.clear()
print(elemento)

#deletar da memoria
del elemento