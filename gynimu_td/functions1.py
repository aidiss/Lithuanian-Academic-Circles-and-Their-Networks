#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv
import pandas as pd





'''
def letsiter():
    THELIST = [x for x in df.prm.str.split(',').values]
    cnt= -1
    for x in THELIST:
        cnt+=1
        print cnt
        try:
            print x[2] #
        except:
            pass
'''

#def test(data):
#    return [x for x in data]
#df.nariai.dropna().apply(test).values




# This pattern creates a list of all Fields
pattern = '|'.join(code_to_name.keys())




def kiekKrypciu(df):
    mydict = {}
    
    def kiekkrypciuviename(nr):
        return len(set(df.T[nr]['nar_dsc']))
        
    for x in df.index.values:
        rez = kiekkrypciuviename(x)
        mydict[x] = rez
    return mydict

'''
#Pridedame metus, menesi ir diena.
df['year'] = [t.year for t in df.data_lks]
df['month'] = [t.month for t in df.data_lks]
df['day'] = [t.day for t in df.data_lks]
df.groupby(['year']).size().plot()
'''