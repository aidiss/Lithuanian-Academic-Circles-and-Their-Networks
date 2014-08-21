#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pieski.py


#Problem with MultiDiGraph

def pieskiGrafa(G, 
                colordict=None, 
                nodePass=3, 
                nsize=None, 
                ncolor=None, 
                nmarker=None, 
                ecolor=None, 
                ewidth=None):
    '''This function draw a graph object'''
    import networkx as nx
    import matplotlib.pyplot as plt
    
    G.remove_nodes_from([z for z in G.nodes() if G.degree(z) < nodePass]) #  and GG.out_degree(z) > 5
    
    inv_smm2011 = colordict
    plt.figure(figsize=(15, 15))
    plt.title(u'Tarpkryptiškumas disertacijų gynimuose')
    pos=nx.spring_layout(G, iterations=10000, k=None,weight=0.5)

    COLORS = ['r', 'g', 'b', 'c', 'y', 'm']
    discList = ['H', 'S', 'P', 'B', 'T', 'A']
       
    count = -1    
    for x in discList:
        count += 1
        nx.draw_networkx_nodes(G,
                               pos,
                               nodelist=[n for n in G.nodes() if x in inv_smm2011[n]],
                               node_color=COLORS[count], #fak_colors[x],
                               node_shape='o', #so^>v<dph8
                               node_size=[data['disertaciju'] * 20 for n, data in G.nodes_iter(data=True) if x in inv_smm2011[n]],
                               alpha=0.2)
                               
    count = -1    
    for x in discList:
        count += 1
        nx.draw_networkx_nodes(G,
                               pos,
                               nodelist=[n for n in G.nodes() if x in inv_smm2011[n]],
                               node_color=COLORS[count], #fak_colors[x],
                               node_shape='o', #so^>v<dph8
                               node_size=[data['keliuoseGynimuoseBuvo'] * 2  for n, data in G.nodes_iter(data=True) if x in inv_smm2011[n]],
                               alpha=0.5)

    nx.draw_networkx_edges(G,
                           pos,
             #             edgelist=G.edges(),
                           edgelist = [(u,v,d) for u,v,d in G.edges(data=True)],
                           width= [d['weight'] / float(2) for u,v,d in G.edges(data=True)],
                           alpha=0.05,
                           weight=1,
                           edge_color='k')

    nx.draw_networkx_labels(G, 
                            pos, 
                            labels={n:str(n).decode('unicode-escape') for n in G.nodes()},  #.decode('escape')
                            font_size=12, 
                            font_color='k', 
                            font_family='sans-serif',#  fantasy cursive serif serif-sans monospace
                            font_weight='normal', 
                            alpha=0.6, 
                            ax=None)
    plt.savefig("Graphs\pirmasgraphas.png", bbox_inches="tight")
    plt.grid(False)
    plt.show()

def introToMethod(df, nr, kind=1, write=False):
    import Graph
    import networkx as nx
    import pandas as pd
    import matplotlib.pyplot as plt
    from unidecode import unidecode
    
    SG = Graph.GraphOneDefenceByNames(nr, df, kind=1, directed=False, mixed=False)
    pos=nx.circular_layout(SG)
    plt.figure(figsize=(4,4))
    plt.grid(False)
    plt.axis('off')
    if kind == 1:
        nx.draw_networkx_nodes(SG, pos)
        nx.draw_networkx_labels(SG, pos, labels = {n:unidecode(str(n).decode('utf-8')) for n in SG.nodes()})
        nx.draw_networkx_edges(SG, pos)
        if write == True:
            plt.savefig('MethodFigure{}.png'.format(kind), box_inches='tight')
        plt.show()
        
    if kind == 2:
        SG = Graph.GraphOneDefenceByNames(nr, df, kind=2, directed=False, mixed=False)
        nx.draw_networkx_nodes(SG, pos)
        nx.draw_networkx_labels(SG, pos, labels = {n:unidecode(str(n).decode('utf-8')) for n in SG.nodes()})
        nx.draw_networkx_edges(SG, pos)
        if write == True:
            plt.savefig('MethodFigure{}.png'.format(kind), box_inches='tight')
        plt.show()
    
    if kind == 3:
        SG = Graph.GraphOneDefenceByNames(nr, df, kind=2, directed=True, mixed=False)
        nx.draw_networkx_nodes(SG, pos)
        nx.draw_networkx_labels(SG, pos, labels = {n:unidecode(str(n).decode('utf-8')) for n in SG.nodes()})
        nx.draw_networkx_edges(SG, pos)
        if write == True:
            plt.savefig('MethodFigure{}.png'.format(kind), box_inches='tight')
        plt.show()
        
    if kind == 4:
        SG = Graph.GraphOneDefenceByNames(nr, df, kind=7, directed=True, mixed=False)
        nx.draw_networkx_nodes(SG, pos)
        nx.draw_networkx_labels(SG, pos, labels = {n:unidecode(str(n).decode('utf-8')) for n in SG.nodes()})
        nx.draw_networkx_edges(SG, pos)
        if write == True:
            plt.savefig('MethodFigure{}.png'.format(kind), box_inches='tight')
        plt.show()
