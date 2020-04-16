import numpy as np
import math
import time
#fx: nparray(m*n) -> nparray(m*n)

#1 get an original ndarray
#im_data = klun.func(firms,timeperiod,frequency,dataset)

#2 define operating type
def diff(ndarr,interval):
	t0 = ndarr[0:-interval,:]
	t1 = ndarr[interval:len(ndarr),:]
	title = [[np.nan for i in range(len(ndarr[0]))]for j in range(interval)]
	dif = t1 - t0
	output = np.vstack((title,dif))
	return output

def diff_per(ndarr,interval):
	t0 = ndarr[0:-interval,:]
	t1 = ndarr[interval:len(ndarr),:]
	title = [[np.nan for i in range(len(ndarr[0]))]for j in range(interval)]
	dif = (100*((t1 - t0)/t0))
	output = np.vstack((title,dif))
	return output

def nma(ndarr,periods):
	calp = len(ndarr)-periods+1 #總共幾個做sum
	t0 = ndarr[0:calp,:]
	for i in range(1,periods):
		tn = ndarr[i:calp+i,:]
		t0 = t0+tn
	output = (t0/periods).tolist()
	title = [[np.nan for i in range(len(ndarr[0]))] for j in range(len(ndarr)-len(output))]
	for j in output:
		title.append(j)
	output = np.asarray(title)
	return output

def decay(ndarr,diminishrate):
	output = ndarr[0]
	for i in range(1,len(ndarr)):
		if i == 1:
			a = (1-(1/diminishrate))*output
			b = (1/diminishrate)*ndarr[i]
			query = np.vstack((a,b))
			temp = np.nansum(query,axis = 0)
		#np.asarray( + (1-(1/diminishrate))*output)
		elif i != 1:
			a = (1-(1/diminishrate))*output[-1]
			b = (1/diminishrate)*ndarr[i]
			query = np.vstack((a,b))
			temp = np.nansum(query,axis = 0)
		output = np.vstack((output,temp))
	for j in range(len(output)):
		for k in range(len(output[j])):
			if math.isnan(ndarr[j,k]) == True:
				output[j,k] = np.nan
	return output

def nstd(ndarr,periods):
	calp = len(ndarr)-periods+1 #總共算幾次
	output = []
	for i in range(calp):
		temp = np.nanstd(ndarr[i:i+periods,:],axis = 0)
		output.append(temp)
	output = np.asarray(output)
	title = [[np.nan for i in range(len(ndarr[0]))] for j in range(len(ndarr)-len(output))]
	output = np.vstack((title,output))
	return output

def rsv(ndarr,periods,isc):
	calp = len(ndarr)-periods+1 #總共算幾次
	output = []
	if isc == True:
		ar1 = np.load('surface/high.npy',allow_pickle = True)
		ar2 = np.load('surface/low.npy',allow_pickle = True)
	else:
		ar1 = ndarr
		ar2 = ndarr
	for i in range(calp):
		temp1 = np.max(ar1[i:i+periods,:],axis = 0)
		temp2 = np.min(ar2[i:i+periods,:],axis = 0)
		temp = (ndarr[i+periods-1]-temp2)/(temp1-temp2)
		output.append(temp)
	output = np.asarray(output)
	output = output*100
	title = [[np.nan for i in range(len(ndarr[0]))] for j in range(len(ndarr)-len(output))]
	output = np.vstack((title,output))
	return output

def breaklow(ndarr,periods,isc):
	calp = len(ndarr)-periods+1 #總共算幾次
	output = []
	if isc == True:
		data = np.load('surface/low.npy',allow_pickle = True)
	else:
		data = ndarr 
	for i in range(calp):
		rec = np.min(data[i:i+periods-1,:],axis = 0)
		cur = ndarr[i+periods-1,:]
		com = cur-rec
		temp = np.sign(com)
		temp = [-min(i,0) for i in temp]
		output.append(temp)

	output = np.asarray(output)
	title = [[np.nan for i in range(len(ndarr[0]))] for j in range(len(ndarr)-len(output))]
	output = np.vstack((title,output))
	return output

def breakhigh(ndarr,periods,isc):
	calp = len(ndarr)-periods+1 #總共算幾次
	output = []
	if isc == True:
		data = np.load('surface/high.npy',allow_pickle = True)
	else:
		data = ndarr 
	for i in range(calp):
		rec = np.max(ndarr[i:i+periods-1,:],axis = 0)
		cur = ndarr[i+periods-1,:]
		com = cur-rec
		temp = np.sign(com)
		temp = [max(i,0) for i in temp]
		output.append(temp)		
	output = np.asarray(output)
	title = [[np.nan for i in range(len(ndarr[0]))] for j in range(len(ndarr)-len(output))]
	output = np.vstack((title,output))
	return output

def bigcombo(ndarr,thresh):
	temp = [0 for i in range(len(ndarr[0]))]
	output = []
	for i in range(len(ndarr)):
		for j in range(len(ndarr[i])):
			if ndarr[i,j] > thresh:
				temp[j] = temp[j] + 1
			elif ndarr[i,j] < thresh:
				temp[j] = 0
		output.append([i for i in temp])
	output = np.asarray(output)
	return output

def smallcombo(ndarr,thresh):
	temp = [0 for i in range(len(ndarr[0]))]
	output = []
	for i in range(len(ndarr)):
		for j in range(len(ndarr[i])):
			if ndarr[i,j] < thresh:
				temp[j] = temp[j] + 1
			elif ndarr[i,j] > thresh:
				temp[j] = 0
		output.append([i for i in temp])
	output = np.asarray(output)
	return output

#3 calculating

#4 export