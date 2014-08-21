#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import networkx as nx

def MazojiDfStatistika(df, code_to_name): #2014-07-28
    ''' grazina truputi statistikos apie gynimus. Tam yra naudojamas
    dataframe. Truputis problemų su tikslumu, trūksta informacijos
    švarumo, kad būtų galima gauti tikslesnę info.'''
    
    
    mydict = {}
    mydict["Viso įrašų"] =  len(df)
    
    pattern = '|'.join(code_to_name.keys())
    
    dktcase = df.dkt_dsc.str.contains(pattern, na=False)
    prmcase = df.prm_dsc.str.contains(pattern, na=False)
    vdvcase = df.vdv_dsc.str.contains(pattern, na=False)
    
    res = df[dktcase]
    mydict["atvejai, kai žinoma doktoranto temos kryptis"] = len(res)

    res = df[prmcase] # Kur yra aiški pirmininko kryptis?
    mydict[u'įrašai turi pirmininko kryptį'] = len(res)

    res = df[vdvcase] # Kur yra aiški pirmininko kryptis?
    mydict[u'įrašai turi vadovo kryptį'] = len(res)

    res = df[dktcase & prmcase]
    mydict["atvejais aiškios doktoranto ir pirmininko kryptys"] = len(res)

    res = df[(dktcase & prmcase) & (df.dkt_dsc == df.prm_dsc)]
    mydict["atvejų kai doktoranto kryptis sutampa su komisijos pirmininko kryptimi"] = len(res)

    res = df[dktcase & prmcase]
    mydict["kai aiški ir doktoranto ir vadovo kryptis"] = len(res)

    res = df[(dktcase & prmcase) & (df.dkt_dsc == df.vdv_dsc)]
    mydict["atvejų kai doktoranto kryptis sutampa su vadovo kryptimi"] =  len(res)

    return mydict

def gaukKiekUnikaliu(df, num=1, kind=1,output='len'):
    
    mylist = []
    df = df.loc[:,['dkt_dsc_pav','vdv_dsc_pav','prm_dsc_pav','opn_dsc_pav',1,2,3,4]]
    if kind == 1:
        rez = df[df.apply(pd.Series.nunique, axis=1) == num].dropna()
        if output=='len':
            return len(rez)
        if output=='df':
            return rez
        
    if kind == 2:
        if num != 1:
            print "Error, this method can only get all uniques"
            return
        rez = df[df.eq(df[1], axis='index').all(1)].dropna()
        if output=='len':
            return len(rez)
        if output=='df':
            return rez
        
def createAllStatDf(G, directed=False, weighted=True):
    '''sukuria grafui statistika'''

    def forDirected(G):

        myList = [nx.in_degree_centrality(G), 
                nx.out_degree_centrality(G), 
                nx.hits(G, max_iter=100, tol=1e-08, nstart=None)]
        return myList

    def forUndirected(G):

        myList = [nx.eigenvector_centrality_numpy(G), 
                  nx.degree_centrality(G),
                  nx.betweenness_centrality(G),
                  nx.communicability_centrality(G), 
                  nx.load_centrality(G),   
                  nx.pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-08, nstart=None, weight='weight'),
                  nx.clustering(G, weight='weight')]
        return myList

    if directed==True and weighted==True:
        data = forDirected(G)
        df = pd.DataFrame(data)
        return df.T
    
    elif directed==False and weighted==True:
        data = forUndirected(G)
        names = ['eigenvector_centrality_numpy','degree_centrality', 'betweenness_centrality','communicability_centrality','load_centrality','pagerank','clustering']
        df = pd.DataFrame(data, index=names)
        return df.T
    
    else:
        print "wrong"
        return

def gaukKokiosKryptysSveciuojasi(df, pavadinimas, virsSkaiciaus):
    tempdf = df[df.dkt_dsc_pav == pavadinimas][df.apply(pd.Series.nunique, axis=1) > virsSkaiciaus]
    return pd.Series(tempdf.values.ravel()).unique()
    
