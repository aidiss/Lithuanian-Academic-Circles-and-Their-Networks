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
                '06H':'KOMUNIKACIJA IR BALALAIKOS',  
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
              'gyn_lks', 'gyn_vta']

mylist = []
def mainALL():
    apie_viena_gynima = []
    for eilesnumeris in range(1,3185):
#        print "Skaitau1: ", eilesnumeris
        try:
            response = open("g:\Desktop\z\ON_HOLD\LMT DB proj\htmls\%s.html" % eilesnumeris) #htmls/%s.html
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
            nariai = re.findall(r'<div class="grfld">(.+?)(?:<\/div><\/div>)', html) 
            oponentai = re.findall(r'oponentai.*<div class="grfld">(.*?)(?=<)', html, re.DOTALL)
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


rezultatas = mainALL() 

HEADINGS = ['skl_ins', 'data_lks', 'vieta', 'dkt',
            'tema', 'rng_ins', 'vdv', 'prm', 
            'nariai', 'opn', 'anotacija', 'pateikimo_data','mokslo_saka']

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
        
# LAIKAS
df.data_lks.replace(menesiai, inplace=True, regex=True)
valymas = {'m. ':'-', ' ':'-'}
df.data_lks.replace(valymas, inplace=True, regex=True)
df.data_lks.replace('-d.*', '', inplace=True, regex=True)
df.data_lks = pd.to_datetime(df['data_lks'])

# DOKTORANTAS
df['dkt_dsc'] = df['tema']
df.dkt_dsc.replace('\w.*\(', '', inplace=True, regex=True)
df.dkt_dsc.replace('\)', '', inplace=True, regex=True)
df.dkt_dsc.replace(' ', '_', inplace=True, regex=True)
df.dkt_dsc.replace('.*?(?=\d+)', '', inplace=True, regex=True)
df.dkt_dsc.replace('_', '', inplace=True, regex=True)


# PIRMININKAS
df['prm_vrd'] = df['prm']
df['prm_dsc'] = df['prm']

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
df.prm_vrd.replace('prof|Prof|dr.|Dr.|Doc.|doc.|habil.|', '', inplace=True, regex=True)
df.prm_vrd.replace(r'tarybos|pirminink\xc4\x97|\xc2\x96', '', inplace=True, regex=True)
df.prm_vrd = df.prm_vrd.str.lstrip('.| |-')
df.prm_vrd = df.prm_vrd.str.rstrip('.| |-')

## VADOVAS
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

df.vdv_dsc.replace('VytautoDid\xc5\xbeiojouniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('VilniausGediminotechnikosuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Matematikosirinformatikosinstitutas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietuosmi\xc5\xa1k\xc5\xb3institutas','', inplace=True, regex=True)
df.vdv_dsc.replace('VytautoDid\xc5\xbeiojouniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietui\xc5\xb3kalbosinstitutas','', inplace=True, regex=True)
df.vdv_dsc.replace('Klaipedosuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lodz\xc4\x97suniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Vilniausuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('\(moksliniskonsultantas','', inplace=True, regex=True)
df.vdv_dsc.replace('moksliniskonsultantas','', inplace=True, regex=True)
df.vdv_dsc.replace('Kauotechnologijosuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('hajouniersitetasJAV','', inplace=True, regex=True)
df.vdv_dsc.replace('Klaip\xc4\x97dosuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Ro\xc4\x8desteriouniersitetasJAV','', inplace=True, regex=True)
df.vdv_dsc.replace('Klaip\xc4\x97dosuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietui\xc5\xb3literat\xc5\xabrosirtautosakosinstitutas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietuosistorijosinstitutas','', inplace=True, regex=True)
df.vdv_dsc.replace('Kult\xc5\xabrosfilosofijosirmenoinstitutas','', inplace=True, regex=True)
df.vdv_dsc.replace('MRiomeriouniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Vilniauspedagoginisuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietuosmi\xc5\xa1k\xc5\xb3isntitutas','', inplace=True, regex=True)
df.vdv_dsc.replace('Vilniausuniersiteto','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietuoskult\xc5\xabrostyrim\xc5\xb3institutas','', inplace=True, regex=True)
df.vdv_dsc.replace('Latijosuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietuoskult\xc5\xabrostyrim\xc5\xb3institutas','', inplace=True, regex=True)
df.vdv_dsc.replace('Vytautodid\xc5\xbeiojouniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietuosedukologijosuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietuosseikatosmoksl\xc5\xb3uniersitetoKardiologijosinstitutas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietuosedukologijosuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Kaunotechnologijosuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('KLaip\xc4\x97dosuniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('MykoloRomeriouniersitetas','', inplace=True, regex=True)
df.vdv_dsc.replace('Lietuosagrarini\xc5\xb3irmi\xc5\xa1k\xc5\xb3moksl\xc5\xb3centras','', inplace=True, regex=True)
df.vdv_dsc = df.vdv_dsc.str.rstrip(' ;0')
    


df.nariai = df.nariai.str.split(r'</div><div class="grfld">')
#df.nariai.replace('<span class="specfld">Pirmininkas</span>-','', inplace=True, regex=True)
#df.nariai.replace('prof|Prof|dr.|Dr.|Doc.|doc.|habil.|', '', inplace=True, regex=True)
#df.nariai = df.nariai.str.lstrip('.1.\t')
#df.nariai = df.nariai.str.rstrip(' ')
#df.nariai.replace('|'.join(df.rng_ins.dropna().values), '', inplace=True, regex=True)

