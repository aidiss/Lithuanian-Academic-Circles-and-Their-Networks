#!/usr/bin/env python
# -*- coding: utf-8 -*-

dsc_list = ['01S', '02S', '03S', '04S', '05S', '06S', '07S', '08S',
            '01H', '02H', '03H', '04H', '05H', '06H', '07H', 
            '01T', '02T', '03T', '04T', '05T', '06T', '07T', '08T', '09T', '10T', 
            '01B', '02B', '03B', '04B', '05B', '06B', '07B', '08B', '09B', '10B',  
            '01P', '02P', '03P', '04P', '05P', '06P', '07P', '08P', '09P',
            '01A', '02A', '03A', '04A']

## 2012
# Lietuvos Respublikos švietimo ir mokslo ministro 2012 m. spalio 16 d.
# „Dėl mokslo krypčių patvirtinimo“ 
# ( Nr. V-1457)
smm2012      = {'01H':u'Filosofija',
                '02H':u'Teologija',
                '03H':u'Menotyra', 
                '04H':u'Filologija', 
                '05H':u'Istorija',
               # '06H':u'Komunikacija',
                '07H':u'Etnologija', 


                '01S':u'Teisė',
                '02S':u'Politikos mokslai',
                '03S':u'Vadyba',
                '04S':u'Ekonomika',
                '05S':u'Sociologija',
                '06S':u'Psichologija',
                '07S':u'Edukologija',
                '08S':u'Komunikacija ir informacija',

                '01P':u'Matematika',
                '02P':u'Fizika',
                '03P':u'Chemija',
                '04P':u'Biochemija',
                '05P':u'Geologija',
                '06P':u'Fizinė geografija',
                '07P':u'Paleontologija',
                '08P':u'Astronomija',
                '09P':u'Informatika',

                '01A':u'Agronomija',
                '02A':u'Veterinarija',
                '03A':u'Zootechnika',                
                '04A':u'Miškotyra',

                '01B':u'Biologija',
                '02B':u'Biofizika',
                '03B':u'Ekologija ir aplinkotyra',
                '04B':u'Botanika',
                '05B':u'Zoologija',
                '06B':u'Medicina',
                '07B':u'Odontologija',
                '08B':u'Farmacija',
                '09B':u'Visuomenės sveikata',
                '10B':u'Slauga',

                '01T':u'Elektros ir elektronikos inžinerija',
                '02T':u'Statybos inžinerija',
                '03T':u'Transporto inžinerija',
                '04T':u'Aplinkos inžinerija', # ir krastotvarka?
                '05T':u'Chemijos inžinerija',
                '06T':u'Energetika ir termoinžinerija',
                '07T':u'Informatikos inžinerija',
                '08T':u'Medžiagų inžinerija',
                '09T':u'Mechanikos inžinerija',
                '10T':u'Matavimų inžinerija'}  

## 2011
# Lietuvos Respublikos švietimo ir mokslo ministro 2011 m. vasario 14 d.
# įsakymas Nr. V-231 „Dėl mokslo krypčių ir šakų patvirtinimo“ 
# (Žin., 2011, Nr. 23-1123)
smm2011      = {'01H':u'Filosofija',
                '02H':u'Teologija',
                '03H':u'Menotyra', 
                '04H':u'Filologija', 
                '05H':u'Istorija',
                '06H':u'Komunikacija',
                '07H':u'Etnologija', 


                '01S':u'Teisė',
                '02S':u'Politikos mokslai',
                '03S':u'Vadyba',
                '04S':u'Ekonomika',
                '05S':u'Sociologija',
                '06S':u'Psichologija',
                '07S':u'Edukologija',
                '08S':u'Komunikacija ir informacija',

                '01P':u'Matematika',
                '02P':u'Fizika',
                '03P':u'Chemija',
                '04P':u'Biochemija',
                '05P':u'Geologija',
                '06P':u'Fizinė geografija',
                '07P':u'Paleontologija',
                '08P':u'Astronomija',
                '09P':u'Informatika',

                '01A':u'Agronomija',
                '02A':u'Veterinarija',
                '03A':u'Zootechnika',                
                '04A':u'Miškotyra',

                '01B':u'Biologija',
                '02B':u'Biofizika',
                '03B':u'Ekologija ir aplinkotyra',
                '04B':u'Botanika',
                '05B':u'Zoologija',
                '06B':u'Medicina',
                '07B':u'Odontologija',
                '08B':u'Farmacija',
                '09B':u'Visuomenės sveikata',
                '10B':u'Slauga',

                '01T':u'Elektros ir elektronikos inžinerija',
                '02T':u'Statybos inžinerija',
                '03T':u'Transporto inžinerija',
                '04T':u'Aplinkos inžinerija', # ir krastotvarka?
                '05T':u'Chemijos inžinerija',
                '06T':u'Energetika ir termoinžinerija',
                '07T':u'Informatikos inžinerija',
                '08T':u'Medžiagų inžinerija',
                '09T':u'Mechanikos inžinerija',
                '10T':u'Matavimų inžinerija'}


    
                
