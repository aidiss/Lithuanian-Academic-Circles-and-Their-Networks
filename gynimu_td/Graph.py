#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Includes three functions:
# GraphOneDefenceByNames
# GraphOneDefenceByCodes
# sudekiGraphys

import networkx as nx
import pandas as pd
import numpy as np

def GraphOneDefenceByNames(nr, df, kind=1, directed=False, mixed=False): # 2014-07-30
    '''This function composes a minigraph of each defence.
    It contains 8 types of drawing. 
    However, directed and mixed kwargs sometimes enforce different behaviour'''
    
    def validity_check():
        ''' should look into things'''
        pass
    
    dict = {}
    
    dkt = [df.T[nr]['dkt_dsc_pav']]
    vdv = [df.T[nr]['vdv_dsc_pav']]
    prm = [df.T[nr]['prm_dsc_pav']]
    nar = [df.T[nr][1],df.T[nr][2],df.T[nr][3],df.T[nr][4]]
    #opn = [df.T[nr]['opn_dsc_pav']]
    opn1 = [df.T[nr]['opn1_dsc_pav']]
    opn2 = [df.T[nr]['opn2_dsc_pav']]
    #Bug
    visi = [dkt, vdv, prm, nar, opn1, opn2] #opn left out

    cnt = 0
    mylist = []
    for x in visi:
        cnt +=1
        skleidziam = [[cnt,z] for z in x]
        mylist.extend(skleidziam)

    dff = pd.DataFrame(mylist, columns=['rol','dsc'])
    
    if directed==True:
        G = nx.DiGraph(name=nr)
    else:
        G = nx.Graph(name=nr)
        
    for x in dff.dsc.unique():
        if (isinstance(x, unicode) == True) or (isinstance(x, str) == True):
            rol = list(dff[dff.dsc == x]['rol'].values)
            G.add_node(x, rol = rol, nr = nr)
               
    def kind1(g, nr):
        ''' visi su visais. Tik nekryptinis'''
        g = nx.Graph(g, name=nr)
        from itertools import combinations
        nodes = g.nodes()
        edges = combinations(nodes, 2)
        #g = nx.Graph()
        g.add_nodes_from(nodes)
        g.add_edges_from(edges)
        return g
    
    def kind2(g, nr, directed=True):
        ''' visi i doktoranta. Kryptinis ir nekryptinis '''
        if nx.is_directed == False:
            print "E: The Graph is not directed" 
        dkt=''
        kiti=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
            if 1 not in data['rol']:
                kiti.append(n)
        for x in kiti:
            g.add_edge(x, dkt)
            g[x][dkt]['nr']=nr # kitas atvejis, sujungti visus, tada isimti rysius, kuriu vienas narys nera dkt.   e,v data in G.edges_iter(data=True):
            try:
                g[x][dkt]['weight'] += 1
            except:
                g[x][dkt]['weight'] = 1
        return g
    
    def kind3(g, directed=False): #oponent graph
        ''' Oponentai pries dkt. Kryptinis ir nekryptinis.'''
        dkt=''
        opn=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
            if 5 in data['rol']:
                opn.append(n)
        for x in opn:
            g.add_edge(x, dkt)
        return g
    
    def kind4(g, directed=False):
        ''' visi i doktoranta ir vadova'''
        dkt=''
        vdv=''
        kiti=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
            if 2 in data['rol']:
                vdv = n
            if 1 not in data['rol'] and 2 not in data['rol']:
                kiti.append(n)
        for x in kiti:
            g.add_edge(x, dkt)
        for x in kiti:
            g.add_edge(x, vdv)
        return g
    
    def kind5(g, directed=False):
        ''' Tuscia vieta'''
        pass

    def kind6(g, directed=False):
        dkt=''
        vdv=''
        kiti=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
            if 2 in data['rol']:
                vdv = n
            if 5 in data['rol']:
                kiti.append(n)
        for x in kiti:
            g.add_edge(x, dkt)
        for x in kiti:
            g.add_edge(x, vdv)

    
    def kind7(g, directed=True):
        '''directed, everyone to everyone expect for doktr,false'''    
        from itertools import combinations
        import itertools
        
        if g.is_directed():
            edges=itertools.permutations(g.nodes(),2)
        else:
            edges=itertools.combinations(g.nodes(),2)
        g.add_edges_from(edges)
        

        dkt=''
        vdv=''
        kiti=[]
        
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                disertacijos_kryptis = n
            if 2 in data['rol']:
                kiti.append(n)
            if 3 in data['rol']:
                kiti.append(n)
            if 4 in data['rol']:
                kiti.append(n)
            if 5 in data['rol']:
                kiti.append(n)
                
        for x in kiti:
            try:
                g.remove_edge(disertacijos_kryptis, x)
            except:
                pass
            
        print g.edges(data=True)
        return g
        

    def kind8(g, directed=False):
        '''directed, everyone to everyone expect from doktr and vdv to anyone else'''    
        from itertools import combinations
        nodes = g.nodes()
        edges = combinations(nodes, 2)
        #g = nx.Graph()
        g.add_nodes_from(nodes)
        g.add_edges_from(edges)
        
        dkt=''
        vdv=''
        
        kiti=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
            if 2 in data['rol']:
                vdv = n
        for x in kiti:
            g.remove_edge(dkt, x)
        for x in kiti:
            g.remove_edge(vdv, x)
        return g
    
    
    if kind == 1:
        return kind1(G,nr)
    if kind == 2:
        return kind2(G,nr)
    if kind == 3:
        return kind3(G)
    if kind == 4:
        return kind4(G)
    if kind == 5:
        return kind5(G)
    if kind == 4:
        return kind4(G)
    if kind == 6:
        return kind6(G)
    if kind == 7:
        return kind7(G)
    if kind == 8:
        return kind8(G)


