#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import re
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

def Apdorok(df, code_to_name): 
      # LAIKAS
      unlist = lambda l: l[0] if len(l) != 0 else None
      unwrap = lambda l: unlist(l) if isinstance(l, list) else l
      df = df.applymap(unwrap)
      
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



      import networkx as nx
      from itertools import chain
      pattern = '|'.join(code_to_name.keys())

      thelist = []
      thedict = {}
      for x in range(len(df)): 
          mylist = []
          try:
              for z in range(len(df.nariai[x])):
                  rez = re.findall(r'\d{2} ?[HSPTBA]', df.nariai[x][z])
                  rex = [g.replace(' ','') for g in rez]
                  mylist.append(rex)
          except:
              pass
          thelist.append(mylist)
          rax = list(chain(*mylist)) 
          thedict[x] = {'nar_dsc': rax}

      list2 = [filter(None, x) for x in thelist]
      list3 = filter(None, list2)

      df['nar_dsc'] = tuple(thedict[x]['nar_dsc'] for x in range(len(df)))

      DEF = df[(df.dkt_dsc.str.contains(pattern, na=False) 
          & df.prm_dsc.str.contains(pattern, na=False) 
          & df.vdv_dsc.str.contains(pattern, na=False))]

      DEF.loc[:,['dkt_dsc', 'vdv_dsc', 'prm_dsc', 'nar_dsc']].values

      PREP = DEF.loc[:,['dkt_dsc', 'vdv_dsc', 'prm_dsc', 'nar_dsc']].values
      prep = DEF.loc[:,'nar_dsc'].values
      return df

def palikTinkamus(df, dsc_list, kind='kodai'):
    ''' default pagal kodus, galima ir pagal pavadinimus'''
    if kind == 'kodai':
        return df[df.dkt_dsc.isin(dsc_list) & df.vdv_dsc.isin(dsc_list) & df.prm_dsc.isin(dsc_list)]
    if kind == 'pav':
        print "not implemented yet"

