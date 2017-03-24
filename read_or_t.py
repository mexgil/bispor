from math import pi,cos,sin,radians
from collections import OrderedDict
import sys


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)



path = r'data\origint\ora.txt'

with open(path,'r') as f:
    data = f.read().split('\n')

nums = slice(17,24)
g_ang = slice(39,48)
v_ang = slice(63,72)
dist = slice(89,96)




stats = []
n=0
for i in data:
    num =i[nums]
    if len(i)<130:
        stats.append(n)
    n+=1

n=0
for i in stats:
    n+=1
    coords = OrderedDict() 
    try:        
        for i in data[i:stats[stats.index(i)+1]]:
            num = i[nums]
            if len(i)<130:
                pn = num
            if len(i)>130:
                try:
                    va = float('{}.{}'.format(i[v_ang][:-5],i[v_ang][-5:]))*0.9
                except:
                    next
                try:
                    ga = float('{}.{}'.format(i[g_ang][:-5],i[g_ang][-5:]))*0.9
                except:
                    next
                
                if va>180:
                    va = 360 - va - 90
                    vang = ((va)*pi)/180
                    ga -=180
                    if ga<0:
                        ga+=360
                    
                elif va<180:
                    va -= 90
                    if ga>359:
                        ga -= 360
                    vang = (va*pi)/180

                gang = radians(ga)
                di = float('{}.{}'.format(i[dist][:-4],i[dist][-4:]))
                d = di*cos(vang)
                try:
                    coords[num][0].append(gang)
                    coords[num][1].append(d)
                except KeyError:
                    coords[num] = [[],[]]
                    coords[num][0].append(gang)
                    coords[num][1].append(d)
    except IndexError:               
        for i in data[i:]:
            print(num)
            num = i[nums]
            if len(i)<130:
                pn = num
            if len(i)>130:
                print(num)
                try:
                    va = float('{}.{}'.format(i[v_ang][:-5],i[v_ang][-5:]))*0.9
                except:
                    next
                try:
                    ga = float('{}.{}'.format(i[g_ang][:-5],i[g_ang][-5:]))*0.9
                except:
                    next
                
                if va>180:
                    va = 360 - va - 90
                    vang = ((va)*pi)/180
                    ga -=180
                    if ga<0:
                        ga+=360
                    
                elif va<180:
                    va -= 90
                    vang = (va*pi)/180
                gang = radians(ga)
                di = float('{}.{}'.format(i[dist][:-4],i[dist][-4:]))
                d = di*cos(vang)
                try:
                    coords[num][0].append(gang)
                    coords[num][1].append(d)
                except KeyError:
                    coords[num] = [[],[]]
                    coords[num][0].append(gang)
                    coords[num][1].append(d)


    #for k in coords.keys():
    #    print('{} --> {}'.format(k, coords[k]))
    minr = radians(1)
    maxr = radians(359)
    rad360 = radians(360)


    #rename targets with distance less than 20 meters from observation point

    
    sm_ind=0
    for k in coords.keys():
        if len(k.lstrip('0'))<4 and mean(coords[k][1])<20:
            coords[k+'_smpl_{}'.format(sm_ind)]=coords[k]
            del coords[k]
            sm_ind+=1


    for k in coords.keys():
        if any(i<minr for i in coords[k][0]) and any(i>maxr for i in coords[k][0]):
            for i in coords[k][0]:
                if i>maxr:
                    coords[k][0][coords[k][0].index(i)] = i-rad360
        g = mean(coords[k][0])
        d = mean(coords[k][1])    
        x = d*cos(g)
        y = d*sin(g)
        coords[k] = (x,y)


        
    with open(r'data\origint\ex\{}_{}.csv'.format(str(n).zfill(7),pn),'w') as f:
        for k in coords.keys():
            f.writelines('{};{};{}\n'.format(str(k.lstrip('0')),str(coords[k][0]),str(coords[k][1])))

            
