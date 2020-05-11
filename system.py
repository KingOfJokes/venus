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

uni = []
def universe(send):
	global uni
	uni = send

def filter(d,f):
	#purify
	print(uni)
	for u in uni:
		pass

	for i in range(0,6): #新股上市前5天容易失真
		if math.isnan((dataset['close'])[d-i,f]) == True: 
			return np.nan

	for i in range(1,2):
		#secure meaningful compare
		if math.isnan((dataset['k9'])[d-1,f]) == True or math.isnan((dataset['d9'])[d-1,f]) == True:
			return 0

		if dataset['k9'][d-i,f] - dataset['d9'][d-i,f] < 0 :
			return 0
	#Those which buy
	weight = 1 #按照要投入的金額比例調整這裡
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
load_needed = ['openn','close','adjopenn','adjclose'] #這邊要把底下filter要呼叫的資料庫打進來
for u in uni:
	load_needed.append(u[0])
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
	for i in range(1,6):
		if math.isnan((dataset['close'])[d-i,f]) == True: 
			return np.nan

	def value(df1,df2,a,sign):
		if sign == '+':
			return dataset[df1][d-a,f]+dataset[df2][d-a,f]
		elif sign == '-':
			return dataset[df1][d-a,f]-dataset[df2][d-a,f]
		elif sign == '*':
			return dataset[df1][d-a,f]*dataset[df2][d-a,f]
		elif sign == '/':
			return dataset[df1][d-a,f]/dataset[df2][d-a,f]

	for u in uni:
		if u[1] == '>':
			if value(u[0],u[0],1,'+') <= 2*u[2]:
				return np.nan
		elif u[1] == '>=':
			if value(u[0],u[0],1,'+') < 2*u[2]:
				return np.nan
		elif u[1] == '=':
			if value(u[0],u[0],1,'+') != 2*u[2]:
				return np.nan
		elif u[1] == '<=':
			if value(u[0],u[0],1,'+') > 2*u[2]:
				return np.nan
		elif u[1] == '<':
			if value(u[0],u[0],1,'+') >= 2*u[2]:
				return np.nan

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
	if wei == 1:
		weight = wei
	else:
		weisplit = wei.split('-')
		figure = weisplit[0]
		mode = weisplit[1]

	if figure == 'price':
		weight = dataset['openn'][d,f]
	elif 'signal' in figure:
		index = int(figure.split('signal')[1])-1
		if_sit2 = ifs[index]
		weight = value(if_sit2[0],if_sit2[2],1,if_sit2[1])

	if mode == '' or mode == 'ori': #default mode為ori
		weight = weight
	elif mode == 'opp':
		weight = -weight
	elif mode == 'inverse':
		if weight != 0:
			weight = 1/weight
	elif mode == 'abs':
		weight = abs(weight)
	return weight

#Block2:import data
tdlist = list(np.load("surface/tdlist.npy",allow_pickle = True))
firmlist = list(np.load("surface/firmlist.npy",allow_pickle = True))
dataset['close0050'] = np.load("surface/close0050.npy",allow_pickle = True)
dataset['openn0050'] = np.load("surface/openn0050.npy",allow_pickle = True)

def dataquery(input_ifs):
	load_needed = ['openn','close','adjopenn','adjclose']
	for if_sit in input_ifs:
		load_needed.append(if_sit[0])
		load_needed.append(if_sit[2])
	for u in uni:
		load_needed.append(u[0])
	load_needed = list(set(load_needed))

	for data_name in load_needed:
		dataset[data_name] = np.load("surface/"+data_name+".npy",allow_pickle = True)

def showinf(field,date,firm):
	if field in dataset:
		print(str(field)+':',dataset[field][date,firm])

#Block3:Create Positions

#temp_position_matrix = np.asarray([0 for x in range(len(firmlist))])
def rankize(posi):
	output = []
	for i in range(len(posi)):
		temp = [0 for i in range(len(posi[i]))]
		ranking = np.argsort(posi[i])
		start = 1
		for ind in range(len(ranking)):
			if posi[i,ranking[ind]] == 0:
				pass
			else:
				temp[ranking[ind]] = start
				start  = start + 1
		output.append(temp)
	output = np.asarray(output)
	return(output)
	
