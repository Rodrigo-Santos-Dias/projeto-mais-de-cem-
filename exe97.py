def area(largura,comprimento):
    area_do_terreno = largura*comprimento
    print(f'A área de um  terreno {largura} X {comprimento} é de {area_do_terreno}m')


largura = float(input('LARGURA(m)'))
comprimento = float(input('COMPRIMENTO(m)'))

area(largura, comprimento)
