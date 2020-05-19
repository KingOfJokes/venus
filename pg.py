import datagenerate as dgp
import dg
import numpy as np
import time
import math
import system
import os
import pandas as pd
import json
import matplotlib.pyplot as plt

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
def createfolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def pos_operate(npdata,number,sign):
	size_r = len(npdata)
	size_c = len(npdata[0])
	num = np.full((size_r,size_c),number)
	comp = npdata-num
	if sign == '>':
		boo = comp>0
	elif sign == '>=':
		boo = comp>=0
	elif sign == '=':
		boo = comp==0
	elif sign == '<':
		boo = comp<0
	elif sign == '<=':
		boo = comp<=0    
	return boo

def uni(npdata,func,thresh):
    temp = np.roll(npdata,1,axis=0)
    if func == '>':
    	boo = np.where(temp > thresh,npdata,np.nan)
    elif func == '<':
    	boo = np.where(temp < thresh,npdata,np.nan)
    boo = boo/boo
    return boo

def newstock_adj(npdata):
    c2 = np.full_like(npdata,1)
    for k in range(0,6):
        temp = np.roll(npdata,k,axis=0)
        temp = temp/temp
        c2 = c2*temp
    return c2
def sigmoid(ndarr):
	return (1/(1+np.exp(-ndarr)))

def thresh(ori_data,day_start,day_end,func,thr):
	temp_arr = np.full((len(ori_data),len(ori_data[0])),1)
	for i in range(day_start,day_end+1):
		temp = np.roll(ori_data,i,axis = 0)
		temp_boo = pos_operate(temp,thr,func)
		temp_arr = temp_arr*temp_boo
	return temp_arr

def showdata(backtest_inf,title,sample,fd,folder_time):
	output_dict = {}
	output_dict['Annual Return'] = '%.2f'%(100*backtest_inf['annualyield'])+'%'
	output_dict['Annual Std'] = '%.2f'%(100*backtest_inf['annualstd'])+'%'
	output_dict['Sharpe'] = '%.2f'%backtest_inf['sharpe']
	output_dict['Turnover rate'] = '%.2f'%(100*backtest_inf['turnover'])+'%'
	output_dict['Longest DD'] = backtest_inf['longestdd']
	output_dict['Maximum DD'] = '%.2f'%(100*backtest_inf['maximumdd'])+'%'

	print('Annual Return:','%.2f'%(100*backtest_inf['annualyield']),'%')
	print('Annual Std.','%.2f'%(100*backtest_inf['annualstd']),'%')
	print('Sharpe:','%.2f'%backtest_inf['sharpe'])
	print('Turnover rate:','%.2f'%(100*backtest_inf['turnover']),'%')
	print('Longest DD:',backtest_inf['longestdd'])
	print('Maximum DD:','%.2f'%(100*backtest_inf['maximumdd']),'%')

	plt.title('Backtest Summary - '+title+' '+sample)
	plt.plot(backtest_inf['dates'], backtest_inf['assets'], label = 'Strategy')
	#plt.plot(backtest_inf['dates'], backtest_inf['historicalhigh'], label = 'Cap')
	plt.legend(loc='upper left')
	plt.savefig('./backtest/'+fd+'/'+folder_time+'/'+sample)
	plt.show()
	plt.close()
	return output_dict

def oldbt(positions,removeh,valid,fd,ftime):
	result = system.backtest(positions,removeh,valid)
	backtest_inf = result[0]
	valid_inf = result[1]
	distribution = result[2]

	output_json = {}
	output_json['Filter'] = []
	output_json['Result-IS'] = []
	output_json['Result-OS'] = []
	'''
	filter_str = wannaknow
	filter_dict = {'String':filter_str}
	output_json['Filter'].append(filter_dict)
	'''
	print('In-sample')
	json_is = showdata(backtest_inf,'','IS',fd,ftime)
	print('Out-sample')
	json_os = showdata(valid_inf,'','OS',fd,ftime)

	output_json['Result-IS'].append(json_is)
	output_json['Result-OS'].append(json_os)

	with open('./backtest/'+fd+'/'+ftime+'/Readme.json', 'w') as outfile:
		for js in output_json:
			outfile.write(json.dumps(js))
			outfile.write(json.dumps(output_json[js]))
			outfile.write("\n") 

	print('Description of each bet')
	distribution_pd = pd.DataFrame(distribution)
	distribution_np = np.asarray(distribution)
	print(distribution_pd.describe())
	plt.hist(distribution_np,bins=50,range=(-0.2,0.2)) 
	plt.title("Distribution")
	plt.savefig('./backtest/'+fd+'/'+ftime+'/distribution')
	plt.show()
	return [json_is,json_os]

def newbt(positions,removeh,valid,ftime,wannaknow):
	result = system.backtest2(positions,removeh,valid)
	backtest_inf = result[0]
	valid_inf = result[1]
	distribution = result[2]

	output_json = {}
	output_json['Filter'] = []
	output_json['Result-IS'] = []
	output_json['Result-OS'] = []
	filter_str = wannaknow
	filter_dict = {'String':filter_str}
	output_json['Filter'].append(filter_dict)

	print('In-sample')
	json_is = showdata(backtest_inf,'DashBoard','IS',ftime)
	print('Out-sample')
	json_os = showdata(valid_inf,'DashBoard','OS',ftime)

	output_json['Result-IS'].append(json_is)
	output_json['Result-OS'].append(json_os)

	with open('./backtest/'+ftime+'/Readme.json', 'w') as outfile:
		for js in output_json:
			outfile.write(json.dumps(js))
			outfile.write(json.dumps(output_json[js]))
			outfile.write("\n") 

	print('Description of each bet')
	distribution_pd = pd.DataFrame(distribution)
	distribution_np = np.asarray(distribution)
	print(distribution_pd.describe())
	plt.hist(distribution_np,bins=50,range=(-0.2,0.2)) 
	plt.title("Distribution")
	plt.savefig('./backtest/'+ftime+'/distribution')
	plt.show()