# -*- coding: utf-8 -*-

def get_num_of_interdir_branches(df):
    
    """
    Does some analysis of a dataframe
    
    Returns:
    Number of interfields branches

    """
    
    mydict = {}
    unq = df[df.duplicated(u'skspvd')].skspvd.unique()
    intrdscplnr = df[df.skspvd.isin(unq)].sort(u'skspvd')

    #Tarpkryptinės šakos ir tarp kokių krypčių
    mydict[u"tarpkryptinių šakų:"]= len([x for x in list(unq)])

    return mydict

def get_num_of_interdir_branches(df):
    
    """
    Returns
        Number of interdirection branches
    """
    mydict = {}
    mylist = []
    unq = df[df.duplicated(u'skspvd')].skspvd.unique()
    for x in unq:
        if len(df[df['skspvd'] == x].krppvd.unique()) > 1:     
             mylist.append([x, df[df['skspvd'] == x].krppvd.unique()])
             
    mydict[u"tarpkryptinių šakų:"] =  len(mylist)
    return mydict
    
    
def get_num_of_branches(df):
    """
    
    Returns:
        Number of branches
        Number of unique branches
        Number of directions
        Number of interfield branches
        Number of interdirection branches
    """
    mydict = {}
    mydict[u"šakų:"] = len(df)
    return mydict


def get_num_of_unq_branches(df): 
    """
    
    Returns:
        Number of unique branches
    """
    mydict = {}
    mydict[u"unikalių šakų:"] =  len(df.skspvd.unique())
    return mydict
    
def get_num_of_dirs(df):
    """
    
    Returns:
        Number of branches
    """
    mydict = {}
    mydict[u"krypčių:"] =  len(df.krppvd.unique())
    return mydict
    
def get_num_of_interfield_branches(df):
    """
    Returns:
        Number of interfield branches
    """
    mydict = {}
    mylist = []
    unq = df[df.duplicated(u'skspvd')].skspvd.unique()
    
    for x in unq:
        if len(df[df['skspvd'] == x].srtpvd.unique()) > 1: 
            mylist.append([x, df[df['skspvd'] == x].srtpvd.unique()])
            
    mydict[u"tarpsritinių šakų:"] = len(mylist)
    return mydict
