# -*- coding: utf-8 -*-

import pandas as pd

def import_smm(dataframe=True, ebunch=False):
    """
    Creates a dataframe and ebunch file
    Returns:
    A list where first item is dataframe and second is ebunch.
    
    Some things should be changed like url of xls file.
    """
    
    if dataframe == True and ebunch == True:
        print "error, cannot return both dataframe and ebunch objects."
        return
        
    df = pd.DataFrame(columns=['pavadinimas','lmt2012','lmt2012_kryptis','lmt2012_sritis','smm2011','smm2007', 'smm1997'])
    PATH = r'C:\Users\Saonkfas\Documents\GitHub\Lithuanian-Academic-Circles-and-Their-Networks\klasifikacijos'
    NAME = 'smm2011.xlsx'
    URL = '\\'.join([PATH,NAME])

    N1, N2  = 'srtkds_pvs', 'krpkds_pvi_srt'

    df = pd.read_excel(URL, sheetname=N1, header=None, index_col=None)
    df.columns = [u'krpkds',u'krppvd']

    df1 = pd.read_excel(URL, sheetname=N2, header=None, index_col=None)
    df1.columns = [u'skskds',u'skspvd',u'krppvd']
    #df1[u'krpkds'].str.lower()
    #df1[u'krppvs'].str.lower()
    #df1.skspvd.str.split(',')

    mylist = []
    for x in range(len(df1.index.values)):
        fltrd = df1.loc[x, u'skspvd'].split(',')
        fltrd = [z.lstrip(' ').lower() for z in fltrd]
        fltrd = [z.rstrip(' .,').lower() for z in fltrd]
        df2 = pd.DataFrame({u'skspvd': fltrd},columns = [ u'skspvd',u'skskds', u'krppvd',u'krpkds'])
        df2['srtpvd'] = 'NZN'
        df2[u'skskds'] = df1.loc[x,u'skskds']
        df2[u'krppvd'] = df1.loc[x,u'krppvd']
        df1 = df1.dropna()
        mylist.append(df2)
    

    df3 = pd.concat(mylist)
    df3.index = range(len(df3))

    # Add the column
    SHIT = {x[0]:x[1] for x in df.loc[:,['krppvd','krpkds']].values}
    df3[df3.loc[:,'krppvd'] == 'Komunikacija ir informacija']['krpkds']='06H'
    df3.krpkds = [SHIT[x] if x != 'Komunikacija ir informacija' else '06H'  for x in df3.krppvd.values]
    df3['srtkds'] = df3.krpkds.str.strip('0123456789')
    trkrp_sakos = df3[df3.skspvd.duplicated()].skspvd.values
    trkrp_sakos_df = df3[df3.skspvd.isin(trkrp_sakos)].sort('skspvd')
    grpd = trkrp_sakos_df.groupby('skspvd').size()
    grpd.order(0,ascending=False)
    #gavome duplikatus ir jų pasirodymo skaičių
    ebunch = [(x[0],x[2]) for x in trkrp_sakos_df.values]
    ebunch1 = [(x[2],x[0]) for x in trkrp_sakos_df.values]
    ebunch = ebunch1
    
    if dataframe == True:
        return df3
        
    if ebunch == True:
        return ebunch

#df.saka = df.saka.str.split(';')


def import_lmt():
    """
    Returns a dataframe
    
    The function is divided into two, first part takes phisical, 
    technological and other sciences, while scond part of the function 
    return humanities and social sciences.
    """
    
    #FTB
    df = pd.read_excel(r'C:\Users\Saonkfas\Documents\GitHub\Lithuanian-Academic-Circles-and-Their-Networks\Klasifikacijos\lmt2012-10-12.xlsx',sheetname='ftb',header=None,index_col=None,columns=['sritis','kryptis','saka'])
    df.columns = [u'skspvd',u'skskds',u'krppvd',u'krpkds',u'srtpvd',u'srtkds']
    df.skspvd = df.skspvd.str.split(';')

    mylist = []
    for x in range(len(df.index.values)):
        fltrd = df.loc[x,u'skspvd']
        fltrd = [z.lstrip(' ').lower() for z in fltrd]
        fltrd = [z.rstrip(' .,').lower() for z in fltrd]
        df1 = pd.DataFrame({u"skspvd": fltrd})
        df1[u'skskds'] = df.loc[x,u'skskds']
        df1[u'krppvd'] = df.loc[x,u'krppvd']
        df1[u'krpkds'] = df.loc[x,u'krpkds']
        df1[u'srtpvd'] = df.loc[x,u'srtpvd']
        df1[u'srtkds'] = df.loc[x,u'srtkds']
        df1 = df1.dropna()
        mylist.append(df1)
    df = pd.concat(mylist)

    df.index = range(len(df))
    df = df.drop(df.index[[272,281]])
    df.index = range(len(df))
    df[u'skspvd'] = df[u'skspvd'].str.lstrip(' ').str.rstrip(' ')
    df[u'krppvd'] = df[u'krppvd'].str.lstrip(' ').str.rstrip(' ')
    df[u'srtpvd'] = df[u'srtpvd'].str.lstrip(' ').str.rstrip(' ')
    df = df[df[u'skspvd'] != '']

    dfFTB = df

    #HSM
    df = pd.read_excel(r'C:\Users\Saonkfas\Documents\GitHub\Lithuanian-Academic-Circles-and-Their-Networks\Klasifikacijos\lmt2012-10-12.xlsx',sheetname='hsm',header=None,index_col=None,columns=['sritis','kryptis','saka'])
    df.columns = [u'skspvd',u'skskds',u'krppvd',u'krpkds',u'srtpvd',u'srtkds']
    df.skspvd = df.skspvd.str.split(';')
    df = df.dropna()
    df.index = range(len(df))

    mylist = []
    for x in range(len(df.index.values)):
        fltrd = df.loc[x,u'skspvd']
        fltrd = [z.lstrip(' ').lower() for z in fltrd]
        df1 = pd.DataFrame({u"skspvd": fltrd})
        df1[u'skskds'] = df.loc[x,u'skskds']
        df1[u'krppvd'] = df.loc[x,u'krppvd']
        df1[u'krpkds'] = df.loc[x,u'krpkds']
        df1[u'srtpvd'] = df.loc[x,u'srtpvd']
        df1[u'srtkds'] = df.loc[x,u'srtkds']
        df1 = df1.dropna()
        mylist.append(df1)
    df = pd.concat(mylist)


    df.index = range(len(df))
    df = df.drop(df.index[[272,281]])
    df.index = range(len(df))
    df[u'skspvd'] = df[u'skspvd'].str.lstrip(' ').str.rstrip(' ')
    df[u'krppvd'] = df[u'krppvd'].str.lstrip(' ').str.rstrip(' ')
    df[u'srtpvd'] = df[u'srtpvd'].str.lstrip(' ').str.rstrip(' ')
    df = df[df[u'skspvd'] != '']

    dfHSM = df
    df = pd.concat([dfHSM,dfFTB])
    df.index= [x for x in range(len(df))]
    return df
