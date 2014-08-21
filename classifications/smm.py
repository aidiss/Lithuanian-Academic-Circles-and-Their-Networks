
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pieski.py

def import_smm():
    """
    Creates a 
    returns a list where first item is dataframe and second is ebunch.
    
    Some things should be changed like url of xls file.
    """
    
    df = pd.DataFrame (columns=['pavadinimas','lmt2012','lmt2012_kryptis','lmt2012_sritis','smm2011','smm2007', 'smm1997'])
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
    

    return [df3, ebunch]
#df.saka = df.saka.str.split(';')
