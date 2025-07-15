#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 18:39:04 2025

@author: ignacio
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
k=10
Q=20

R=20
C=1
C2=1
R5=1
R3=1
R4=9
R1=9

ww=20000*np.pi
wz=1591

R=R*wz
R5=R5*wz
R3=R3*wz
R4=R4*wz
R1=R1*wz
C=C*(1/(ww*wz))
C2=C2*(1/(ww*wz))

#my_tf = TransferFunction( [1*(w0/Q)*k,0], [1, (w0/Q), w0] )
my_tf = TransferFunction( [(1/(C*R))*((R4/R5)+1),0], [1, (1/(C*R)), R4/(C2*C*R1*R3*R5)] )


plt.close('all')

bodePlot(my_tf, fig_id=1)

pzmap(my_tf, fig_id=2) #S plane pole/zero plot

GroupDelay(my_tf, fig_id=3)