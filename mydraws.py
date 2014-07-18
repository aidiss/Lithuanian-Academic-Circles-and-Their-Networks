#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import itertools
from classifications import *
pd.options.display.mpl_style = 'default'


# Draws all branches of a field.
def draw_field_history(df, 
                       daktar=True, habil=True,
                       sritis=None, kryptis=None,
                       tarpsnis=['1940','2100'], 
                       KIND='line', figsize=(13,7)):

    condition_dict = {}

    if sritis != None:
        condition_dict['sritis'] = df['dkt_dsc'].str.contains(sritis, na=False)
    if kryptis != None:
        temp = df['dkt_dsc'].str.contains(kryptis, na=False) 
        condition_dict['kryptis'] = temp
        
    if tarpsnis != None:
        pass
        #condition_dict['gyn_lks'] = df['gyn_lks'].isin(['1940':'2100'])        
    if habil == False:
        condition_dict['dkt_lps'] = df['dkt_lps'] == 'Habilituotas daktaras'
    if daktar == False:
        condition_dict['dkt_lps'] = df['dkt_lps'] == 'Daktaras'

    plt.figure(1, figsize=(13,7))
    
    for kryptiss in kryptis.split('|'):
        fltrd = df[condition_dict['sritis']]
        fltrd = df[df['dkt_dsc'].str.contains(kryptiss, na=False)]
        fltrd = fltrd[fltrd['gyn_lks'] >= tarpsnis[0]]
        fltrd = fltrd[fltrd['gyn_lks'] <= tarpsnis[1]]
        grpd = fltrd.groupby(fltrd['gyn_lks'].map(lambda x: x.year)).size()
        KODAS = '{}{}'.format(kryptiss, sritis)
        PAVADINIMAS = code_to_name[KODAS]
        LABEL = ' '.join([PAVADINIMAS, KODAS])
        plt.plot(grpd.index, 
                 grpd.values, 
                 label=LABEL, 
                 linewidth=4,
                 alpha=0.75)
    
        #df[condition_dict['sritis']]
    df = df[df['gyn_lks'] >= tarpsnis[0]]
    df = df[df['gyn_lks'] <= tarpsnis[1]]
    df = df.groupby(df['gyn_lks'].map(lambda x: x.year)).size()
    LABEL = "VISO"
    plt.plot(df.index, 
             df.values / float(len(kryptis.split('|'))), 
             label=LABEL,
             c='k',
             linewidth=4,
             alpha=0.75)

    plt.xlabel(u'Metai')
    plt.ylabel(u'Gynimų sk')
    plt.title(u'{} srities disertacijų gynimai pagal metus'.format(sritis))
    plt.legend(loc=2)
    plt.show()
    
    
    
#Deprecated
# This is the alternative way of drawing the main timeline
def draw_history2(df):
    crazylist = [df[df['dkt_dsc'].str.contains(x, na=False)].groupby(df['gyn_lks'].map(lambda x: x.year)).size() 
                 for x in ['H', 'S', 'P', 'T', 'B']]
    dfplot = pd.DataFrame(crazylist, index=['H', 'S', 'P', 'T', 'B'])
    #dfplot = dfplot.dropna(axis=1) #This makes some erros
    dfplot = dfplot.fillna(0) # But this does not look very nice, I have to fix axes.
    dfplot.T.plot(kind='line',linewidth=3,alpha=0.5,figsize=(13,7))
    dfplot
    
    plt.show()


#Deprecated
def draw_history(df):
    plt.figure(1, figsize=(13,7))
    for x in ['H','S','P','T','B']:
        plt.subplot(111)
        fltrd = df[df['dkt_dsc'].str.contains(x, na=False)]
        grpd = fltrd.groupby(fltrd['gyn_lks'].map(lambda x: x.year)).size()
        plt.plot(grpd.index, grpd.values,label='{}'.format(x),linewidth=4,alpha=0.7)
    
    #plot(df.groupby(df['data_lks'].map(lambda x: x.year)).size())

    plt.xlabel(u'Metai')
    plt.ylabel(u'Gynimų sk')
    plt.title(u'Disertacijų gynimai pagal metus')

    plt.legend(loc=2) #bbox_to_anchor=(0., 1.02, 1., .102) , ncol=1 , mode="expand"

    #plt.axis([1940, 2014, 0, 500])
    plt.grid(True)
    plt.show()


