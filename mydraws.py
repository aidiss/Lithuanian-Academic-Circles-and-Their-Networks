#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.mpl_style = 'default'

def draw_history(df):
    plt.figure(1, figsize=(13,7))
    for x in ['H','S','P','T','B']:
        plt.subplot(111)
        fltrd = df[df['dkt_dsc'].str.contains(x, na=False)]
        grpd = fltrd.groupby(fltrd['gyn_lks'].map(lambda x: x.year)).size()
        plt.plot(grpd.index, grpd.values,label='{}'.format(x),linewidth=4,alpha=0.7)
    
    #plot(df.groupby(df['data_lks'].map(lambda x: x.year)).size())

    plt.xlabel(u'Metai')
    plt.ylabel(u'Gynimų sk')
    plt.title(u'Disertacijų gynimai pagal metus')

    plt.legend(loc=2) #bbox_to_anchor=(0., 1.02, 1., .102) , ncol=1 , mode="expand"

    #plt.axis([1940, 2014, 0, 500])
    plt.grid(True)
    plt.show()

# This is the alternative way of drawing the main timeline
def draw_history2(df):
    crazylist = [df[df['dkt_dsc'].str.contains(x, na=False)].groupby(df['gyn_lks'].map(lambda x: x.year)).size() 
                 for x in ['H','S','P','T','B']]
    dfplot = pd.DataFrame(crazylist,index=['H', 'S', 'P', 'T', 'B'])
    #dfplot = dfplot.dropna(axis=1) #This makes some erros
    dfplot = dfplot.fillna(0) # But this does not look very nice, I have to fix axes.
    dfplot.T.plot(kind='line',linewidth=3,alpha=0.5,figsize=(13,7))
    dfplot
    
    plt.show()

# Draws all branches of a field.
def draw_field_history(df, sritis, 
                       daktar=True, habil=True, 
                       start=None, end=None, 
                       KIND='line', figsize=(13,7)):
    if habil == False and daktar == False:
        print("What are you trying to plot dude?")
        return                    
    if habil == False:
        fltrd = df[df['dkt_lps'] != ('habilituotas daktaras')]
    if daktar == False:
        fltrd = fltrd[fltrd['dkt_lps'] != ('daktaras')]

    plt.figure(1, figsize=(13,7))
    fltrd = df[df['dkt_dsc'].str.contains(sritis, na=False)]
    for kryptis in ['01', '02', '03', '04', '05', '06', '07', '08', '09',  '10']:
        fltrd1 = df[df['dkt_dsc'].str.contains(kryptis, na=False)]
        grpd = fltrd1.groupby(fltrd['gyn_lks'].map(lambda x: x.year)).size()
        plt.plot(grpd.index, grpd.values,label='{}{}'.format(sritis, kryptis),linewidth=4,alpha=0.7)
    
    plt.xlabel(u'Metai')
    plt.ylabel(u'Gynimų sk')
    plt.title(u'{} srities disertacijų gynimai pagal metus'.format(sritis))
    plt.legend(loc=2)
    plt.show()
