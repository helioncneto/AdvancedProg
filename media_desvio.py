# -*- coding: utf-8 -*-

import numpy as np
import scipy.stats

f = open('media_desvio.txt', 'r')
medidas = list()
indices = list()
medidas_dict = dict()

for l in f:
    medidas.append(l.split())
f.close()

for i in range(len(medidas)):
    if i == 0:
        indices.append(medidas[i][0])
        medidas_dict[medidas[i][0]] = list()
        medidas_dict[medidas[i][0]].append(int(medidas[i][1]))
    elif medidas[i][0] not in indices:
        indices.append(medidas[i][0])
        medidas_dict[medidas[i][0]] = list()
        medidas_dict[medidas[i][0]].append(int(medidas[i][1]))
    else:
        medidas_dict[medidas[i][0]].append(int(medidas[i][1]))

arq = open('md', 'w')
for k in medidas_dict.keys():
    media = str(sum(medidas_dict[k])/len(medidas_dict[k]))
    desvio_padrao = np.std(np.array(medidas_dict[k]))
    Z_alpha = 1.96
    conf_int = (Z_alpha * desvio_padrao) / np.sqrt(len(medidas_dict[k]))
    #print conf_int
    arq.write(k + ' ' + media + ' ' + "%.2f" % conf_int )
    arq.write('\n')
arq.close()