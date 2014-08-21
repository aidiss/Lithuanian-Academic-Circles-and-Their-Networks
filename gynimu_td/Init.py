#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from GynimuTd.Dicts import *

HEADINGS_DF1=['dkt_vrd', 'dkt_dsc', 'dkt_ins', 'dkt_lps', 
              'dis_tem', 'dis_ant',
              'vdv_vrd', 'vdv_dsc', 'vdv_ins', 'vdv_pdl',
              'prm_vrd', 'prm_dsc', 'prm_ins', 'prm_pdl',
              'opn_vrd', 'opn_dsc', 'opn_ins', 'opn_pdl',
              'trb',
              'gyn_lks', 'gyn_vta']

def mainALL():
    mylist = []
    apie_viena_gynima = []
    for eilesnumeris in range(1,3679):
#        print "Skaitau1: ", eilesnumeris
        try:
            response = open(r"C:\Users\Saonkfas\Documents\GitHub\Lithuanian-Academic-Circles-and-Their-Networks\htmls\%s.html" % eilesnumeris) #htmls/%s.html
            html = response.read()
        
            skelbianti_institucija = re.findall(r'<div class="prevfld"><p class="fldname">Skelbianti institucija</p><p>(.+?)</p></div>', html, re.DOTALL)
            data_ir_laikas = re.findall(r'<div class="prevfld"><p class="fldname">Data ir laikas</p><p>(.+?)</p></div>', html, re.DOTALL)
            vieta = re.findall(r'<div class="prevfld"><p class="fldname">Vieta</p><p>(.+?)</p></div>', html, re.DOTALL)
            doktorantas = re.findall(r'<div class="prevfld"><p class="fldname">Doktorantas</p><p>(.+?)</p></div>', html, re.DOTALL)
            tema = re.findall(r'<div class="prevfld"><p class="fldname">Tema</p><p>(.+?)</p></div>', html, re.DOTALL)
            mokslo_saka = re.findall(r'<div class="prevfld"><p class="fldname">Mokslo šaka</p><p>(.+?)</p></div>', html, re.DOTALL)
            parengta_institucijoje = re.findall(r'<div class="prevfld"><p class="fldname">Parengta institucijoje</p><p>(.+?)</p></div>', html, re.DOTALL)
            vadovas = re.findall(r'</div><div class="prevfld"><p class="fldname">Vadovas</p><p>(.*?)</p></div>', html, re.DOTALL) 
            pirmininkas = re.findall(r'<div class="grfld"><span class="specfld">Pirmininkas</span>(.+?)</div>', html, re.DOTALL)
            nariai = re.findall(r'<div class="grfld">(.+?)(?:<\/div><\/div>).*?<div class="prevfldgroup">', html, re.DOTALL) 
            oponentai = re.findall(r'oponentai.*<div class="grfld">(.*?)(?=<)', html, re.DOTALL)
            #oponentai = re.findall(r'opon.*\n<div class="grfld">(.*?dr.*?\))(?:</div><div class="grfld">)?(.*?dr.*?\))?.*', html)
            anotacija = re.findall (r'<div class="fldanotation"><p class="fldname">\s*Anotacija\s*</p>\s*<div class="fldcontent">(.+?)</div>', html, re.DOTALL) # gal veiks..
            pateikimo_data = re.findall(r'</div><div class="prevfld"><p class="fldname">Pateikimo data</p><p>(.*?)</p></div>', html, re.DOTALL)
            
            apie_viena_gynima.append(skelbianti_institucija)
            apie_viena_gynima.append(data_ir_laikas)
            apie_viena_gynima.append(vieta)
            apie_viena_gynima.append(doktorantas)
            apie_viena_gynima.append(tema)
            apie_viena_gynima.append(parengta_institucijoje)
            apie_viena_gynima.append(vadovas)    
            apie_viena_gynima.append(pirmininkas)
            apie_viena_gynima.append(nariai)               
            apie_viena_gynima.append(oponentai)
            apie_viena_gynima.append(anotacija)
            apie_viena_gynima.append(pateikimo_data)
            apie_viena_gynima.append(mokslo_saka)
            
            mylist.append(apie_viena_gynima)
            apie_viena_gynima = []
            
        except Exception as e:
            print "nepavyko", eilesnumeris, str(e) 
            continue
    return mylist