def draw_classification(G, 
                        layout='spring', 
                        SRITYS = [u'Humanitariniai mokslai', u'Socialiniai mokslai', 
              u'Biomedicinos mokslai', u'Fiziniai mokslai', 
              u'Technologijos mokslai', u'Žemės ūkio mokslai'], 
                        kryptys=None,
                        sakos=True,
                        K=0.2):
    plt.figure(figsize=(15, 15))
    plt.title(u'Klasifikacija')
    
    nbunch = [z[0] for z in G.nodes(data=True) if (z[1][u'sritis'] in SRITYS) or (z[1][u'sritis'] == '')]
    G.remove_nodes_from([ n for n in G if n not in set(nbunch)])
    G.remove_nodes_from([ n for n in G if  len([x for x in nx.all_neighbors(G, n)]) == 0]) 
    if layout == 'spring':
        pos = nx.spring_layout(G,k=K, iterations=100)
    if layout == 'spectral':
        pos = nx.spectral_layout(G, dim=2, weight='weight', scale=1)


    #SAKOS
    nx.draw_networkx_nodes(G,
                           pos,
                           #nodelist=G.nodes()[5:-1],
                           nodelist=[z[0] for z in G.nodes(data=True) if z[1][u'sritis'] == ''],
                           node_color='k',
                           node_shape='s',
                           node_size=100,
                           alpha=0.5)

    count = -1
    for x in SRITYS:
        count += 1
        COLORS = ['r', 'b', 'g', 'c', 'm', 'y', 'k']
        NODELIST = [z[0] for z in G.nodes(data=True) 
                    if z[1][u'sritis'] != u'' and z[1][u'sritis'] == x]
        nx.draw_networkx_nodes(G,
                               pos,
                               #nodelist=G.nodes()[5:-1],
                               nodelist=NODELIST,
                               node_color=COLORS[count], #fak_colors[x],
                               node_shape='s', #so^>v<dph8
                               node_size=500,
                               alpha=0.25)

    nx.draw_networkx_edges(G,
                            pos,
             #               edgelist=G.edges(),
                            edgelist = [(u,v,d) for u,v,d in G.edges(data=True)],
                            width=1,
                            alpha=0.1,
                            weight=1,
                            edge_color='k')

    nx.draw_networkx_labels(G, 
                                pos, 
                                labels=None, 
                                font_size=12, 
                                font_color='k', 
                                font_family='sans-serif', 
                                font_weight='normal', 
                                alpha=0.6, 
                                ax=None)
    plt.grid(False)
    plt.show()


##########
#NARIAI DSC GRAFUI

def complete_graph_from_list(L, create_using=None):
    G=nx.empty_graph(len(L),create_using)
    if len(L)>1:
        if G.is_directed():
            edges=itertools.permutations(L,2)
        else:
            edges=itertools.combinations(L,2)
        G.add_edges_from(edges)
    return G


def draw_sritys_sakos(df):
    df['mokslo_saka_kodas'] = df.mokslo_saka.str.extract('([HSPTBA] ?\d{3})')
    df['mokslo_saka_kodas'] = df['mokslo_saka_kodas'].str.strip(' ')
    df['mokslo_saka_kodas'].replace(' ','', inplace=True, regex=True)
    rez = df[~df.mokslo_saka_kodas.isnull()].loc[:,['dkt_dsc','mokslo_saka_kodas']].values

    plt.figure()
    G = nx.MultiGraph()
    pos=nx.spring_layout(G, dim=2, k=0.25, scale=10, iterations=1000)
    G.add_edges_from([(x[0],x[1]) for x in rez])
    nx.draw(G)

    plt.figure()
    G = nx.MultiDiGraph()
    pos=nx.spring_layout(G, dim=2, k=0.25, scale=10, iterations=1000)
    G.add_edges_from([(x[1],x[0]) for x in rez])
    nx.draw(G)

    plt.figure()
    G = nx.MultiDiGraph()
    pos=nx.spring_layout(G, dim=2, k=0.25, scale=10, iterations=1000)
    G.add_edges_from([(x[0],x[1]) for x in rez])
    nx.draw(G)
