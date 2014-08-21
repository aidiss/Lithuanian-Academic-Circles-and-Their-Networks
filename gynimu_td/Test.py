#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unidecode import unidecode
def pavadinimus(List, klasifikacija):
    mylist = []
    values = [unidecode(x.lower()) for x in klasifikacija.values()]
    for x in List:
        if x in values:
            pass
        else:
            mylist.append(x)
    return mylist
