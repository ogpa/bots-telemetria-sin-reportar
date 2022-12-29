string = "PEDRO2WABCqwa-qas123DCXDX"
#c = "x"

# res = string.find(c)
# print(res)


def convertir_placa(alias):
    c = "-"
    pos_guion = alias.find(c)
    if pos_guion != -1:
        placa = alias[pos_guion-3:pos_guion+4]
    else:
        placa = alias
    print(placa)


convertir_placa("PEDRO2WABCqwaqas123DCXDX")
