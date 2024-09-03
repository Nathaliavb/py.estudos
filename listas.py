# n1 = [5,6,7,8,9]
# n2 = [3,6,7,0,3,4,6]
# valores = n1 + n2
# print (len(valores))
# print(7 in valores)

# planetas = ['mercurio', 'terra', 'marte']
# for nomes in planetas:
#   print(nomes)

# bebidas = [] 

# for i in range(5):
#     print('Digite uma bebida favorita:')
#     bebida = input ()
#     bebidas.append(bebida)

# bebidas.sort()
# print(f'bebidas escolhidas:')
# for bebide in bebidas:
#   print(bebide)

# lista = []

# for lis in range (4):
#     print('Adicione um item a lista:')
#     list = input()
#     lista.append(list)

# print(f'Essa é sua lista ate agora: {lista}')



lista = []

def adicionar_itens(lista, quantidade):
    for i in range(quantidade):
        print('Adicione um item à lista:')
        item = input()
        lista.append(item)
    print(f'Essa é sua lista até agora: {lista}')


adicionar_itens(lista, 4)

while True:
    resposta = input("Deseja adicionar mais 4 itens à lista? (sim/não): ").strip().lower()
    if resposta == "sim":
        adicionar_itens(lista, 4)
    elif resposta == "não":
        print("Lista encerrada.")
        break
    else:
        print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")

print(f'Lista final: {lista}')



  