# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('/home/ignacio/Escritorio/Facultad/2025/TC2/TC2_Virtual/lib/python3.12/site-packages')


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

w0 = 1
k=1

my_tf = TransferFunction( [1,-(k*w0)], [1, w0] )


plt.close('all')

bodePlot(my_tf, fig_id=1 )

pzmap(my_tf, fig_id=2) #S plane pole/zero plot

GroupDelay(my_tf, fig_id=3)

