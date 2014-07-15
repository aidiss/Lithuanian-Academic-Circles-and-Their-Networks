#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Looks for a dissertation name in the main dataframe.
def rsktem(tema):
    return df[df.tema.str.contains(tema, regex=True, case=False)]
    
    
# Looks for a name in the main dataframe.
def rskvrd(vardas):
    return df[df.dkt_vrd.str.contains(vardas, regex=True, case=False)]
    