def PridekDiscPavadinimus(df, Unidecode=False, manualReplace=False):
    #dkt
    df.loc[:,'dkt_dsc_pav'] = df.tema.str.extract('.*(\(.*\))').str.rstrip(')BSHPTA 0123456789').str.lstrip('(')
    df.loc[:,'dkt_dsc_pav'] = df.loc[:,'dkt_dsc_pav'].str.lower()

    #vdv
    rez = df.vdv.str.extract('mokslai, (.*\))')
    rez = rez.str.rstrip(')BSHPTA 0123456789-, –(')
    rez = rez.str.lstrip(' ')

    rez = rez.str.replace('med\xc5\xbeiag\xc5\xb3 in\xc5\xbeineija', 'med\xc5\xbeaig\xc5\xb3 in\xc5\xbeinerija')
    rez = rez.str.replace('med\xc5\xbeiag\xc5\xb3 in\xc5\xbeineija', 'med\xc5\xbeiag\xc5\xb3 in\xc5\xbeinerija')
    rez = rez.str.replace('med\xc5\xbeaig\xc5\xb3 in\xc5\xbeinerija', 'med\xc5\xbeiag\xc5\xb3 in\xc5\xbeinerija')
    rez = rez.str.replace('aplinkos in\xc5\xbeinerija ir kra\xc5\xa1tovarka', 'aplinkos in\xc5\xbeinerija ir kra\xc5\xa1totvarka')
    rez = rez.str.replace('elektros ir eletkronikos in\xc5\xbeinerija', 'elektros ir elektronikos in\xc5\xbeinerija')
    rez = rez.str.replace('\xc2\x96','')
    rez = rez.str.replace('(\,.*)','')
    rez = rez.str.lstrip(' ')
    rez = rez.str.replace('( ?\d{2} .*)','')
    rez = rez.str.replace('\xe2\x80\x93','')
    rez = rez.str.replace('(06.*)','')
    rez = rez.str.replace(' (-.*)', '')
    rez = rez.str.replace(' ? ?\d{2}.*','')
    rez = rez.str.replace('eduklologija', 'edukologija')
    rez = rez.str.replace('edukologij', 'edukologija')
    rez = rez.str.rstrip(' ')
    rez = rez.str.replace('inforamtikos inzinerija', 'informatikos inzinerija')
    rez = rez.str.replace('mechanikos inzinerija', 'mechanikos in\xc5\xbeinerija')
    rez = rez.str.replace('veterinarija', 'veterinarine medicina') 
    df.loc[:,'vdv_dsc_pav'] = rez
    df.loc[:,'vdv_dsc_pav'] = df.loc[:,'vdv_dsc_pav'].str.lower()

    #prm
    rez = df.prm.str.extract('mokslai, (.*\))')
    rez = rez.str.rstrip(')BSHPTA 0123456789-, –(')
    rez = rez.str.lstrip(' ')

    rez = rez.str.replace('elektros ir eletkronikos in\xc5\xbeinerija', 'elektros ir elektronikos in\xc5\xbeinerija')
    rez = rez.str.replace('\xc2\x96','')
    rez = rez.str.replace('( ?\d{2} .*)','')
    rez = rez.str.replace(' (-.*)', '')
    rez = rez.str.replace('(06.*)','')
    rez = rez.str.rstrip(' -')
    rez = rez.str.replace('\\xe2\\x80\\x93 01b\, medicina','')
    rez = rez.str.replace('odontologijos','odontologija')
    rez = rez.str.replace('socialiniai mokslai, vadyba ir administravimas','vadyba ir administravimas')
    rez = rez.str.replace('zemes ukio mokslai', 'miskotyra') # blogas irasas 3643
    rez = rez.str.replace('inforamtikos inzinerija', 'informatikos inzinerija')
    rez = rez.str.replace('\xe2\x80\x93', '')
    rez = rez.str.replace('\d{2}.*','')
    rez = rez.str.replace('aplinkos in\xc5\xbeinerija', 'aplinkos in\xc5\xbeinerija ir kraštotvarka')
    rez = rez.str.replace('ir kraštotvarka ir kraštotvarka', 'ir kraštotvarka')
    rez = rez.str.replace('veterinarija', 'veterinarine medicina') 
    rez = rez.str.replace('vadyba', 'vadyba ir administravimas') 
    rez = rez.str.replace('ir administravimas ir administravimas', 'ir administravimas') 
    rez = rez.str.replace('adminstravimas ir vadyba ir administravimas', 'vadyba ir administravimas') 
    
        
    rez = rez.str.rstrip(' ')
    rez = rez.str.lstrip(' ')
    
    df.loc[:,'prm_dsc_pav'] = rez
    df.loc[:,'prm_dsc_pav'] = df.loc[:,'prm_dsc_pav'].str.lower()


    #opn
    rez = df.opn.str.extract('mokslai, (.*\))')
    rez = rez.str.replace('(,?-? *\d{2} *.*)','')
    rez = rez.str.replace('( ?–)','')
    rez = rez.str.replace('\xc2\x96','')
    rez = rez.str.replace('( \()','')
    rez = rez.str.replace('elektros ir elektronikos inzinierija', 'elektros ir elektronikos inzinerija')
    rez = rez.str.replace('medziagu inzinerija\)', 'medziagu inzinerija')
    rez = rez.str.replace('medziagu inzinierija', 'medziagu inzinerija')
    rez = rez.str.replace('aplinkos in\xc5\xbeinerija', 'aplinkos in\xc5\xbeinerija ir kraštotvarka')
    rez = rez.str.replace('ir kraštotvarka ir kraštotvarka', 'ir kraštotvarka')
    rez = rez.str.replace('veterinarija', 'veterinarine medicina')
    rez = rez.str.rstrip(')')

    rez = rez.str.rstrip(' ')
    rez = rez.str.lstrip(' ')
    df.loc[:,'opn_dsc_pav'] = rez
    df.loc[:,'opn_dsc_pav'] = df.loc[:,'opn_dsc_pav'].str.lower()
    
    if Unidecode == True:
        df.loc[:,'dkt_dsc_pav'] = df.loc[:,'dkt_dsc_pav'].str.decode('utf-8')
        df.loc[:,'vdv_dsc_pav'] = df.loc[:,'vdv_dsc_pav'].str.decode('utf-8')    
        df.loc[:,'prm_dsc_pav'] = df.loc[:,'prm_dsc_pav'].str.decode('utf-8')
        df.loc[:,'opn_dsc_pav'] = df.loc[:,'opn_dsc_pav'].str.decode('utf-8') 
        # df.loc[:,'opn_dsc_pav'] = unidecode(df.loc[:,'opn_dsc_pav'].str.decode('utf-8'))  # this doe snot work
    
    if manualReplace == True:
        littledict = {'ą':'a', 'č':'c', 'ę':'e', 'ė':'e', 'į':'i', 'š':'s', 'ų':'u', 'ū':'u', 'ž':'z'}
        for x in littledict:          
            df.loc[:,'dkt_dsc_pav'] = df.loc[:,'dkt_dsc_pav'].str.replace(x, littledict[x])
            df.loc[:,'vdv_dsc_pav'] = df.loc[:,'vdv_dsc_pav'].str.replace(x, littledict[x])  
            df.loc[:,'prm_dsc_pav'] = df.loc[:,'prm_dsc_pav'].str.replace(x, littledict[x])
            df.loc[:,'opn_dsc_pav'] = df.loc[:,'opn_dsc_pav'].str.replace(x, littledict[x])
    return df

