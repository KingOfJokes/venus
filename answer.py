#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime
import re
import math
import pickle
import system
from pandas.plotting import register_matplotlib_converters
plt.style.use('ggplot')
register_matplotlib_converters()
#Block1:define filter
#Block2:import data
#Block3:Create Positions

def showdata(backtest_inf,title,subtitle):
	print('Annual Return:','%.2f'%(100*backtest_inf['annualyield']),'%')
	print('Annual Std.','%.2f'%(100*backtest_inf['annualstd']),'%')
	print('Sharpe:','%.2f'%backtest_inf['sharpe'])
	print('Turnover rate:','%.2f'%(100*backtest_inf['turnover']),'%')
	print('Longest DD:',backtest_inf['longestdd'])
	print('Maximum DD:','%.2f'%(100*backtest_inf['maximumdd']),'%')

	current_time = datetime.now().strftime('%Y%m%d_%H%M%S')

	plt.title('Backtest Summary - '+title+' '+subtitle)
	plt.plot(backtest_inf['dates'], backtest_inf['assets'], label = 'Strategy')
	#plt.plot(backtest_inf['dates'], backtest_inf['historicalhigh'], label = 'Cap')
	plt.legend(loc='upper left')
	plt.savefig('C://Users/Ryan/Desktop/backtest/'+current_time)
	plt.show()
	plt.close()

removeh = 50 #去頭(部分資料缺乏初始值)
valid = 100 #去尾(做validfy)
def selectmode(num):
	if num == 1: #自選模式，去system改filter
		system.dataimport()
		system.datacreate()
		positions = system.positionize()
		#positions = systerm.ranknize(positions) #按照大小給予權重1/n、2/n......
		#positions = system.longize(positions,5) #看有沒有要使用加長功能(即買入部位之後，是否要至少持有n天)
		#positions = system.neutralize(positions) #使部位的價金為0，實現風險中立
		positions = system.shareize(positions) #轉換成買入張數
		print('Position generated.')
		backtest_inf = system.backtest(positions,removeh,valid)[0]
		valid_inf = system.backtest(positions,removeh,valid)[1]
		distribution = system.backtest(positions,removeh,valid)[2]
	elif num == 2: #模組模式，在這裡改底下的ifs
		ifs = [['fore','+','fore','>=',200,1,3],['yoy','+','yoy','>',0,1,1],['vma10','+','vma10','>',1000,1,1]] #[data1,運算子,data2,比較子,比較值,過去第n天~m天]
		system.dataquery(ifs)
		positions = system.positionize2(ifs,'signal2') #條件、符合者的權重(1 for 等量、'openn' for price、'signalx' for alpha signalx)
		#positions2 = systerm.ranknize(positions) #按照大小給予權重1/n、2/n......
		positions = system.longize(positions,1) #看有沒有要使用加長功能(即買入部位之後，是否要至少持有n天)
		positions = system.neutralize(positions) #使部位的價金為0，實現風險中立
		positions = system.shareize(positions) #轉換成買入張數
		print('Position generated.')
		result = system.backtest(positions,removeh,valid)
		backtest_inf = result[0]
		valid_inf = result[1]
		distribution = result[2]

	print('In-sample')
	showdata(backtest_inf,'F3>100,RY1>0','IS')
	print('Out-sample')
	showdata(valid_inf,'F3>100,RY1>0','OS')

	print('Description of each bet')
	distribution_pd = pd.DataFrame(distribution)
	distribution_np = np.asarray(distribution)
	print(distribution_pd.describe())
	plt.hist(distribution_np,bins=50,range=(-0.2,0.2)) 
	plt.title("Distribution") 
	plt.show()
	
	
a = time.time()
#selectmode(1)
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
