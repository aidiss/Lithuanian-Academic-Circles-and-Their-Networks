#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv
import pandas as pd

dsc_list = ['01S', '02S', '03S', '04S', '05S', '06S', '07S', '08S',
            '01H', '02H', '03H', '04H', '05H', '06H', '07H', 
            '01T', '02T', '03T', '04T', '05T', '06T', '07T', '08T', '09T', '10T', 
            '01B', '02B', '03B', '04B', '05B', '06B', '07B', '08B', '09B', '10B',  
            '01P', '02P', '03P', '04P', '05P', '06P', '07P', '08P', '09P',
            '01A', '02A', '03A', '04A']
dsc_i_pilna  = {'01H':'Filosofija',
                '02H':'Teologija',
                '03H':'Menotyra', 
                '04H':'Filologija', 
                '05H':'Istorija', 
                '07H':'Etnologija', 

                '01S':'Teisė',
                '02S':'Politikos mokslai',
                '03S':'Vadyba',
                '04S':'Ekonomika',
                '05S':'Sociologija',
                '06S':'Psichologija',
                '07S':'Edukologija',
                '08S':'Komunikacija ir informacija',

                '01P':'Matematika',
                '02P':'Fizika',
                '03P':'Chemija',
                '04P':'Biochemija',
                '05P':'Geologija',
                '06P':'Fizinė geografija',
                '07P':'Paleontologija',
                '08P':'Astronomija',
                '09P':'Informatika',

                '01A':'Agronomija',
                '02A':'Veterinarija',
                '03A':'Zootechnika',                
                '04A':'Miškotyra',

                '01B':'Biologija',
                '02B':'Biofizika',
                '03B':'Ekologija ir aplinkotyra',
                '04B':'Botanika',
                '05B':'Zoologija',
                '06B':'Medicina',
                '07B':'Odontologija',
                '08B':'Farmacija',
                '09B':'Visuomenės sveikata',
                '10B':'Slauga',

                '01T':'Elektros ir elektronikos inžinerija',
                '02T':'Statybos inžinerija',
                '03T':'Transporto inžinerija',
                '04T':'Aplinkos inžinerija',
                '05T':'Chemijos inžinerija',
                '06T':'Energetika ir termoinžinerija',
                '07T':'Informatikos inžinerija',
                '08T':'Medžiagų inžinerija',
                '09T':'Mechanikos inžinerija',
                '10T':'Matavimų inžinerija'}


HEADINGS_DF1=['dkt_vrd', 'dkt_dsc', 'dkt_ins', 'dkt_lps', 
             'dis_tem', 'dis_ant',
            'vdv_vrd', 'vdv_dsc', 'vdv_ins', 'vdv_pdl',
            'prm_vrd', 'prm_dsc', 'prm_ins', 'prm_pdl',
            'opn_vrd', 'opn_dsc', 'opn_ins', 'opn_pdl',
            'trb',
            'gyn_lks', 'gyn_vta'])

mylist = []
def mainALL():
    apie_viena_gynima = []
    for eilesnumeris in range(1,3185):
#        print "Skaitau1: ", eilesnumeris
        try:
            response = open("g:\Desktop\z\ON_HOLD\LMT DB proj\htmls\%s.html" % eilesnumeris) #htmls/%s.html
            html = response.read()
        
            skelbianti_institucija = re.findall(r'<div class="prevfld"><p class="fldname">Skelbianti institucija</p><p>(.+?)</p></div>', html)
            data_ir_laikas = re.findall(r'<div class="prevfld"><p class="fldname">Data ir laikas</p><p>(.+)</p></div>', html)
            vieta = re.findall(r'<div class="prevfld"><p class="fldname">Vieta</p><p>(.+?)</p></div>', html)
            doktorantas = re.findall(r'<div class="prevfld"><p class="fldname">Doktorantas</p><p>(.+?)</p></div>', html)
            tema = re.findall(r'<div class="prevfld"><p class="fldname">Tema</p><p>(.+?)</p></div>', html) #need to split tema ir saka
            parengta_institucijoje = re.findall(r'<div class="prevfld"><p class="fldname">Parengta institucijoje</p><p>(.+?)</p></div>', html)
            vadovas = re.findall(r'</div><div class="prevfld"><p class="fldname">Vadovas</p><p>(.*?)</div>', html) # re.findall(r'<div class="prevfld"><p class="fldname">Vadovas</p><p>(.+?)</p></div>')
            pirmininkas = re.findall(r'<div class="grfld"><span class="specfld">Pirmininkas</span>(.+?)</div>', html)
            nariai = re.findall(r'<div class="grfld">(.+?)</div>', html) #iki oponentai
            
            oponentai = re.findall(r'oponentai.*<div class="grfld">(.*?)(?=<)', html, re.DOTALL)
            
            anotacija = re.findall (r'<div class="fldanotation"><p class="fldname">\s*Anotacija\s*</p>\s*<div class="fldcontent">(.+?)</div>', html) # gal veiks..
            
            pateikimo_data = re.findall(r'</div><div class="prevfld"><p class="fldname">Pateikimo data</p><p>', html)
            
            
            #~ apie_viena_gynima.append([skelbianti_institucija,data_ir_laikas, vieta, doktorantas, tema, parengta_institucijoje,vadovas, pirmininkas, nariai, oponentai, anotacija, pateikimo_data])
            
            apie_viena_gynima.append(skelbianti_institucija)
            apie_viena_gynima.append(data_ir_laikas) ###events
            apie_viena_gynima.append(vieta) ### Eventas #prideti
            apie_viena_gynima.append(doktorantas) ### People Role
            apie_viena_gynima.append(tema) ### People
            apie_viena_gynima.append(parengta_institucijoje) ### People Institui
            apie_viena_gynima.append(vadovas) ### Role People     
            #~ apie_viena_gynima.append(rask_visa_komisija)
            apie_viena_gynima.append(pirmininkas) ### Role People
            apie_viena_gynima.append(nariai) ### Role People #################                 
            apie_viena_gynima.append(oponentai) ### Role People ################
            apie_viena_gynima.append(anotacija) ### People #prideti
            apie_viena_gynima.append(pateikimo_data) ### People #prideti
            
            mylist.append(apie_viena_gynima)
            apie_viena_gynima = []
            
        except Exception as e:
            print "nepavyko", eilesnumeris, str(e) 
            continue
    return mylist


