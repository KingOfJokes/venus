#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import math
import pickle
import dg
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def filter(d,f):
	#purify
	#print(type(dataset['close']))
	for i in range(0,6): #新股上市前5天容易失真
		if math.isnan((dataset['close'])[d-i,f]) == True: 
			return 0

	for i in range(1,2):
		#secure meaningful compare
		if math.isnan((dataset['k9'])[d-1,f]) == True or math.isnan((dataset['d9'])[d-1,f]) == True:
			return 0

		if dataset['k9'][d-i,f] - dataset['d9'][d-i,f] < 0 :
			return 0
	#Those which buy
	weight = 1	
	return weight
dataset = {
	'close0050':[],
	'openn0050':[],
	'adjopenn':[],
	'adjclose':[],
	'openn':[],
	'high':[],
	'low':[],
	'close':[],
	'volume':[],
	'turnover':[],
	'outstand':[],
	'mktc':[],
	'pe':[],
	'pb':[],
	'cdy':[],
	'fore':[],
	'it':[],
	'dler':[],
	'foreratio':[],
	'itratio':[],
	'dlerratio':[],
	'managerratio':[],
	'mortratio':[],
	'finb':[],
	'shortb':[],
	'fsratio':[],
	'rsv9':[],
	'k9':[],
	'd9':[],
	'ema12':[],
	'ema26':[],
	'dif':[],
	'dem':[],
	'bar':[],
	'ma5':[],
	'ma10':[],
	'ma20':[],
	'ma60':[],
	'ma120':[],
	'ma240':[],
	'vma5':[],
	'vma10':[],
	'vma20':[],
	'vma60':[],
	'vma120':[],
	'vma240':[],
	'ma13':[],
	'ma21':[],
	'ma55':[],
	'totalers':[],
	'ers1':[],
	'ers1to5':[],
	'ers5to10':[],
	'ers10to15':[],
	'ers15to20':[],
	'ers20to30':[],
	'ers30to40':[],
	'ers40to50':[],
	'ers50to100':[],
	'ers100to200':[],
	'ers200to400':[],
	'ers400to600':[],
	'ers600to800':[],
	'ers800to1000':[],
	'ers1000plus':[],
	'ratio1':[],
	'ratio1to5':[],
	'ratio5to10':[],
	'ratio10to15':[],
	'ratio15to20':[],
	'ratio20to30':[],
	'ratio30to40':[],
	'ratio40to50':[],
	'ratio50to100':[],
	'ratio100to200':[],
	'ratio200to400':[],
	'ratio400to600':[],
	'ratio600to800':[],
	'ratio800to1000':[],
	'above1000ratio':[],
	'totalerscombo':[],
	'to50ratio':[],
	'to50ratiocombo':[],
	'to100ratio':[],
	'to100ratiocombo':[],
	'above400ratio':[],
	'above400ratiocombo':[],
	'above1000ratiocombo':[],
	'per1000pluser':[],
	'ers400plus':[],
	'per400pluser':[],
	'other400':[],
	'other400combo':[],
	'publish':[],
	'rev':[],
	'lyrev':[],
	'yoy':[],
	'mom':[],
	'accrev':[],
	'accrevyoy':[],
	'yoycombo':[],
	'momcombo':[],
	'accrevyoycombo':[],
	'breakhigh':[],
	'cash':[],
	'conta':[],
	'ar':[],
	'inv':[],
	'ca':[],
	'ppe':[],
	'nca':[],
	'totala':[],
	'shortdebt':[],
	'contl':[],
	'ap':[],
	'cl':[],
	'longdebt':[],
	'ncl':[],
	'totall':[],
	'equitycap':[],
	'quarrev':[],
	'gross':[],
	'opex':[],
	'rdex':[],
	'opgain':[],
	'incomebeftax':[],
	'eps':[],
	'roe':[],
	'grossmargin':[],
	'opmargin':[],
	'ibtmargin':[],
	'iatmargin':[],
	'opexmargin':[],
	'rdexmargin':[],
	'curratio':[],
	'quickratio':[],
	'debtratio':[],
	'arday':[],
	'invday':[],
	'apday':[],
	'grossmargindy':[],
	'grossmargindq':[],
	'opmargindy':[],
	'opmargindq':[],
	'iatmargindy':[],
	'iatmargindq':[],
	'ibtmargindy':[],
	'ibtmargindq':[],
	'ardaydy':[],
	'ardaydq':[],
	'invdaydy':[],
	'invdaydq':[],
	'apdaydy':[],
	'apdaydq':[],
	'debtratiody':[],
	'debtratiodq':[],
	'quickratiody':[],
	'quickratiodq':[],
	'roedy':[],
	'roedq':[]
}
load_needed = ['close','adjopenn','adjclose'] #這邊要把底下filter要呼叫的資料庫打進來
def dataimport():
	for data_name in load_needed:
		dataset[data_name] = np.load("surface/"+data_name+".npy",allow_pickle = True)

def datacreate():
	dataset['rsv9'] = dg.rsv(dataset['close'],9,True)
	dataset['k9'] = dg.decay(dataset['rsv9'],3)
	dataset['d9'] = dg.decay(dataset['k9'],3)
	
