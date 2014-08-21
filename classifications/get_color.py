#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  get_colors.py
# 2014 07 23

def get_node_colors(nodelist, df):
    """
    Gets colors for a list of nodes
    
    returns a list of color names
    
    Possible changes:
    A possibility to get a string or a list.
    A possibility to return different code for color, RGB or HEX
    """
    colorlist = []
    
    for x in nodelist:
        TEMP = df[df['krppvd'] == x]['srtpvd'].unique()
        if TEMP == u'Humanitariniai mokslai':
            colorlist.append('r')
        elif TEMP == u'Socialiniai mokslai':
            colorlist.append('b')
        elif TEMP == u'Biomedicinos mokslai':
            colorlist.append('y')
        elif TEMP == u'Fiziniai mokslai':
            colorlist.append('c')
        elif TEMP == u'Technologijos mokslai':
            colorlist.append('g')
        elif TEMP == u'Žemės ūkio mokslai':
            colorlist.append('m')
        else:
            colorlist.append('k')
    return colorlist


# 2014 07 23
def get_edge_colors(edgelist, df):
    """
    Gets colors for a list of edges
    
    returns a list of color names
    
    Possible changes:
    A possibility to get a string or a list.
    A possibility to return different code for color, RGB or HEX
    """
    colorlist = []
    for x in edgelist:
        SHIT = df[df['krppvd'] == x]['srtpvd'].unique()
        if SHIT == u'Humanitariniai mokslai':
            colorlist.append('r')
        elif SHIT == u'Socialiniai mokslai':
            colorlist.append('b')
        elif SHIT == u'Biomedicinos mokslai':
            colorlist.append('y')
        elif SHIT == u'Fiziniai mokslai':
            colorlist.append('c')
        elif SHIT == u'Technologijos mokslai':
            colorlist.append('g')
        elif SHIT == u'Žemės ūkio mokslai':
            colorlist.append('m')
        else:
            colorlist.append('k')
    return colorlist

def get_edge_color(edge_name):
    pass

def get_node_color(node_name):
    pass 
