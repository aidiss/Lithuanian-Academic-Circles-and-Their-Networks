#!/usr/bin/env python
# -*- coding: utf-8 -*-

mydict = {}
for index, row in df.iterrows():
    one = row[0]
    two = tuple(set([x for x in row[1:8].values if x]))
    thr = len(two)
    mydict[index] = [one, two, thr]
pd.DataFrame(mydict).T.groupby(2).size().plot(kind='bar', figsize=(3,2))
#plt.pie(pd.DataFrame(mydict).T.groupby(2).size())




# About edges
def genDijkstraPath(G):
    ''' Generates DijkstraPath between two nodes'''
    mydict = {}
    for N1 in G.nodes():
        mydict[N1] = {}
        for N2 in G.nodes():
            mydict[N1][N2] = nx.dijkstra_path(G,N1,N2)
    return mydict




rez =[[x, nx.average_clustering(GL[0], nodes=x, weight='weight')] for x in nx.find_cliques(GL[0])] #not for directed # perziureti ju vidutinius svorius
import operator
sorted(rez, key=operator.itemgetter(1))



coms = [x for x in nx.k_clique_communities(GG,5)] # perziureti vidutini svori



#df[df.prm_dsc.str.contains('11B|12B|13B|14B', na=False)] #paskutinis 10-12-02
#df[df.dkt_dsc.str.contains('11B|12B|13B|14B', na=False)] #nėra
#df[df.prm_dsc.str.contains('01A|02A|03A|04A', na=False)] #nuo 2011-09-16
#df[df.dkt_dsc.str.contains('01A|02A|03A|04A', na=False)] #Keistas reikalas

#[x for x in df if ['05H', '05P', '05H', '05H'] in df.nar_dsc]



# Pabandykime gauti informacija apie gynimus, kurie peržengė didžiąją ribą.
dF = df[df.dkt_dsc.str.contains('|'.join(dsc_list), na=False) & df.vdv_dsc.str.contains('|'.join(dsc_list), na=False)]
dF = dF[dF.dkt_dsc.str.contains('S|H', na=False) & dF.vdv_dsc.str.contains('\d{2}[PTBA]', na=False)]
dF.loc[:,['tema','dkt_dsc','vdv_dsc']]

#Gauname Įdomius atvejus = http://www.lmt.lt/lt/paslaugos/disertacijos/d-db/1329/p0.html
#http://www.lmt.lt/lt/paslaugos/disertacijos/d-db/2724/p0.html arba2723
#Bugas, netinkamai atpažintas vadovas ir mokslinis konsultantas: http://www.lmt.lt/lt/paslaugos/disertacijos/d-db/3511/p0.html arba 3510



[nx.transitivity(x) for x in GL]



import mpld3
mpld3.enable_notebook()

def KazkoksPiesiimas(G, write=False):

    G = nx.Graph()
    graphs = []
    for x in prep:
        if x:
            REQ = list(set(x))
            M = complete_graph_from_list_alt(REQ)

            for u,v,data in M.edges_iter(data=True):
                #w = data['weight']
                if G.has_edge(u,v) == False:
                    G.add_edge(u, v, weight=1)
                    G[u][v]['weight']=1
                else:

                    G[u][v]['weight'] += 1

    colors ={'red':{'a':0.7,'r':255,'g':0,'b':0},
             'orange':{'a':0.7,'r':255,'g':69,'b':0},
             'yellow':{'a':0.7,'r':255,'g':215,'b':0},
             'green':{'a':0.7,'r':34,'g':139,'b':34},
             'blue':{'a':0.7,'r':65,'g':105,'b':225},
             'purple':{'a':0.7,'r':157,'g':112,'b':219}}

    srit_to_col ={'H':colors['red'],
                  'S':colors['orange'],
                  'P':colors['yellow'],
                  'T':colors['green'],
                  'B':colors['blue'],
                  'A':colors['purple']}                

    for u, data in G.nodes_iter(data=True):
        G.node[u]['viz'] = {}
        G.node[u]['viz']['color'] = {}
        for x in srit_to_col.keys():
            if x in u:
                G.node[u]['viz']['color'] = srit_to_col[x]
        G.node[u]['viz']['size']= 2.0375757

    for x in G.nodes():
        G.node[x]['label']=code_to_name[x] #.decode('utf-8')
    #print G.nodes(data=True)
    print G

    plt.figure(figsize=(15, 15))
    plt.title('TITLE')
    pos = nx.spring_layout(G, dim=2, k=0.25, scale=10, iterations=1000)

    count = -1
    for x in ['H','S','T','P','A','B']:
        count += 1
        COLORS = ['r','g','b','c','y','m']
        nx.draw_networkx_nodes(G,
                               pos,
                               nodelist=[n for n in G.nodes() if x in n],
                               node_color=COLORS[count], #fak_colors[x],
                               node_shape='o', #so^>v<dph8
                               node_size=500,
                               alpha=0.2)

    nx.draw_networkx_edges(G,
                           pos,
                           # edgelist=G.edges(),
                           edgelist = [(u,v,d) for u,v,d in G.edges(data=True)],
                           width=[d['weight']/float(2) for u,v,d in G.edges(data=True)],
                           alpha=0.1,
                           edge_color='k')

    nx.draw_networkx_labels(G, 
                            pos, 
                            labels={n:code_to_name[n] for n in G.nodes()},  #.decode('escape')
                            font_size=12, 
                            font_color='k', 
                            font_family='sans-serif',#  fantasy cursive serif serif-sans monospace
                            font_weight='normal', 
                            alpha=0.6, 
                            ax=None)
    plt.grid(False)
    plt.show()
    if write=True:
        nx.write_gexf(G, 'nariai_dsc1.gexf')