#Block1:define filter
#ifs = [[df1,com,df2,choice_compare.get(),float(entrybound.get()),int(reviewday.get())]]

def filter2(d,f,ifs,wei):
	#purify
	for i in range(0,6):
		if math.isnan((dataset['close'])[d-i,f]) == True: 
			return 0

	def value(df1,df2,a,sign):
		if sign == '+':
			return dataset[df1][d-a,f]+dataset[df2][d-a,f]
		elif sign == '-':
			return dataset[df1][d-a,f]-dataset[df2][d-a,f]
		elif sign == '*':
			return dataset[df1][d-a,f]*dataset[df2][d-a,f]
		elif sign == '/':
			return dataset[df1][d-a,f]/dataset[df2][d-a,f]

	#Those which don't buy
	for if_sit in ifs:
		for i in range(if_sit[5],if_sit[6]+1):
			#secure meaningful compare
			if math.isnan((dataset[if_sit[0]])[d-1,f]) == True or math.isnan((dataset[if_sit[2]])[d-1,f]) == True:
				return 0
			if if_sit[3] == '<':
				if value(if_sit[0],if_sit[2],i,if_sit[1]) >= if_sit[4] :
					return 0
			elif if_sit[3] == '>':
				if value(if_sit[0],if_sit[2],i,if_sit[1]) <= if_sit[4] :
					return 0
			elif if_sit[3] == '>=':
				if value(if_sit[0],if_sit[2],i,if_sit[1]) < if_sit[4] :
					return 0
			elif if_sit[3] == '<=':
				if value(if_sit[0],if_sit[2],i,if_sit[1]) > if_sit[4] :
					return 0
			elif if_sit[3] == '=':
				if value(if_sit[0],if_sit[2],i,if_sit[1]) != if_sit[4] :
					return 0
	#Those which buy
	weight = wei
	return weight


#Block2:import data
tdlist = list(np.load("surface/tdlist.npy",allow_pickle = True))
firmlist = list(np.load("surface/firmlist.npy",allow_pickle = True))
dataset['close0050'] = np.load("surface/close0050.npy",allow_pickle = True)
dataset['openn0050'] = np.load("surface/openn0050.npy",allow_pickle = True)

def dataquery(input_ifs):
	load_needed = ['close','adjopenn','adjclose']
	for if_sit in input_ifs:
		load_needed.append(if_sit[0])
		load_needed.append(if_sit[2])
	load_needed = list(set(load_needed))

	for data_name in load_needed:
		dataset[data_name] = np.load("surface/"+data_name+".npy",allow_pickle = True)

def showinf(field,date,firm):
	if field in dataset:
		print(str(field)+':',dataset[field][date,firm])

#Block3:Create Positions

#temp_position_matrix = np.asarray([0 for x in range(len(firmlist))])
def rank(ndarr):
	output = []
	for i in range(len(ndarr)):
		temp = [0 for i in range(len(ndarr[i]))]
		ranking = np.argsort(ndarr[i])
		start = 1
		for ind in range(len(ranking)):
			if ndarr[i,ranking[ind]] == 0:
				pass
			else:
				temp[ranking[ind]] = start
				start  = start + 1
		output.append(temp)
	output = np.asarray(output)
	return(output)
	
def fade(nparray,day): #day should be more than 2
	#給定array, 吐出一個把每個非0元至少自動持續day天，要從後面往前，不然會更新錯
	upperbound =len(nparray)-1 
	for d in range(upperbound,-1,-1):
		for f in range(len(nparray[d])):
			if nparray[d,f] != 0 and day >= 2:
				for i in range(d+1,min(upperbound,d+day)):
					if nparray[i,f] == 0:
						nparray[i,f] = nparray[d,f]
	return nparray

def normalize(nparray):
	summation = 0
	#validnumber = 0
	for i in nparray:
		if math.isnan(i)==False:
			summation = summation + i
			#validnumber = validnumber + 1
	if summation != 0:
		nparray = nparray/abs(summation)
	return nparray
def parrel(nparray,delta):
	return nparray-delta

def positionize(removehead):
	position_matrix = []
	for d in range(removehead,len(tdlist)):

		temp_position_matrix = []
		for f in range(len(firmlist)):
			temp_position_matrix.append(filter(d,f))
		temp_position_matrix = normalize(np.asarray(temp_position_matrix))
		position_matrix.append(temp_position_matrix)
	position_matrix = np.asarray(position_matrix)
	return position_matrix

def positionize2(removehead,input_ifs,wei):
	position_matrix = []
	for d in range(removehead,len(tdlist)):
		temp_position_matrix = []
		for f in range(len(firmlist)):
			temp_position_matrix.append(filter2(d,f,input_ifs,wei))
		temp_position_matrix = normalize(np.asarray(temp_position_matrix))
		position_matrix.append(temp_position_matrix)
	position_matrix = np.asarray(position_matrix)
	return position_matrix

