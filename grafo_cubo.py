import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1,2,3,4,5,6,7,8])

#print(G.nodes())

G.add_weighted_edges_from([(1,2,1+2), (1,4,1+4), (1,8,1+8), (2,3,2+3),(2,7,2+7),(3,4,3+4),
                           (8,7,8+7), (8,5,8+5), (4,5,4+5), (6,7,6+7), (6,3,6+3), (6,5,6+5)])


nx.draw(G, with_labels=True, font_weight='bold')
sp = dict(nx.all_pairs_shortest_path(G))
escolha = raw_input("Escolha o no: ")
if int(escolha) > 0 and int(escolha) <= 8:
    if int(escolha) == 1:
        print "O caminho oposto e 6"
        print sp[1][6]
    if int(escolha) == 2:
        print "O caminho oposto e 5"
        print sp[2][5]
    if int(escolha) ==3:
        print "O caminho oposto e 8"
        print sp[3][8]
    if int(escolha) ==4:
        print "O caminho oposto e 7"
        print sp[4][7]
    if int(escolha) ==5:
        print "O caminho oposto e 2"
        print sp[5][2]
    if int(escolha) ==6:
        print "O caminho oposto e 1"
        print sp[6][1]
    if int(escolha) ==7:
        print "O caminho oposto e 4"
        print sp[7][4]
    if int(escolha) == 8:
        print "O caminho oposto e 3"
        print sp[8][3]
else:
    print "escolha um numero de 1 a 8"

plt.show()