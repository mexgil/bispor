from math import pi,cos,sin,radians
from collections import OrderedDict
import sys


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)



path = r'data\origin\ora.txt'

with open(path,'r') as f:
    data = f.read().split('\n')

nums = slice(18,24)
g_ang = slice(40,48)
v_ang = slice(64,72)
dist = slice(90,96)




stats = []
n=0
for i in data:
    num =i[nums]
    if len(num.lstrip('0'))==6:
        stats.append(n)
    n+=1

n=0
for i in stats:
    n+=1
    coords = OrderedDict() 
    try:        
        for i in data[i:stats[stats.index(i)+1]]:
            num = i[nums]
            if len(num.lstrip('0'))==6:
                pn = num
            if len(num.lstrip('0'))<6:
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
    except IndexError:               
        for i in data[i:]:
            num = i[nums]
            if len(num.lstrip('0'))==6:
                pn = num
            if len(num.lstrip('0'))<6:
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
                    
         
    for k in coords.keys():
        g = mean(coords[k][0])
        d = mean(coords[k][1])    
        x = d*cos(g)
        y = d*sin(g)
        coords[k] = (x,y)

        
    with open(r'data\origin\ex\{}.csv'.format(str(n).zfill(7)),'w') as f:
        for k in coords.keys():
            f.writelines('{};{};{}\n'.format(str(k.lstrip('0')),str(coords[k][0]),str(coords[k][1])))

            
