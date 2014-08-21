#!/usr/bin/env python
# -*- coding: utf-8 -*-

def GaukKryptiPagalVarda(vardas):

    tempdf = df[~df.prm_dsc.isin(code_to_name.values())].dropna()
    tempdf.prm_vrd.replace('- Dr. ','', inplace=True, regex=True)
    tempdf.prm_vrd.replace('prof|Prof|dr.|Dr.|Doc.|doc.|habil.|', '', inplace=True, regex=True)
    tempdf.prm_vrd = tempdf.prm_vrd.str.rstrip(' ')
    tempdf.prm_vrd = tempdf.prm_vrd.str.lstrip(' -.')

    mylist = [x for x in tempdf.prm_vrd.values]
    mylist = [x for x in mylist if x]
    mylist = set(mylist)
    #[x.lower() for x in mylist]

    dfseni = pd.read_pickle('gynima1950-2009.pkl')

    import pprint
    splitlist = [x.split() for x in mylist]
    splitlist = [x for x in splitlist if len(x) >= 2]
    lit_list = []
    for x in splitlist:
        fltrd = dfseni[dfseni.dkt_vrd.str.contains(x[0].strip('.'),case=False) 
                    & dfseni.dkt_vrd.str.contains(x[1],case=False)]
        if len(fltrd) > 0:
            mydict = {}
            mydict['vardas'] = ' '.join([x[0],x[1]])
            mydict['dkt_dsc'] = list(set(fltrd['dkt_dsc'].values))
            mydict['length'] = len(fltrd)
            lit_list.append(mydict)
    #pprint.pprint(lit_list)

    surelist = [x for x in lit_list if x['length'] == 1]
    def rask_dsc(vardas): #IR TEMOS DISCIPLINA
        if surelist[0]['vardas'] == vardas:
            return surelist[0]['dkt_dsc'][0] 
        #SPLIT


    #df[~df.prm_dsc.str.contains(pattern, na=False)].prm_vrd = rask_dsc(df[~df.prm_dsc.str.contains(pattern, na=False)].prm_vrd)
    #df[~df.vdv_dsc.str.contains(pattern, na=False)].vdv_vrd # 
    #df[~df.vdv_dsc.str.contains(pattern, na=False)].vdv_dsc