def longize(posit,day): #day should be more than 2
	#給定array, 吐出一個把每個非0元至少自動持續day天，要從後面往前，不然會更新錯
	posi = posit.copy()
	upperbound =len(posi)-1 
	for d in range(upperbound,-1,-1):
		for f in range(len(posi[d])):
			if posi[d,f] != 0 and day >= 2:
				for i in range(d+1,min(upperbound,d+day)):
					if posi[i,f] == 0:
						posi[i,f] = posi[d,f]
	return posi

def neutralize(posit):
	posi = posit.copy()
	adj_matrix = []
	for d in range(len(posi)):
		adj = np.nanmean(posi[d])
		temp = [adj for i in range(len(posi[d]))]
		adj_matrix.append(temp)
	adj_matrix = np.asarray(adj_matrix)
	posi = posi - adj_matrix
	return posi

def normalize(posit):
	#validnumber = 0
	posi = posit.copy()
	posisum = np.nansum(abs(posi),axis = 1)
	posisum = np.tile(posisum,(len(posi[0]),1)).T
	posi = posi/posisum
	return posi

def shareize(posit):
	output = []
	posi = posit.copy()
	pricetag = dataset['openn']
	for pd in range(len(posi)):
		temp = [posi[pd,f]/pricetag[pd,f] for f in range(len(posi[pd]))]
		output.append(temp)
	output = np.asarray(output)
	return output

def positionize():
	position_matrix = []
	for d in range(1,len(tdlist)):
		temp_position_matrix = []
		for f in range(len(firmlist)):
			temp_position_matrix.append(filter(d,f))
		temp_position_matrix = normalize(np.asarray(temp_position_matrix))
		position_matrix.append(temp_position_matrix)
	position_matrix = np.asarray(position_matrix)
	return position_matrix

def positionize2(input_ifs,wei):
	position_matrix = []
	for d in range(1,len(tdlist)):
		temp_position_matrix = []
		for f in range(len(firmlist)):
			temp_position_matrix.append(filter2(d,f,input_ifs,wei))
		position_matrix.append(temp_position_matrix)
	position_matrix = np.asarray(position_matrix)
	return position_matrix

#positions = positionize(removeh)
#position_matrix = np.asarray(position_matrix)
#Block3b:Save as pickle
#pkfile = open('position_20200304.pkl')

#Block4a:Initialize
#benchmark = np.load("C:/Users/Ryan/Desktop/mercury/surface/close0050.npy",allow_pickle = True)

