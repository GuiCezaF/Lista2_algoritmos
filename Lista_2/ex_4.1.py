'''
    Expanda a tabela de senos e cossenos para incluir também a tangente,
    usando a função math.tan().
    Cuidado! Você tem de se preocupar com as tangentes de 90 e 270 graus.
    Por quê? Trate estes casos especiais, evitando incorrer em erro.
    Use math.inf e -math.inf para indicar valores infinitos,
    positivos e negativos.
'''

import math

print('{:>9}{:>9}{:>9}{:>9}{:>9}'.format(
    'Graus', 'Radianos', 'Seno', 'Cosseno', 'Tangente'))

for graus in range(0, 361, 30):
    rad = math.radians(graus)
    seno = math.sin(rad)
    cosseno = math.cos(rad)

    if graus == 90:
        tan = math.inf

    elif graus == 270:
        tan = -math.inf
    else:
        tan = math.tan(rad)

    print('{:>9.2f}{:>9.2f}{:>9.2f}{:>9.2f}{:>9.2f}'.format(
        graus, rad, seno, cosseno, tan))