#positions = positionize(removeh)
#position_matrix = np.asarray(position_matrix)
#Block3b:Save as pickle
#pkfile = open('position_20200304.pkl')

#Block4a:Initialize
#benchmark = np.load("C:/Users/Ryan/Desktop/mercury/surface/close0050.npy",allow_pickle = True)

def innerp(checkar1,checkar2):
	result = 0
	for i in range(len(checkar1)):
		if math.isnan(checkar1[i])==False and math.isnan(checkar2[i])==False:
			result = result + checkar1[i]*checkar2[i]
	return result

#Block4b:Backtest
def backtest(position_matrix,removehead,valid):
	ini = 100
	assets_rec = [ini]
	return_rec = []
	hishighs = [ini]
	dropdowns = []
	backtestdates = [tdlist[removehead-1]]
	totaloperate = 0
	hishigh = ini

	for d in range(1,len(position_matrix) - valid):
		pricetag_bef = dataset['adjopenn'][d+removehead-1,0:]
		pricetag_aft = dataset['adjopenn'][d+removehead,0:]

		bef_pos = position_matrix[d-1]
		aft_pos = position_matrix[d]
		operate = bef_pos - aft_pos #前減後

		if innerp(pricetag_bef,bef_pos)!= 0:
			dailyreturn = innerp(pricetag_aft,bef_pos)/innerp(pricetag_bef,bef_pos)
		else:
			dailyreturn = 1

		ini = ini*dailyreturn
		assets_rec.append(ini)
		return_rec.append(dailyreturn)
		backtestdates.append(tdlist[d+removehead])

		if assets_rec[d] > hishigh:
			hishigh = assets_rec[d]
		dropdown = (hishigh-assets_rec[d])/hishigh
		dropdowns.append(dropdown)
		hishighs.append(hishigh)

	assets_rec = np.asarray(assets_rec)
	return_rec = np.asarray(return_rec)-1
	backtestdates = np.asarray(backtestdates)
	hishighs = np.asarray(hishighs)
	maxduration = 0
	duration = 0
	maxdd = 0

	for dd in dropdowns:
		if dd > 0:
			duration = duration + 1
		elif dd == 0:
			duration = 0
		if duration > maxduration:
			maxduration = duration
		if dd > maxdd:
			maxdd = dd

	annualgeo = ((assets_rec[len(assets_rec)-1]/assets_rec[0])**(240/len(return_rec))) - 1
	annualstd = np.std(return_rec)*(240**0.5)
	sharpe = annualgeo/annualstd
	backtest_dict = {
		'assets':assets_rec,
		'return':return_rec,
		'dates':backtestdates,
		'annualyield':annualgeo,
		'annualstd':annualstd,
		'sharpe':sharpe,
		'longestdd':maxduration,
		'maximumdd':maxdd,
		'historicalhigh':hishighs}
	return backtest_dict

def validfy(position_matrix,removehead,valid):
	ini = 100
	assets_rec = [ini]
	return_rec = []
	hishighs = [ini]
	dropdowns = []
	backtestdates = [tdlist[removehead-1]]
	totaloperate = 0
	hishigh = ini

	for d in range(len(position_matrix) - valid,len(temp_position_matrix)):
		pricetag_bef = dataset['adjopenn'][d+removehead-1,0:]
		pricetag_aft = dataset['adjopenn'][d+removehead,0:]

		bef_pos = position_matrix[d-1]
		aft_pos = position_matrix[d]
		operate = bef_pos - aft_pos #前減後

		if innerp(pricetag_bef,bef_pos)!= 0:
			dailyreturn = innerp(pricetag_aft,bef_pos)/innerp(pricetag_bef,bef_pos)
		else:
			dailyreturn = 1

		ini = ini*dailyreturn
		assets_rec.append(ini)
		return_rec.append(dailyreturn)
		backtestdates.append(tdlist[d+removehead])

		if assets_rec[d] > hishigh:
			hishigh = assets_rec[d]
		dropdown = (hishigh-assets_rec[d])/hishigh
		dropdowns.append(dropdown)
		hishighs.append(hishigh)

	assets_rec = np.asarray(assets_rec)
	return_rec = np.asarray(return_rec)-1
	backtestdates = np.asarray(backtestdates)
	hishighs = np.asarray(hishighs)
	maxduration = 0
	duration = 0
	maxdd = 0

	for dd in dropdowns:
		if dd > 0:
			duration = duration + 1
		elif dd == 0:
			duration = 0
		if duration > maxduration:
			maxduration = duration
		if dd > maxdd:
			maxdd = dd

	annualgeo = ((assets_rec[len(assets_rec)-1]/assets_rec[0])**(240/len(return_rec))) - 1
	annualstd = np.std(return_rec)*(240**0.5)
	sharpe = annualgeo/annualstd
	backtest_dict = {
		'assets':assets_rec,
		'return':return_rec,
		'dates':backtestdates,
		'annualyield':annualgeo,
		'annualstd':annualstd,
		'sharpe':sharpe,
		'longestdd':maxduration,
		'maximumdd':maxdd,
		'historicalhigh':hishighs}
	return backtest_dict