"""
Classifications
========

    Classifications (NX) is a Python package for the comaprison of 
    classifications of academic and science disciplines, branches and 
    fields..

    No website yet

Using
-----

    Just write in Python

    >>> import clasisifactions as cl
    >>> cl.compare(G, H)

"""
#    Copyright (C) 2014 by
#    Aidis Stukas <aidiss@gmail.com>

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from numpy import corrcoef, sum, log, arange
from numpy.random import rand
from pylab import pcolor, show, colorbar, xticks, yticks

import sys
if sys.version_info[:2] < (2, 7):
    m = "Python 2.7 or later is required for classifications (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

# Release data
#from classifications import release

__author__   = 'Aidis Stukas'
#__license__  = release.license

#__date__ = release.date
#__version__ = release.version

#These are import orderwise

#import classifications.draw1
from classifications.dicts import *

#pandas
from classifications.import_classification import import_lmt
from classifications.import_classification import import_smm
from classifications.get_matrix import get_matrix
from classifications.analyse import get_num_of_interdir_branches
from classifications.analyse import get_num_of_interdir_branches
from classifications.analyse import get_num_of_branches
from classifications.analyse import get_num_of_unq_branches
from classifications.analyse import get_num_of_dirs
from classifications.analyse import get_num_of_interfield_branches

#networkx
from classifications.create_graph import create_graph

#matplotlib.pyplot
from classifications.create_plot import create_plot
from classifications.create_plot import create_plot1
from classifications.get_color import get_node_colors
from classifications.get_color import get_edge_colors


#mpld3
from d3_export import d3_export
