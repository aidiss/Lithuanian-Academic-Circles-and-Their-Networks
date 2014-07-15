# coding: utf-8
#!/usr/bin/env python

import re
import csv
import pandas as pd

def scrape_those_htmls(): #is MII LT
    Extract_from_html(html)
    print html
    #~ url = "C:\Users\Saonkfas\www.mokslas.mii.lt\mokslas\SRITYS"
    #~ url = "C:\Users\Saonkfas\www.mokslas.mii.lt\mokslas\SRITYS\b\duom00.php@pav=A&sritis="
    #~ url ="C:\Users\Saonkfas\www.mokslas.mii.lt\mokslas\SRITYS\%s\duom00.php@pav=%s&sritis=" % (ftbhs, abecele)
    url = r"\www.mokslas.mii.lt"
    
    rask_bloka = "<li>.*?<li>" #finds a set about one person
    rask_varda = "daktaras <b>(.+?)</b>" #returns name 
    rask_dis_pav = "<b>Disertacija</b>: (.*?)<br>" #returns name of dissertation
    rask_moksl_laipsn = "Mokslo laipsnis</b>: (.+?)<br>" #returns "daktaras" or "habilituotas daktaras"
    rask_gyn_dat = "Gynimo data</b>:(.+?)<br>" #returns date of birth
    rask_moksl_krypt = "Mokslo kryptis</b>: (.+?)<br>" #returns branch of science
    rask_instituc = "<b>Institucija</b>: (.+?)</ul>" #return institution 
    sujunk_radiniu_bloka = [name, dis_name, dis_level, 
                            defence_date, institution]
    print sujunk_radiniu_bloka

def html_to_one_txt():
    abecele = ["a", u"ą", "b", "c", u"č", "d", "e", u"ę", 
               u"ė", "f", "g", "h", "i", "y", u"į", "j", 
               "k", "l", "m", "n", "o", "p", "r", "s", 
               "š", "t", "u", u"ų", u"ū", "v", "z", u"ž"] 
    sritys = ["H", "S", "F", "T", "B"]
    count = 0
    ret = []
    for sritis in sritys:
        for letter in abecele:
            try:
                fr = open(r"www.mokslas.mii.lt\mokslas\SRITYS\{}\duom00.php@pav={}&sritis=".format(sritis,letter), 'r')
                html = fr.read()
                apie_kiekviena = re.findall('daktaras <b>.*?</ul><p><li>', html, re.UNICODE)
                ret.extend(apie_kiekviena)
            except:
                pass
    return ret

def from_raw_to_clean(raw):
    ret = []
    html = raw
    cleaned = []
    regexx = r"<b>(.*?)</b> <ul><b>Disertacija</b>: (.*?)<br><b>Mokslo laipsnis</b>: (.*?)<br><b>Gynimo data</b>: (.*?)<br><b>Mokslo kryptis</b>: (.*?)<br><b>Institucija</b>:(.*?)</ul><p><li>"
    cleaned = re.findall(regexx, html, re.UNICODE)
    for x in cleaned:
        ret.append(x)
    return ret
    
def tvarkyk(df):
    df.dkt_dsc.replace(' ','', regex=True, inplace=True)
    df.data_lks.replace('.','-',inplace=True)
    df.data_lks = pd.to_datetime(df['data_lks'])

    df.sort('data_lks',axis=0, ascending=True, inplace=True)
    df.drop_duplicates(inplace=True)
    df.index = range(1,len(df) + 1)

    encoding_dict = {r'\xf0':'š', r'\xf8':'ų', r'\xe8':'č', r'\xfe':'ž', r'\xeb':'ė', 
                     r'\xfb':'ū', r'\xd0':'Š', r'\xe1':'į', r'\xc8':'Č', r'\xdb':'Ū', 
                     r'\xde':'Ž', r'\xe0':'ą', r'\xe6':'ę', r'\xc1':'Į', r'\xcb':'Ė' }
    df.replace(encoding_dict, regex=True, inplace=True)
    return df
