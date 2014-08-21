# -*- coding: utf-8 -*-

def flatten_graph(g):
    """
    Takes a graph and changes it to a different perspective
    All nodes that have been connected only to two nodes covenrted to edges
    
    Arguments:
    g- networkx graph
    
    Returns: 
    networkx graph object.
    """
    
    istrinti = []
    nupiesti = []
    for x in g.nodes():
        if len(g[x]) == 2:  # randa viršūnes, kurios turi lygiai dvi kraštines.
            du_nodai = []
            for key in g[x]: 
                du_nodai.append(key) 
            # Ka reikes prideti? 
            
            setas = set(g.neighbors(du_nodai[0])) & set(g.neighbors(du_nodai[1])) #sukuriame potencialiai sujungiamų viršūnių setuką.
            setas = list(setas)
            setas = [x for x in setas if len(g[x]) == 2]
            setas = [x for x in setas if x[0] not in u'ZXCVBNMASDFGHJKLQWERTYUIOPĄČĘĖĮŠŲŪ']
            istrinti.extend(setas)            
            
            # ka reikes prideti
            ONESHIT = (du_nodai[0], du_nodai[1], {'label': ', '.join(setas), 'weight': len(setas)})
            if ONESHIT[0][0] in u'ZXCVBNMASDFGHJKLQWERTYUIOPĄČĘĖĮŠŲŪ' and ONESHIT[1][0] in u'ZXCVBNMASDFGHJKLQWERTYUIOPĄČĘĖĮŠŲŪ':
                nupiesti.append(ONESHIT)
            
    g.remove_nodes_from(istrinti)
    g.add_edges_from(nupiesti)
    return g