def GraphOneDefenceByCodes(nr, df, kind=1, directed=False, mixed=False):
    '''This function composes a minigraph of each defence.
    It contains 8 types of drawing. 
    However, directed and mixed kwargs sometimes enforce different behaviour'''
    
    def validity_check():
        ''' should look into things'''
        pass
    
    #import pandas as pd
    #import networkx as nx
    dict = {}
    
    dkt = [df.T[nr]['dkt_dsc']]
    vdv = [df.T[nr]['vdv_dsc']]
    prm = [df.T[nr]['prm_dsc']]
    nar = df.T[nr]['nar_dsc']
#    opn = ['01B', '07B'] #fake so far
    visi = [dkt, vdv, prm, nar]  #, opn
    
    cnt = 0
    mylist = []
    for x in visi:
        cnt +=1
        skleidziam = [[cnt,z] for z in x]
        mylist.extend(skleidziam)
        
    dff = pd.DataFrame(mylist, columns=['rol','dsc'])
    
    G = nx.Graph(name=nr)
    
    if directed==True:
        G = nx.DiGraph(name=nr)
        
    for x in dff.dsc.unique():
        rol = list(dff[dff.dsc == x]['rol'].values)
        G.add_node(x, rol = rol)
        
    def kind1(g, nr):
        ''' visi su visais. Tik nekryptinis'''
        g = nx.Graph(g, name=nr)
        from itertools import combinations
        nodes = g.nodes()
        edges = combinations(nodes, 2)
        #g = nx.Graph()
        g.add_nodes_from(nodes)
        g.add_edges_from(edges)
        return g
    
    def kind2(g, nr, directed=False):
        ''' visi i doktoranta. Kryptinis ir nekryptinis '''
        dkt=''
        kiti=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
            if 1 not in data['rol']:
                kiti.append(n)
        for x in kiti:
            if g.has_edge(x,dkt):
                g[x][dkt]['weight'] += 1
            else:
                g.add_edge(x, dkt, weight=1)
                g[x][dkt]['nr']=nr
        return g
        
    
    def kind3(g, directed=False): #oponent graph
        ''' Oponentai pries dkt. Kryptinis ir nekryptinis.'''
        dkt=''
        opn=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
            if 5 in data['rol']:
                opn.append(n)
        for x in opn:
            g.add_edge(x, dkt)
        return g
    
    def kind4(g, directed=False):
        ''' visi i doktoranta ir vadova'''
        dkt=''
        vdv=''
        kiti=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
            if 2 in data['rol']:
                vdv = n
            if 1 not in data['rol'] and 2 not in data['rol']:
                kiti.append(n)
        for x in kiti:
            g.add_edge(x, dkt)
        for x in kiti:
            g.add_edge(x, vdv)
        return g
    
    def kind5(g, directed=False):
        ''' Tuscia vieta'''
        pass

    def kind6(g, directed=False):
        dkt=''
        vdv=''
        kiti=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
            if 2 in data['rol']:
                vdv = n
            if 5 in data['rol']:
                kiti.append(n)
        for x in kiti:
            g.add_edge(x, dkt)
        for x in kiti:
            g.add_edge(x, vdv)
    
    def kind7(g, directed=False):
        '''directed, everyone to everyone expect for doktr,false'''    
        from itertools import combinations
        nodes = g.nodes()
        edges = combinations(nodes, 2)
        #g = nx.Graph()
        g.add_nodes_from(nodes)
        g.add_edges_from(edges)
        
        dkt=''
        vdv=''
        
        kiti=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
        for x in kiti:
            g.remove_edge(dkt, x)
        return g

    def kind8(g, directed=False):
        '''directed, everyone to everyone expect from doktr and vdv to anyone else'''    
        from itertools import combinations
        nodes = g.nodes()
        edges = combinations(nodes, 2)
        #g = nx.Graph()
        g.add_nodes_from(nodes)
        g.add_edges_from(edges)
        
        dkt=''
        vdv=''
        
        kiti=[]
        for n, data in g.nodes_iter(data=True):
            if 1 in data['rol']:
                dkt = n
            if 2 in data['rol']:
                vdv = n
        for x in kiti:
            g.remove_edge(dkt, x)
        for x in kiti:
            g.remove_edge(vdv, x)
        return g
    
    
    if kind == 1:
        return kind1(G,nr)
    if kind == 2:
        return kind2(G,nr)
    if kind == 3:
        return kind3(G)
    if kind == 4:
        return kind4(G)
    if kind == 5:
        return kind5(G)
    if kind == 4:
        return kind4(G)
    if kind == 6:
        return kind6(G)
    if kind == 7:
        return kind7(G)
    if kind == 8:
        return kind8(G)

