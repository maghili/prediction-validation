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

comp = dict()#comparison dictionary
a = 1;
while a in data and a+window-1 in data:
    error = []; string = '%d|%d|'%(a, a+window-1) #Not including the intermediate hours based on format suggestion in FAQ 
    w = 0
    while w < window:
        for stock in data[a+w]:
            if a+w in predict and stock in predict[a+w]: #only the ones that are in the prediction will be counted
                error.append(abs(data[a+w][stock] - predict[a+w][stock]))
        w += 1
    if len(error) == 0:#if there is no match
        comp[a] = string + 'NA'
    else:
        comp[a] = string + '%f'%(round(sum(error)/len(error), 2))
    a += 1


for key in comp:
    f = open('./output/comparison.txt', 'a')
    f.write(comp[key]+'\n')
f.close()

print 'time elapsed: ', t1-t0
