dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0],dados[1])
#listas compostas
pessoas = list()
pessoas.append(dados[:])
pessoas=[['Pedro',25],['Maria',19],['João',32]]
print(pessoas[2][0])
#teste
print('Teste')
teste = list()
teste.append('Gustavo')
teste.append(19)
galera = list()
galera.append(teste[:])# galera.append(teste[:]) <----_desta forma é copia posso mudar apenas uma estrutura de minha escolha
# galera.append(teste)-----> assim é ligaçaõ se eu mudar uma estrutura automaticamente mudo a outra
teste[0]='Maria'
teste[1]=90
galera.append(teste[:])
print(galera)
pessoal = list()
dado = list()
for c in range(0,3):
     dado.append(str(input('Nome: ')))
     dado.append(int(input('Idade: ')))
     pessoal.append(dado[:])
     dado.clear()
for p in pessoal:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade tem {p[1]} anos de idade')
    else:
        print(f'{p[0]} é menor de idade tem {p[1]} anos de idade')
