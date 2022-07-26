pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22}
outraspessoas = {'nome':'Rodrigo','sexo':'M','idade':26}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#galera = []
#galera.append(pessoas.copy())
#galera.append(outraspessoas.copy())
#for k in pessoas.keys():
 #   print(k)
#for k, v in pessoas.items():
#brasil =[]
#estado1={'uf':'Rio de Janeiro','sigla':'Rj'}
#estado2={'uf':'São Paulo','sigla':'Sp'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0])
#print(brasil[1])
#print(brasil[1]["uf"])

#estado = dict()
#brasil = list()
#for c in range (0,3):
 #   estado['uf'] =str(input('Unidade federativa: '))
  #  estado['sigla'] =str(input('sigla do estado: '))
   # brasil.append(estado.copy())
#for es in brasil:
   # print(es)
 #   for v in es.values():
  #      print(v,end=' ')
   # print()
d = {'b':2,'a':1,'d':4,'c':3}
ordenada = list(d.keys())
ordenada.sort()
for key in ordenada:
    print(key,'=',d[key])