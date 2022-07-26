def notas(*n,sit=False ):
    dados = list()
    for c in n:
        dados.append(c)
    dicio = dict()
    totnotas = maior = menor= media= 0
    for pos,i in enumerate(dados):
        totnotas+=1
        media += i
        if pos == 0:
            maior= menor = i
        else:
            if i >maior:
                maior = i
            if i < menor:
                menor = i
    media /= totnotas
    dicio["total"] = totnotas
    dicio["maior"]= maior
    dicio["menor"] = menor
    dicio["media"] = media
    if sit == True:
        if dicio["media"] <5:
            dicio["situação"] = "Ruim"
        if dicio["media"]>=5<=6.9:
            dicio["situação"] = "Razoavel"
        if dicio["media"] >= 7:
            dicio["situação"] = "Boa"
    print(dicio)


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
#print(resp)