rezultatas = mainALL() 

HEADINGS = ['skl_ins', 'data_lks', 'vieta', 'dkt',
            'tema', 'rng_ins', 'vdv', 'prm', 
            'nariai', 'taryba', 'opn', 'anotacija']

df = pd.DataFrame(rezultatas,columns=HEADINGS)

unlist = lambda l: l[0] if len(l) != 0 else None
unwrap = lambda l: unlist(l) if isinstance(l, list) else l
df = df.applymap(unwrap)

menesiai = {}
menesiai = {'sausio':'01',
            'vasario':'02',
            'kovo':'03',
            'balandžio':'04',
            'gegužės':'05',
            'birželio':'06',
            'liepos':'07',
            'rugpjūčio':'08',
            'rugsėjo':'09',
            'spalio':'10',
            'lapkričio':'11',
            'gruodžio':'12'}
df.data_lks.replace(menesiai, inplace=True, regex=True)

valymas = {'m. ':'-', ' ':'-'}
df.data_lks.replace(valymas, inplace=True, regex=True)

df.data_lks.replace('-d.*', '', inplace=True, regex=True)

df.data_lks = pd.to_datetime(df['data_lks'])
##
df['dkt_dsc'] = df['tema']
df.dkt_dsc.replace('\w.*\(', '', inplace=True, regex=True)
df.dkt_dsc.replace('\)', '', inplace=True, regex=True)
df.dkt_dsc.replace(' ', '_', inplace=True, regex=True)
df.dkt_dsc.replace('.*?(?=\d+)', '', inplace=True, regex=True)
df.dkt_dsc.replace('_', '', inplace=True, regex=True)
# Dar turime problemų, kai kurių sričių pradžiose yra neriekalingų simbolių, 
#tokių kaip '"','Į','Č','Ž',',,', o galbūt ir kitų. Juos galime palyginti lengvai atpažinti. 
#Po jų seka sričių pavadinimai iš didžiosios raidės.


# Pažiūrėkime į pirmininkas
df['prm_vrd'] = df['prm']
df['prm_dsc'] = df['prm']
#[x for x in df.prm_dsc.values]

##########

df.prm_dsc.replace('.*(?=0|1\d \w)','', inplace=True, regex=True)
df.prm_dsc.replace('.*(?=0|1\d\w)','', inplace=True, regex=True)
df.prm_dsc.replace('\)\.', '', inplace=True, regex=True)
df.prm_dsc.replace('\)', '', inplace=True, regex=True)
df.prm_dsc.replace('\;', '', inplace=True, regex=True)
df.prm_dsc.replace(' ','', inplace=True, regex=True)
df.prm_dsc.replace(',*?','', inplace=True, regex=True)
df.prm_dsc.replace(',','', inplace=True, regex=True)
df.prm_dsc.replace('VytautoDidžiojouniversitetas','', inplace=True, regex=True)
df.prm_dsc.replace('pirmininkas','', inplace=True, regex=True)
df.prm_dsc.replace('\.','', inplace=True, regex=True)
df.prm_dsc.replace('-','', inplace=True, regex=True)
df.prm_dsc.replace('\–','', inplace=True, regex=True)
df.prm_dsc.replace('Vilniausuniversitetas','', inplace=True, regex=True)
df.prm_dsc.replace(' ','', inplace=True, regex=True)
df.prm_dsc.replace('\xc2\x96','', inplace=True, regex=True)
df.prm_dsc.replace('Biochemijosinstitutas','', inplace=True, regex=True)



df.prm_vrd.replace('.*?dr\. ','', inplace=True, regex=True)

df.prm_vrd.replace(',.*','', inplace=True, regex=True)
df.prm_vrd.replace('tarybos pirmininkas.*?','', inplace=True, regex=True)
df.prm_vrd.replace('\(.*','', inplace=True, regex=True)
#df.prm_dsc.replace('(?:\d{2}\w{1}).*','', inplace=True,regex=True)
#[x for x in df.prm_dsc.values]

## apie vadova

df['vdv_vrd'] = df['vdv']
df['vdv_dsc'] = df['vdv']

df.vdv_dsc.replace('.*(?=\d{2} \w)','', inplace=True, regex=True)
df.vdv_dsc.replace('.*(?=\d{2}\w)','', inplace=True, regex=True)
df.vdv_dsc.replace(' ','', inplace=True, regex=True)
df.vdv_dsc.replace('</p>','', inplace=True, regex=True)
df.vdv_dsc.replace('\)','', inplace=True, regex=True)
df.vdv_dsc.replace(',.*?','', inplace=True, regex=True)
df.vdv_dsc.replace('-.*?','', inplace=True, regex=True)
df.vdv_dsc.replace('v.*?','', inplace=True, regex=True)
df.vdv_dsc.replace('O.*?','', inplace=True, regex=True)
df.vdv_dsc.replace('\..*?','', inplace=True, regex=True)
    
    
    