'''
def innerp(checkar1,checkar2):
	result = 0
	for i in range(len(checkar1)):
		if math.isnan(checkar1[i])==False and math.isnan(checkar2[i])==False:
			result = result + checkar1[i]*checkar2[i]
	return result
'''
#Block4b:Backtest
def backtest(position_matrix,removehead,valid):
	ini = 100
	assets_rec = [ini]
	return_rec = []
	hishighs = [ini]
	dropdowns = []
	turnovers = []
	backtestdates = [tdlist[0]]
	totaloperate = 0
	hishigh = ini
	eachperf = []

	for d in range(removehead+1,len(tdlist)):
		#pricetag_bef = dataset['adjopenn'][d+removehead-1,0:]
		#pricetag_aft = dataset['adjopenn'][d+removehead,0:]
		pricetag_bef = dataset['adjopenn'][d-1,0:]
		pricetag_aft = dataset['adjopenn'][d,0:]

		bef_pos = position_matrix[d-1]
		aft_pos = position_matrix[d-0]
		operate = aft_pos - bef_pos #前減後

		for f in range(len(bef_pos)):
			if math.isnan(pricetag_bef[f]) == False:
				eff = np.sign(bef_pos[f])*((pricetag_aft[f]-pricetag_bef[f])/pricetag_bef[f])
			else:
				eff = np.nan
			if eff > -0.4 and eff < 0.4:
				eachperf.append(eff)
			elif math.isnan(eff) == False:
				print('error',eff,'d',tdlist[d],'f',firmlist[f],pricetag_aft[f],pricetag_bef[f])
				bef_pos[f] = 0

		if np.nansum(pricetag_bef*bef_pos)!= 0:
			dailyreturn = 1+((np.nansum(pricetag_aft*bef_pos)-np.nansum(pricetag_bef*bef_pos))/np.nansum(pricetag_bef*abs(bef_pos)))
		else:
			dailyreturn = 1
		
		turnover = np.nansum(pricetag_aft*abs(operate))
		scale = np.nansum(pricetag_bef*abs(bef_pos))
		if scale != 0:
			turnover_ratio = turnover/scale
		else:
			turnover_ratio = 0
		turnovers.append(turnover_ratio)
		
		ini = ini*dailyreturn
		assets_rec.append(ini)
		return_rec.append(dailyreturn)
		backtestdates.append(tdlist[d])

		if assets_rec[d-removehead-1] > hishigh:
			hishigh = assets_rec[d-removehead-1]
		dropdown = (hishigh-assets_rec[d-removehead-1])/hishigh
		dropdowns.append(dropdown)
		hishighs.append(hishigh)

	assets_rec = np.asarray(assets_rec)
	return_rec = np.asarray(return_rec)-1
	backtestdates = np.asarray(backtestdates)
	hishighs = np.asarray(hishighs)
	turnovers = np.asarray(turnovers)
	maxduration = 0
	duration = 0
	maxdd = 0

	for dd in dropdowns[0:len(assets_rec)-valid]:
		if dd > 0:
			duration = duration + 1
		elif dd == 0:
			duration = 0
		if duration > maxduration:
			maxduration = duration
		if dd > maxdd:
			maxdd = dd

	assets_rec_in = assets_rec[0:len(assets_rec)-valid]
	assets_rec_out = assets_rec[len(assets_rec)-valid:len(assets_rec)]
	assets_rec_out = assets_rec_out/assets_rec_out[0]
	return_rec_in = return_rec[0:len(return_rec)-valid]
	return_rec_out = return_rec[len(return_rec)-valid:len(return_rec)]
	backtestdates_in = backtestdates[0:len(backtestdates)-valid]
	backtestdates_out = backtestdates[len(backtestdates)-valid:len(backtestdates)]
	turnovers_in = turnovers[0:len(turnovers)-valid]
	turnovers_out = turnovers[len(turnovers)-valid:len(turnovers)]

	annualgeo_in = ((assets_rec_in[len(assets_rec_in)-1]/assets_rec_in[0])**(240/len(return_rec_in))) - 1
	annualstd_in = np.std(return_rec_in)*(240**0.5)
	sharpe_in = annualgeo_in/annualstd_in

	annualgeo_out = ((assets_rec_out[len(assets_rec_out)-1]/assets_rec_out[0])**(240/len(return_rec_out))) - 1
	annualstd_out = np.std(return_rec_out)*(240**0.5)
	sharpe_out = annualgeo_out/annualstd_out

	backtest_dict = {
		'assets':assets_rec_in,
		'return':return_rec_in,
		'dates':backtestdates_in,
		'annualyield':annualgeo_in,
		'annualstd':annualstd_in,
		'sharpe':sharpe_in,
		'longestdd':maxduration,
		'maximumdd':maxdd,
		'turnover':np.nanmean(turnovers_in)
		#'historicalhigh':hishighs
		}
	validfy_dict = {
		'assets':assets_rec_out,
		'return':return_rec_out,
		'dates':backtestdates_out,
		'annualyield':annualgeo_out,
		'annualstd':annualstd_out,
		'sharpe':sharpe_out,
		'longestdd':0,
		'maximumdd':0,
		'turnover':np.nanmean(turnovers_out)
		#'historicalhigh':hishighs
		}

	return [backtest_dict,validfy_dict,eachperf]