def pridekStulpeliusApieVisuNariuDiscPavadinimus(df):
    rez = [' '.join(df.loc[x,'nariai']) for x in df.index]
    df.loc[:, 'nariaiBeTarpu'] = rez
    rez = df.nariaiBeTarpu.str.extract('(\(.*?\)).*?(\(.*?\)).*?(\(.*?\)).*?(\(.*?\)).*?(\(.*?\))',  re.DOTALL)
    
    littledict = {'ą':'a', 'č':'c', 'ę':'e', 'ė':'e', 'į':'i', 'š':'s', 'ų':'u', 'ū':'u', 'ž':'z'}
    for x in rez.columns:
        rez[x] = rez[x].str.replace('.*\,','')
        rez[x] = rez[x].str.rstrip(')BPTHSA 0123456798- ')
        rez[x] = rez[x].str.rstrip(')BPTHSA 0123456798- –')
        rez[x] = rez[x].str.replace('\(.*\)','')
        rez[x] = rez[x].str.replace('\xc2\x96','')
        rez[x] = rez[x].str.replace('\\xc2\\x96','')
        
        rez[x] = rez[x].str.rstrip(' ')
        rez[x] = rez[x].str.lstrip(' ')
       
        
        for z in littledict:          
            rez[x] = rez[x].str.replace(z, littledict[z])
            rez[x] = rez[x].str.replace(z, littledict[z])  
            rez[x] = rez[x].str.replace(z, littledict[z])
            rez[x] = rez[x].str.replace(z, littledict[z])
            
    for x in rez.columns:
                
        rez[x] = rez[x].str.replace(' ?\(.*','')
        rez[x] = rez[x].str.replace(' ?\d{2].*','')
        rez[x] = rez[x].str.replace('odontologijos', 'odontologija')
        rez[x] = rez[x].str.replace('\\tedukologija', 'edukologija')
        rez[x] = rez[x].str.replace('\\n agronomija', 'agronomija')
        rez[x] = rez[x].str.replace('\\n.*','')
        rez[x] = rez[x].str.replace('\\xe2\\x80\\x93.*','')
        rez[x] = rez[x].str.replace('mechanikos inznerija', 'mechanikos inzinerija')
        rez[x] = rez[x].str.replace('\\\n','')
        rez[x] = rez[x].str.replace('\\tpsichologija', 'psichologija')
        rez[x] = rez[x].str.replace('elektros ir elektronikos inzinierija', 'elektros ir elektronikos inzinerija')
        rez[x] = rez[x].str.replace('elektros ir elektronikos inznerija', 'elektros ir elektronikos inzinerija')
        rez[x] = rez[x].str.replace('polikos mokslai', 'politikos mokslai')
        rez[x] = rez[x].str.replace('transporto  inzinerija', 'transporto inzinerija')
        rez[x] = rez[x].str.replace('transporto inznerija', 'transporto inzinerija')
        rez[x] = rez[x].str.replace('vadyba ir adminsitravimas', 'vadyba ir administravimas')
        rez[x] = rez[x].str.replace('elektros ir elektronikos inznerija', 'elektros ir elektronikos inzinerija')
        rez[x] = rez[x].str.replace('elektros ir elektronikos inzinierija', 'elektros ir elektronikos inzinerija')
        rez[x] = rez[x].str.replace('elektros ir elektronikos inznerija', 'elektros ir elektronikos inzinerija')
        rez[x] = rez[x].str.replace('technologijos kos inzinerija ir krastotvarka', 'aplinkos inzinerija ir krastotvarka') # 1421 lmt  klaida
        rez[x] = rez[x].str.replace('aplinkos inzinerija', 'aplinkos inzinerija ir krastotvarka')
        rez[x] = rez[x].str.replace('ir krastotvarka ir krastotvarka', 'ir krastotvarka')
        rez[x] = rez[x].str.replace('inzinierija', 'inzinerija')  
        
        rez[x] = rez[x].str.replace('Etnologija', 'etnologija') 
        rez[x] = rez[x].str.replace('geografija', 'fizine geografija')
        rez[x] = rez[x].str.replace('fizine fizine', 'fizine') 
        rez[x] = rez[x].str.replace('vadyba', 'vadyba ir administravimas') 
        rez[x] = rez[x].str.replace('ir administravimas ir administravimas', 'ir administravimas') 
        rez[x] = rez[x].str.replace('adminstravimas ir vadyba ir administravimas', 'vadyba ir administravimas') 
        rez[x] = rez[x].str.replace('chemija inzinerija', 'chemijos inzinerija')
        
        rez[x] = rez[x].str.replace('veterinarija', 'veterinarine medicina') 

        rez[x] = rez[x].str.replace('informatikos', 'informatikos inzinerija')
        rez[x] = rez[x].str.replace('inzinerija inzinerija', 'inzinerija')
        
        rez[x] = rez[x].str.replace('ekologija ir aplinkosauga', 'ekologija ir aplinkotyra')

        rez[x] = rez[x].str.replace('politologija', 'politikos mokslai') 
        
        
        
        rez[x] = rez[x].str.replace('edklogija','eduklogija')
        rez[x] = rez[x].str.replace('eduklogija','eduklogija') 
        rez[x] = rez[x].str.replace('fizika -o','fizika') 
        rez[x] = rez[x].str.replace('\-', '') 
        rez[x] = rez[x].str.replace(' o', '')
        
        rez[x] = rez[x].str.lower()
        rez[x] = rez[x].str.rstrip(' ')
        rez[x] = rez[x].str.lstrip(' ')
    df = pd.concat([df,rez],axis =1)
    
    return df


#df.loc[:, 'opn_dsc_pav'].unique()
