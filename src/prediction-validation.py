import numpy as np
import time
#####
#reading the data
data = dict()#actual data
with open('./input/actual.txt') as datafile:
    for line in datafile:
        lst = line.rstrip('\n').split('|')
        if int(lst[0]) in data:
            data[int(lst[0])][lst[1]] = float(lst[-1])# putting the data in nested dictioneries
        else:
            data[int(lst[0])] = {}
            data[int(lst[0])][lst[1]] = float(lst[-1])

datafile.close()

predict = dict()#predicted data
with open('./input/predicted.txt') as prediction:
    for line in prediction:
        lst = line.rstrip('\n').split('|')
        if int(lst[0]) in predict:
            predict[int(lst[0])][lst[1]] = float(lst[-1])
        else:
            predict[int(lst[0])] = {}
            predict[int(lst[0])][lst[1]] = float(lst[-1])
with open('./input/window.txt') as w:
     for line in w:
         window = int(line.rstrip('\n'))
w.close()

t0 = time.time()#to start timing the calculations
comp = dict()#comparison dictionary
a = 1;
while a in data and a+window-1 in data:
    error = []; string = ''; w = 0
    while w < window:
        string += '%d|'%(a+w)
        for stock in data[a+w]:
            if stock in predict[a+w]:
                error.append(abs(data[a+w][stock] - predict[a+w][stock]))
        w += 1
    if len(error) > 0:
        comp[a] = string + '%1.2f'%np.average(error)
    a += 1


for key in comp:
    f = open('./output/comparison.txt', 'a')
    f.write('\n'+comp[key])
f.close()

t1 = time.time()
print 'time elapsed: ', t1-t0