def backtest2(position,removehead,valid):
	ini = 100
	assets_rec = [ini]
	return_rec = []
	hishighs = [ini]
	dropdowns = []
	turnovers = []
	backtestdates = [tdlist[0]]
	totaloperate = 0
	hishigh = ini
	eachperf = []

	pricetag = dataset['adjopenn']
	pricetag_yest = np.roll(pricetag,1,axis = 0) 
	position_yest = np.roll(position,1,axis = 0)
	operate = position - position_yest
	scale = np.nansum(pricetag_yest*np.abs(position_yest),axis = 1)
	turn = np.nansum(pricetag*np.abs(operate),axis = 1)
	turnover = turn/scale
	cost = position_yest*pricetag_yest
	result = position_yest*pricetag
	dailyreturn = np.nansum(result,axis = 1)/np.nansum(cost,axis = 1)
	eachbet = (result-cost)/cost

	for d in range(removehead+1,len(position)):
		if np.isinf(turnover[d]) == False and np.isnan(turnover[d]) == False:
			turnovers.append(turnover[d])
		else:
			turnovers.append(0)

		ini = ini*dailyreturn[d]
		assets_rec.append(ini)
		return_rec.append(dailyreturn[d])
		backtestdates.append(tdlist[d])

		if assets_rec[d-removehead-1] > hishigh:
			hishigh = assets_rec[d-removehead-1]
		dropdown = (hishigh-assets_rec[d-removehead-1])/hishigh
		dropdowns.append(dropdown)
		hishighs.append(hishigh)

	for d in range(1,len(eachbet)):
		for f in range(len(eachbet[d])):
			bet = eachbet[d,f]
			if np.isnan(bet) == False:
				eachperf.append(bet)
			if np.abs(bet)>0.4:
				print('error',bet,'d',tdlist[d],'f',firmlist[f],pricetag[d,f],pricetag_yest[d,f])

	assets_rec = np.asarray(assets_rec)
	return_rec = np.asarray(return_rec)-1
	backtestdates = np.asarray(backtestdates)
	hishighs = np.asarray(hishighs)
	turnovers = np.asarray(turnovers)
	maxduration = 0
	duration = 0
	maxdd = 0

	for dd in dropdowns[0:len(assets_rec)-valid]:
		if dd > 0:
			duration = duration + 1
		elif dd == 0:
			duration = 0
		if duration > maxduration:
			maxduration = duration
		if dd > maxdd:
			maxdd = dd

	assets_rec_in = assets_rec[0:len(assets_rec)-valid]
	assets_rec_out = assets_rec[len(assets_rec)-valid:len(assets_rec)]
	assets_rec_out = assets_rec_out/assets_rec_out[0]
	return_rec_in = return_rec[0:len(return_rec)-valid]
	return_rec_out = return_rec[len(return_rec)-valid:len(return_rec)]
	backtestdates_in = backtestdates[0:len(backtestdates)-valid]
	backtestdates_out = backtestdates[len(backtestdates)-valid:len(backtestdates)]
	turnovers_in = turnovers[0:len(turnovers)-valid]
	turnovers_out = turnovers[len(turnovers)-valid:len(turnovers)]

	annualgeo_in = ((assets_rec_in[len(assets_rec_in)-1]/assets_rec_in[0])**(240/len(return_rec_in))) - 1
	annualstd_in = np.std(return_rec_in)*(240**0.5)
	sharpe_in = annualgeo_in/annualstd_in

	annualgeo_out = ((assets_rec_out[len(assets_rec_out)-1]/assets_rec_out[0])**(240/len(return_rec_out))) - 1
	annualstd_out = np.std(return_rec_out)*(240**0.5)
	sharpe_out = annualgeo_out/annualstd_out

	backtest_dict = {
		'assets':assets_rec_in,
		'return':return_rec_in,
		'dates':backtestdates_in,
		'annualyield':annualgeo_in,
		'annualstd':annualstd_in,
		'sharpe':sharpe_in,
		'longestdd':maxduration,
		'maximumdd':maxdd,
		'turnover':np.nanmean(turnovers_in)
		#'historicalhigh':hishighs
		}
	validfy_dict = {
		'assets':assets_rec_out,
		'return':return_rec_out,
		'dates':backtestdates_out,
		'annualyield':annualgeo_out,
		'annualstd':annualstd_out,
		'sharpe':sharpe_out,
		'longestdd':0,
		'maximumdd':0,
		'turnover':np.nanmean(turnovers_out)
		#'historicalhigh':hishighs
		}

	return [backtest_dict,validfy_dict,eachperf]