# Doktorantas ir pirmininkas
res = df[(df.dkt_dsc.str.contains(pattern, na=False) & df.prm_dsc.str.contains(pattern, na=False))
         & (df.dkt_dsc != df.prm_dsc)]
print len(res), "atvejų, kai nesutampa doktoranto ir komisijos pirmininko kryptys"
subset = res[['dkt_dsc', 'prm_dsc']]
tuples_dict[0] = [tuple(x) for x in subset.values]


# Doktorantas ir vadovas
dkt_vdv = df[(df.dkt_dsc.str.contains(pattern, na=False) & df.vdv_dsc.str.contains(pattern, na=False))
         & (df.dkt_dsc != df.vdv_dsc)]
print len(res), "atvejų, kai nesutampa doktoranto ir vadovo kryptys"

subset = res[['dkt_dsc', 'vdv_dsc']]
tuples_dict[1] = [tuple(x) for x in subset.values]


# Pirmininkas ir vadovas
res = df[(df.prm_dsc.str.contains(pattern, na=False) & df.vdv_dsc.str.contains(pattern, na=False))
         & (df.prm_dsc != df.vdv_dsc)]
print len(res), "atvejų, kai nesutampa komisijos pirmininko ir vadovo kryptys"

subset = res[['prm_dsc', 'vdv_dsc']]
tuples_dict[2] = [tuple(x) for x in subset.values]


# Visos trys salys

rez = df[(df.dkt_dsc.str.contains(pattern, na=False) & df.prm_dsc.str.contains(pattern, na=False) & df.vdv_dsc.str.contains(pattern, na=False))
         & ((df.dkt_dsc != df.prm_dsc) & (df.dkt_dsc != df.vdv_dsc)&  (df.vdv_dsc != df.prm_dsc))]
         

#& df.prm_dsc.str.contains(pattern, na=False) & df.vdv_dsc.str.contains(pattern, na=False))
       #  & ((df.dkt_dsc != df.prm_dsc) & (df.dkt_dsc != df.vdv_dsc)&  (df.vdv_dsc != df.prm_dsc))]

# kkai nesutampa visos trys
#set(tuples_dict[0]) - set(tuples_dict[1]), set(tuples_dict[1]) - set(tuples_dict[2]), set(tuples_dict[2]) - set(tuples_dict[0])

import networkx as nx
G=nx.MultiDiGraph()
G.add_edges_from(tuples_dict[0])


#Slėpti

def kazinkKoksGrafas(G):
    plt.figure(figsize=(5, 5))
    plt.title('TITLE')
    pos=nx.spring_layout(G, iterations=100, k=0.1)

    count = -1
    for x in ['H','S','T','P','A','B']:
        count += 1
        COLORS = ['r','g','b','c','y','m']
        nx.draw_networkx_nodes(G,
                               pos,
                                nodelist=[z for z in G.nodes() if x in z],
                                node_color=COLORS[count], #fak_colors[x],
                                node_shape='o', #so^>v<dph8
                                node_size=500,
                                alpha=0.2)

    nx.draw_networkx_edges(G,
                            pos,
             #               edgelist=G.edges(),
                            edgelist = [(u,v,d) for u,v,d in G.edges(data=True)],
                            width=2,
                            alpha=0.2,
                            weight=1,
                            edge_color='k')
    '''
    nx.draw_networkx_labels(G, 
                                pos, 
                                labels=None, 
                                font_size=10, 
                                font_color='k', 
                                font_family='sans-serif', 
                                font_weight='normal', 
                                alpha=0.6, 
                                ax=None)
    '''
    plt.show()




įdomu, ar komisijos vadovo kryptis visada atitinka komisijos narių daugumos kryptį?)
(įdomus ryšys, spėju, jog vadovas turėtų atitikti doktoranto kryptį. Aišku, gali būti kad vadovai yra priskiriami ne pagal turimą laipsnį, bet pagal vėliau keičiama kryptį. Manau šiais atvejais galime įtarti, jog vadovas dirbo kita linke. Kad tai nėra jaunas vadovas.)


Radome keletą įdomių šakų: *idomios mokslo sakos = ['S189','H593','H280','S170','S216']
*idomios mokslo kryptys = [04H 05S 03S 03p 01H 05H 09P 02P 03H]




# highlight_path='medicina'
if highlight_path != None:
    nodesToHighlight = []
    edgesToHighlight = []
    for path in nx.all_pairs_dijkstra_path(G):
        if highlight_path in path:
            nodesToHighlight.append[path]  # These nodes will have to be highlighted
            # edgesToHighlight.append[path]  # These nodes will have to be highlighted
