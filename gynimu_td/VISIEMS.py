#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  VISIEMS.py.py


visiKrypciuPav = set(df.dkt_dsc_pav.unique()) | set(df.vdv_dsc_pav.unique()) | set(df.prm_dsc_pav.unique()) | set(df.opn_dsc_pav.unique()) | set(df[1].unique()) | set(df[2].unique()) | set(df[3].unique()) | set(df[4].unique())
#gaukKokiosKryptysSveciuojasi(df, 'farmacija', 2)
[[x, Stats.gaukKiekUnikaliu(df, x, kind=1, output='len')] for x in range(1,5)] # output can be 'df' # still buggy, returns entries with empty values
rez = [Stats.gaukKiekUnikaliu(df, x, kind=1, output='len') for x in range(1,5)]
