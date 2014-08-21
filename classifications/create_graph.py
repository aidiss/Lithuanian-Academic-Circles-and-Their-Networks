# -*- coding: utf-8 -*-
import networkx as nx

def create_graph(df):
    """
    Converts a dataframe to a graph.
    
    Arguments:
    df - pandas dataframe object.
    
    Dataframe must have the following structure:
    ..............
    
    Returns: 
    networkx DiGraph object.
    """
    
    def gauktipa(x):
        if len(df[df[u'krppvd'] == x]) != 0:
            return u'kryptis'
        elif len(df[df[u'skspvd'] == x]) != 0:
            return u'saka'
        else:
            return u"nzn"
    
    def gaukkrpkds(x):
        if list(df[df[u'krppvd'] == x].krpkds.unique())[0]:
            return list(df[df[u'krppvd'] == x].krpkds.unique())[0]
    #    if list(df3[df3[u'sritis'] == x].sritis.unique())[0]:
    #        return list(df[df[u'sritis'] == x].sritis.unique())[0]

    trkrp_sakos = df[df.skspvd.duplicated()].skspvd.values
    trkrp_sakos_df = df[df.skspvd.isin(trkrp_sakos)].sort('skspvd')
    grpd = trkrp_sakos_df.groupby('skspvd').size()
    grpd.order(0,ascending=False)
    #gavome duplikatus ir jų pasirodymo skaičių
    ebunch = [(x[0],x[2]) for x in trkrp_sakos_df.values]
    ebunch1 = [(x[2],x[0]) for x in trkrp_sakos_df.values]
    ebunch = ebunch1
    
    G = nx.DiGraph(ebunch)

    for x in G.nodes():
        G.node[x][u'tipas'] = ''

        G.node[x][u'krppvd'] = ''
        G.node[x][u'krpkds'] = ''

        G.node[x][u'srtpvd'] = ''
        G.node[x][u'srtkds'] = ''

        TIPAS = gauktipa(x)
        G.node[x][u'tipas'] = TIPAS
        if TIPAS == u'kryptis':
            krpkds = gaukkrpkds(x)
            G.node[x][u'krpkds'] = krpkds
        #if TIPAS == u'kryptis':
        #    G.node[x][u'srtkds'] = krpkds.strip('0123456789')
            G.node[x][u'srtkds'] = df[df.loc[:,u'krppvd'] == x]['srtkds'].unique()[0]
        else:
            G.node[x][u'srtkds'] = None
    return G
