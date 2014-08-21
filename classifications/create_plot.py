# -*- coding: utf-8 -*-
"""
this module creates all kinds plots.
In most cases it accepts g object as first argument followed up by some
others

Example:

create_plot1(G)

module level variables: there are none

Dependencies:
matplotlib.pyplot
"""

import matplotlib.pyplot as plt
import networkx as nx
from get_color import *
from flatten_graph import flatten_graph

def create_plot1(g, df=None, dedirect=False, flatten=False, edgelabels = True, 
          nodelabels=True, fsize=None, K=None, save=False):
                  
    """Creates a graph from a figure   
    returns/shows a figure.
    
    Args:
    g - (networkx graph object)
    df - pandas dataframe object. Default is None
    dedirect - converts networkx DiGraph to Graph. Default is False
    flatten - manipultes a graph by replacing nodes that have only two 
    edges with straighforward edge. Also, groups these kind of edges if
    it is possible
    
    
    edgelabels . Default is None
    nodelables . Default is None
    fsize
    K
    Save
    
    Returns:
    matplotlib figure
    
    """
    
    if dedirect==True:
        g = nx.Graph(g)
        
    if fsize != None:
        plt.figure(1, figsize=fsize)
    pos = nx.spring_layout(g, dim=2, scale=1)
    
    if flatten == True:
        g = flatten_graph(g)
        pos = nx.spring_layout(g, dim=2, scale=1)
    
    pos = nx.spring_layout(g, dim=2, scale=10, k=K)
    
    node_colors = get_node_colors(g.nodes(), df)
    nx.draw_networkx_nodes(g, pos, alpha=0.3, node_size=300, node_color=node_colors)
    
    edge_colors = get_edge_colors(g.edges(), df)
    nx.draw_networkx_edges(g, pos, alpha=0.1, edge_color='b')
    
    if nodelabels == True:
        nx.draw_networkx_labels(g, pos)
        
    if edgelabels == True:
        nx.draw_networkx_edge_labels(g, pos)
        
    if save == True:
        mpld3.save_html(figure(1), 'graph.html')
        
    return plt.figure(1)

def create_plot(G, sritys, layout='spring', K=0.2, 
                        dedirect=False, sritdraw=True, reverse=False):
    """
    A Graph object
    
    Arguments:
    sritys - a string that consist of one or any number of letters 
    representing different fields 'hmptba'
    layout - networkx layout
    K - networkx K value
    dedirect = forces graph to be converted to a graph
    sridraw - does something
    revers - reverses a graph for a different kind of plot
    
    returns:
    nothing. But shows a figure.
    """
    
    plt.figure(figsize=(10, 10))
    outdeg = G.out_degree()
    outdeg = G.in_degree()

    SRITYS = [x.upper() for x in sritys]
    
    if sritdraw == True:
        to_keep = [z[0] for z in G.nodes(data=True) if z[1]['srtkds'] in SRITYS]
        THELIST = []
        for h in to_keep:
            LALA = G.neighbors(h)
            THELIST.extend(LALA)
        to_keep.extend(THELIST)
        G = G.subgraph(to_keep)
        
    if layout == 'spring':
        pos = nx.spring_layout(G, k=K, iterations=1000)
        
    if layout == 'spectral':
        pos = nx.spectral_layout(G, dim=2, weight='weight', scale=1)
        
    count = -1
    count += 1
    COLORS = ['r', 'b', 'g', 'c', 'm', 'y', 'k']
    SKSLIST = [z[0] for z in G.nodes(data=True) if z[1]['tipas'] == u'saka']
    KRPLIST = [z[0] for z in G.nodes(data=True) if z[1]['tipas'] == u'kryptis']
    
    if dedirect == True:
        G = nx.Graph(G)
    if reverse == True:
        G = nx.reverse(G)

    nx.draw_networkx_nodes(G,
                           pos,
                           #nodelist=G.nodes()[5:-1],
                           nodelist= SKSLIST,
                           node_color= 'k', #fak_colors[x],
                           node_shape= 's', #so^>v<dph8
                           node_size= 200,
                           alpha=0.1)

    nx.draw_networkx_nodes(G,
                           pos,
                           #nodelist=G.nodes()[5:-1],
                           nodelist=KRPLIST,
                           node_color=COLORS[1], #fak_colors[x],
                           node_shape='s', #so^>v<dph8
                           node_size=500,
                           alpha=0.25)

    nx.draw_networkx_edges(G,
                           pos,
                           edgelist=G.edges(),
                           # edgelist = [(u,v,d) for u,v,d in G.edges(data=True)],
                            width=1,
                            alpha=0.1,
                           # weight=1,
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


    plt.title(u'2011 m Šmm Klasifikacijos tarpdiscipliniškumas')
    plt.grid(False)
    return plt.figure(1) 