def sudekiGrafus(graphList):
    '''Takes a list of graphs and creates on graph out of them.
    Different approaches may be taken here.'''
    import numpy as np
    
    G = nx.DiGraph()
    count = -1
    for SG in graphList:
        count += 1

        for n, data in SG.nodes_iter(data=True):
            if G.has_node(n):
                G.node[n]['keliuoseGynimuoseBuvo'] += 1
                if 1 in data['rol']:
                    G.node[n]['disertaciju'] += 1
            else:
                G.add_node(n, disertaciju=0)
                G.add_node(n, keliuoseGynimuoseBuvo=1)
                
        for u, v, data in SG.edges_iter(data=True):
            if G.has_edge(u,v):
                try:
                    G[u][v]['weight'] += SG[u][v]['weight']
                except:
                    pass
            else:
                G.add_edge(u, v, weight=1)

    print count, " entries viewed."
    print "Nr of nodes: ", len(G.nodes())
    print "Nr of edges: ", len(G.edges())
    return G


def augmentNodes(g):
    r1 = nx.eigenvector_centrality_numpy(g)
    r2 = nx.degree_centrality(g) # DP MY
    r3 = nx.betweenness_centrality(g)
    r5 = nx.load_centrality(g,weight='weight') # DY, WY-writename # Scientific collaboration networks: II. Shortest paths, weighted networks, and centrality, M. E. J. Newman, Phys. Rev. E 64, 016132 (2001).
    r6 = nx.pagerank(g, alpha=0.85, personalization=None, max_iter=100, tol=1e-08, nstart=None, weight='weight')
    
    if nx.is_directed(g) == True:
        r8 = nx.in_degree_centrality(g)
        r9 = nx.out_degree_centrality(g)
#        r10 = nx.hits(g, max_iter=100, tol=1e-08, nstart=None)
    else:
        r4 = nx.communicability_centrality(g)
        r7 = nx.clustering(g, weight='weight')
        
    for x in g.nodes():
        g.node[x]['eigenvector_centrality_numpy'] = r1[x]
        g.node[x]['degree_centrality'] = r2[x]  
        g.node[x]['betweenness_centrality'] = r3[x]
        g.node[x]['load_centrality'] = r5[x]  
        g.node[x]['pagerank'] = r6[x]

        if nx.is_directed(g) == True:
            g.node[x]['in_degree_centrality'] = r8[x]
            g.node[x]['out_degree_centrality'] = r9[x]
#            g.node[x]['hits'] = r10[x]
        else:
            g.node[x]['communicability_centrality'] = r4[x]
            g.node[x]['clustering'] = r7[x]
    return g        


def augmentEdges(g):
    r1 = nx.edge_betweenness_centrality(g, normalized=True, weight='weight')
    for x in nx.edges_iter(g):
        g[x[0]][x[1]]['edge_betweenness_centrality'] = r1[x]
    return g

'''
MOVE ELSEWHERE TO STATS
def augmentEdges(G):
    r1 = nx.shortest_path_length(G) #unweighted
    r2 = nx.all_pairs_dijkstra_path(G)
    r3 = nx.all_pairs_dijkstra_path_length(G)
    r4 = nx.communicability_exp(G)
    
    for source in r3.keys:
        for target in r3[source]:
            pass
           # G[source][target]['dijkstra_path_length'] = res
    print "This is not working properly. Need further inspection"        
    return G
'''