def edgeCentralities(df, G):

    DF2 = pd.DataFrame(nx.edge_betweenness_centrality(G), 
    index=['edge_betweenness_centrality'])
    DF2 = DF2.T.unstack(level=0)
    DF2.columns = DF2.columns.get_level_values(1)

    DF3 = pd.DataFrame(nx.edge_current_flow_betweenness_centrality(G,normalized=True), 
    index=['edge_current_flow_betweenness_centrality'])
    DF3 = DF3.T.unstack(level=0)
    DF3.columns = DF3.columns.get_level_values(1)

    DF4 = pd.DataFrame(nx.edge_load(G), 
    index=['edge_load'])
    DF4 = DF4.T.unstack(level=0)
    DF4.columns = DF4.columns.get_level_values(1)

    DFB = pd.concat([DF2, DF3, DF4], axis=0) #buggy
    return pd.Panel({'edge_betweenness_centrality':DF2, 
                     'edge_current_flow_betweenness_centrality':DF3, 
                     'edge_load':DF4})



def getHugeStats(g):
    
    if nx.is_directed(g) == True:
        P1 = pd.DataFrame({'load_centrality': nx.load_centrality(g, weight='weight'),
                           'betweenness_centrality': nx.betweenness_centrality(g, weight='weight'),
                           
                           'pagerank': pd.Series(nx.pagerank(g, alpha=0.85, personalization=None, max_iter=100, tol=1e-08, nstart=None, weight='weight')),
                           'eigenvector_centrality': nx.eigenvector_centrality_numpy(g),
                           'degree_centrality': pd.Series(nx.degree_centrality(g)),
                           'in_degree_centrality': pd.Series(nx.in_degree_centrality(g)),
                           'out_degree_centrality': pd.Series(nx.out_degree_centrality(g))})
                           
    else:
        P1 = pd.Panel({'spl': pd.DataFrame(nx.shortest_path_length(g)),
                          'apdp': pd.DataFrame(nx.all_pairs_dijkstra_path(g)), 
                          'apdl': pd.DataFrame(nx.all_pairs_dijkstra_path_length(g)),
                          'c_exp': pd.DataFrame(nx.communicability_exp(g))})    
    return P1



def totalAppearancesVsDefences(G, plot=False, ret='list'):
    GES, GESL, GEST  = G.nodes(), len(G.nodes()), G.edges(data=True)
    GNS, GNSL, GNST  = G.edges(), len(G.edges()), G.nodes(data=True)
    rez = [[x,y['disertaciju'],y['keliuoseGynimuoseBuvo'], y['disertaciju'] / float(y['keliuoseGynimuoseBuvo'])  ] for x,y in GNST]

    mylist = [x[3] for x in rez]
    fullList = [x[1:4] for x in rez]
    index = [x[0] for x in rez]
    S = pd.DataFrame(mylist, index=index)
    S = S.sort([0],ascending=False)
    if plot==True:
        plt.plot(S)
        return
    if ret=='list':
        return rez
    if ret=='df':
        return pd.DataFrame(fullList, index=index).sort(0, ascending=False)

'''
ShortPathForUnweighted = [ 
#nx.single_source_shortest_path(G, source),  #Compute shortest path between source and all other nodes reachable from source.
#nx.single_source_shortest_path_length(G, source),  #Compute the shortest path lengths from source to all reachable nodes.
#nx.predecessor(G, source)
]  #Returns dictionary of predecessors for the path from source to all nodes in G.

#Shortest path algorithms for weighed graphs.
ShortPathForWeighted = [
    #nx.dijkstra_path(G, source, target),  #Returns the shortest path from source to target in a weighted graph G.
    #nx.dijkstra_path_length(G, source, target),  #Returns the shortest path length from source to target in a weighted graph.
    #nx.single_source_dijkstra_path(G, source),  #Compute shortest path between source and all other reachable nodes for a weighted graph.
    #nx.single_source_dijkstra_path_length(G, source),  #Compute the shortest path length between source and all other reachable nodes for a weighted graph.
    nx.all_pairs_dijkstra_path(G),  #Compute shortest paths between all nodes in a weighted graph.
    nx.all_pairs_dijkstra_path_length(G),  #Compute shortest path lengths between all nodes in a weighted graph.
   # nx.single_source_dijkstra(G, source),#Compute shortest paths and lengths in a weighted graph G.
    #nx.bidirectional_dijkstra(G, source, target),  #Dijkstra’s algorithm for shortest paths using bidirectional search.
    #nx.dijkstra_predecessor_and_distance(G, source),  #Compute shortest path length and predecessors on shortest paths in weighted graphs.
    #nx.bellman_ford(G, source),  #Compute shortest path lengths and predecessors on shortest paths in weighted graphs.
    nx.negative_edge_cycle(G)] #
'''
