import matplotlib.pyplot as plt
import matplotlib.markers as plm
import numpy as np
import json

x = []
y1 = []
y2 = []
y3 = []

y1_std = []
y2_std = []
y3_std = []


fname="../results/data.csv"
f = open(fname, 'r')
num_cols = len(f.readline().split(':'))
f.seek(0)
lines = f.read().splitlines()
f.close()

for line in lines:
	data = line.split(':')
	print(data[0])
	x.append(float(data[0].replace(',', '.')))
	y1.append(28-float(data[1].replace(',', '.')))
	y2.append(28-float(data[2].replace(',', '.')))
	y3.append(28-float(data[3].replace(',', '.'))) 
	y1_std.append(0)
	y2_std.append(0)
	y3_std.append(0)
								
fig = plt.figure(2)

yMax = max(y2) + max(y2)*0.02
yMim = max(y2)*-0.02
plt.ylim(yMim, yMax)

xMax = len(x) + len(x)*0.02
xMim =  len(x)*-0.02
plt.xlim(xMim, xMax)
#plt.xticks(x, rotation = "horizontal")

plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)    												

plt.errorbar(x,y1, ls="solid", label='Best', color='g', yerr=y1_std, zorder=3)			
plt.errorbar(x,y2, ls="solid", label='Worst', color='r', yerr=y2_std, zorder=3)						
plt.errorbar(x,y3, ls="solid", label='Average', color='b', yerr=y3_std, zorder=3)			

		

nameFile = 'queens'
ylabel = 'Pairs of non-attacking queens'
xlabel = 'Number of generations'
title = "8-Queens Problem"

plt.ylabel(ylabel, fontweight="bold")
plt.xlabel(xlabel, fontweight="bold") 	
#plt.title(title, fontweight="bold")

plt.legend(numpoints=1, loc="upper left", ncol=3, bbox_to_anchor=(-0.02, 1.15))


fig.savefig('../plots/queens/'+nameFile+'.png', bbox_inches='tight')
plt.close(fig) 			

