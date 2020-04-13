#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import math
import pickle
import system
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#Block1:define filter
#Block2:import data
#Block3:Create Positions

def showdata(backtest_inf):
	print('Annual Return:','%.2f'%(100*backtest_inf['annualyield']),'%')
	print('Annual Std.','%.2f'%(100*backtest_inf['annualstd']),'%')
	print('Sharpe:','%.2f'%backtest_inf['sharpe'])
	print('Longest DD:',backtest_inf['longestdd'])
	print('Maximum DD:','%.2f'%(100*backtest_inf['maximumdd']),'%')

	plt.title('Backtest Summary - Strategy')
	plt.plot(backtest_inf['dates'], backtest_inf['assets'], label = 'Strategy')
	plt.plot(backtest_inf['dates'], backtest_inf['historicalhigh'], label = 'Cap')
	plt.legend(loc='upper left')
	plt.savefig('C://Users/Ryan/Desktop/backtest/s20200303a')
	plt.show()
	plt.close()


removeh = 50 #去頭(部分資料缺乏初始值)
valid = 100 #去尾(做validfy)
def selectmode(num):
	if num == 1: #自選模式，去system改filter
		system.dataimport()
		system.datacreate()
		positions = system.positionize(removeh)
		#positions = systerm.rank(positions) #按照大小給予權重1/n、2/n......
		#positions = system.fade(positions,5) #看有沒有要使用fade功能(即買入部位之後，是否要至少持有n天)
		backtest_inf = system.backtest(positions,removeh,valid)
		valid_inf = system.validfy(positions,removeh,valid)
	elif num == 2: #模組模式，在這裡改底下的ifs
		ifs = [['k9','-','d9','>=',0,1,1]] 
		system.dataquery(ifs)
		positions2 = system.positionize2(removeh,ifs,1) #(去頭天數、去尾天數、符合訊號的權重)
		#positions2 = systerm.rank(positions2) #按照大小給予權重1/n、2/n......
		#positions2 = system.fade(positions2,5) #看有沒有要使用fade功能(即買入部位之後，是否要至少持有n天)
		backtest_inf = system.backtest(positions2,removeh,valid)
		valid_inf = system.validfy(positions2,removeh,valid)

	showdata('In-sample:',backtest_inf)
	showdata('Out-sample:',valid_inf)

a = time.time()
selectmode(1)
b = time.time()
print(b-a)

a = time.time()
selectmode(2)
b = time.time()
print(b-a)


'''
print("Current Portfolio:")
firmlist = list(np.load("surface/firmlist.npy",allow_pickle = True))
for f in range(len(position_matrix[len(positions)-1])):
	if positions[len(positions)-1][f] != 0:
		print(firmlist[f],'https://www.fugle.tw/ai/'+str(firmlist[f]))
'''