code_to_name =  {'01H':u'Filosofija',
                '02H':u'Teologija',
                '03H':u'Menotyra', 
                '04H':u'Filologija', 
                '05H':u'Istorija',
                '06H':u'NE TA KLASIFIKACIJA', #'06H':u'Komunikacija ir informacija',
                '07H':u'Etnologija', 

                '01S':u'Teisė',
                '02S':u'Politikos mokslai',
                '03S':u'Vadyba',
                '04S':u'Ekonomika',
                '05S':u'Sociologija',
                '06S':u'Psichologija',
                '07S':u'Edukologija',
                '08S':u'Komunikacija ir informacija',

                '01P':u'Matematika',
                '02P':u'Fizika',
                '03P':u'Chemija',
                '04P':u'Biochemija',
                '05P':u'Geologija',
                '06P':u'Fizinė geografija',
                '07P':u'Paleontologija',
                '08P':u'Astronomija',
                '09P':u'Informatika',

                '01A':u'Agronomija',
                '02A':u'Veterinarija',
                '03A':u'Zootechnika',
                '04A':u'Miškotyra',

                '01B':u'Biologija',
                '02B':u'Biofizika',
                '03B':u'Ekologija ir aplinkotyra',
                '04B':u'Botanika',
                '05B':u'Zoologija',
                '06B':u'Medicina',              #06B Agronomija
                '07B':u'Odontologija',          #07B Medicina 
                '08B':u'Farmacija',             #08B Stomatologija
                '09B':u'Visuomenės sveikata',   #09B Farmacija
                '10B':u'Slauga',                #10B Visuomenės sveikata
                '11B':u'NE TA KLASIFIKACIJA',   #11B Slauga
                '12B':u'NE TA KLASIFIKACIJA',   #12B Veterinarinė medicina
                '13B':u'NE TA KLASIFIKACIJA',   #13B Zootechnika
                '14B':u'NE TA KLASIFIKACIJA',   #14B Miškotyra

                '01T':u'Elektros ir elektronikos inžinerija',
                '02T':u'Statybos inžinerija',
                '03T':u'Transporto inžinerija',
                '04T':u'Aplinkos inžinerija',
                '05T':u'Chemijos inžinerija',
                '06T':u'Energetika ir termoinžinerija',
                '07T':u'Informatikos inžinerija',
                '08T':u'Medžiagų inžinerija',
                '09T':u'Mechanikos inžinerija',
                '10T':u'Matavimų inžinerija'}



#Lietuvos Respublikos švietimo ir mokslo ministro 2003 m. gegužės 28 d.
#įsakymą Nr. ISAK-743 „Dėl Švietimo ir mokslo ministerijos 
#1998 m. sausio 9 d. įsakymo Nr. 30 
#„Dėl mokslo sričių, krypčių ir šakų klasifikacijos“ pakeitimo“ 
#(Žin., 2003, Nr. 55-2475).


## Labai seni
#Lietuvos Respublikos švietimo ir mokslo ministerijos 
#1998 m. sausio 9 d. įsakymą Nr. 30 
#„Dėl mokslo sričių, krypčių ir šakų klasifikacijos“ 
#(Žin., 1998, Nr. 6-126);

#Lietuvos Respublikos švietimo ir mokslo ministerijos 
#1998 m. vasario 4 d. įsakymą Nr. 243 
#„Dėl Švietimo ir mokslo ministerijos 1998 m. sausio 9 d. įsakymo Nr. 30 „Dėl mokslo sričių, krypčių ir šakų klasifikacijos“ dalinio pakeitimo“ (Žin., 1998, Nr. 15-363);
#Lietuvos Respublikos švietimo ir mokslo ministro 1998 m. gruodžio 28 d.
#įsakymą Nr. 1588 „Dėl Švietimo ir mokslo ministerijos 1998 m. sausio 9 d. įsakymo Nr. 30 dalinio papildymo“ (Žin., 1999, Nr. 5-128);
