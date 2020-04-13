import datagenerate as dgp
import dg
import numpy as np
import time
import math
import system

'''
@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.s
'''
#%timeit compute_memview.compute(array_1, array_2, a, b, c)

test = np.asarray([[6,2,3],[3,3,4],[3,2,5],[4,4,3],[6,4,5],[7,7,7],[6,3,5]])
test2 = np.asarray([[7,3,4],[5,5,8],[4,5,9],[1,7,8],[7,7,1],[3,4,2],[5,5,5]])

'''
tests = []
for j in range(100000):
	tests.append(test+1)

a = time.time()
for i in range(10000):
	t = (type(dgp.nstd(tests[i],4)))
b = time.time()
print(b-a)

a = time.time()
for i in range(10000):
	t = (type(dg.nstd(tests[i],4)))
b = time.time()
print(b-a)
'''
print(test)
print(test2)


ifs = [['fore','+','it','>',7,2]]
def filter2(d,f,ifs):
	#purify
	#print('sta')
	if math.isnan(test[d,f]) == True: 
		return 0

	def value(ss,sign):
		if sign == '+':
			return test[d-ss,f]+test2[d-ss,f]
		elif sign == '-':
			return test[d-ss,f]-test2[d-ss,f]
		elif sign == '*':
			return test[d-ss,f]*test2[d-ss,f]
		elif sign == '/':
			return test[d-ss,f]/test2[d-ss,f]

	#Those which don't buy
	for if_sit in ifs:
		#print('a')
		for i in range(1,if_sit[5]+1):
			#print(i)
			#secure meaningful compare
			if math.isnan(test[d-1,f]) == True or math.isnan(test2[d-1,f]) == True:
				return 0

			if if_sit[3] == '<':
				if value(i,if_sit[1]) >= if_sit[4] :
					#print('< kick')
					return 0
			elif if_sit[3] == '>':
				#print(i,value(i,if_sit[1]),if_sit[4])
				if value(i,if_sit[1]) <= if_sit[4] :
					#print('> kick')
					return 0
			elif if_sit[3] == '>=':
				if value(if_sit[5],if_sit[1]) < if_sit[4] :
					#print('>= kick')
					return 0
			elif if_sit[3] == '<=':
				if value(if_sit[5],if_sit[1]) > if_sit[4] :
					#print('<= kick')
					return 0
			elif if_sit[3] == '=':
				if value(if_sit[5],if_sit[1]) != if_sit[4] :
					#print('= kick')
					return 0
	#Those which buy
	weight = test[d-1,f] + test2[d-1,f]
	return weight

b = []
for i in range(2,7):
	a = []
	for j in range(3):
		a.append(filter2(i,j,ifs))
		#print('val',filter2(i,j,ifs))
	b.append(a)
b = np.asarray(b)
print(b)
#c = system.fade(b,1)
#print(c)
d = system.rank(b)
print(d)