# -*- coding: utf-8 -*-

import networkx as nx
import json
import os    


# 2014 07 23
def d3_export(g, output_directory='output'):
    """
    This dumps json d3 file
    
    Arguments:
    g - networkx graph object
    output_directory - where the file is going to be saved
    
    Returns:
    No, only dump of a file.
    """

    try:
        os.stat(output_directory)
    except:
        os.mkdir(output_directory)
    
    code2num = {'H':1, 'S':2, 'P':3, 'T':4, 'B':5, 'A':6, None:7}
    nodelist = g.nodes()
    edgelist = g.edges()
    valuedict = {n:code2num[d['srtkds']] for n,d in sorted(g.nodes_iter(data=True))}
    
    outfile_name = os.path.join('%s' % output_directory,'tod3.json')

    node_key ={node:counter for counter,node in enumerate(sorted(nodelist))}
    
    nodes = [{'group' : valuedict[node],
              'name' : node,  #'group': cliques[node]  ,
              'nodeSize': 1} for node in sorted(nodelist)]  #'nodeSize': int(cited_works[node]['count'])
    
    links  = [{'source': node_key[p[0]],
              'target' : node_key[p[1]],
              'value' : 1} 
              for p in edgelist] #'value': int(p[2]['weight']) 
              
    d3_data = {'nodes': nodes, 'links' : links}
    json.dump(d3_data, open(outfile_name, 'wb'))
