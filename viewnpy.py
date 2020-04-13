#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import dg
import datagenerate as dgg

view = np.load('surface/openn.npy',allow_pickle = True)
close = np.load('surface/close.npy',allow_pickle = True)
firmlist = list(np.load("surface/firmlist.npy",allow_pickle = True))


rsv = dg.rsv(close,9,True)
rsv9 = np.load('surface/rsv9.npy',allow_pickle = True)
k = dgg.decay(rsv,3)
k9 = np.load('surface/k9.npy',allow_pickle = True)
output = pd.DataFrame(rsv)
output2 = pd.DataFrame(rsv9)
d = dgg.decay(k,3)
d9 = np.load('surface/d9.npy',allow_pickle = True)
print(d)
print(d9)