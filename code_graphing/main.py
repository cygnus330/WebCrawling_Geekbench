import matplotlib.pyplot as plt
import importlib
import numpy as np

from readcell import read_cell_line

#importlib.reload(plt)

draw_what = 1

year_RAW = read_cell_line(2, 'releasedate.xlsx', 2, 13)
month_RAW = read_cell_line(3, 'releasedate.xlsx', 2, 13)
STscore_RAW = []
MTscore_RAW = []
date_RAW = []
for i in range(12):
    date_RAW.append(year_RAW[i] + month_RAW[i]/12)
for i in range (3,7):
    STscore_RAW.append([])
    MTscore_RAW.append([])
    STscore_RAW[i - 3] = read_cell_line(i, 'STScore.xlsx', 3, 14)
    MTscore_RAW[i - 3] = read_cell_line(i, 'MTScore.xlsx', 3, 14)

STscore = []
MTscore = []
for i in range(4):
    STscore.append([[], [], []])
    MTscore.append([[], [], []])

for j in range(4):
    mylist = []
    mylist2 = []
    mylist3 = []
    for i in range(12):
        if(STscore_RAW[j][i] != 0):
            mylist.append(STscore_RAW[j][i])
            mylist2.append(date_RAW[i])
            mylist3.append(i+1)
    STscore[j][0] = mylist
    STscore[j][1] = mylist2
    STscore[j][2] = mylist3
for j in range(4):
    mylist = []
    mylist2 = []
    mylist3 = []
    for i in range(12):
        if(STscore_RAW[j][i] != 0):
            mylist.append(MTscore_RAW[j][i])
            mylist2.append(date_RAW[i])
            mylist3.append(i + 1)
    MTscore[j][0] = mylist
    MTscore[j][1] = mylist2
    MTscore[j][2] = mylist3

'''
print(STscore)
print(MTscore)

for i in range(4):
    listtoxlsx(STscore[i], f'output\STscorei{9-2*i}.xlsx')
    listtoxlsx(MTscore[i], f'output\MTscorei{9-2*i}.xlsx')
'''



#date, line
plt.clf()
plt.plot(MTscore[0][1], MTscore[0][0], 'o-', label='i9', color='red')
plt.plot(MTscore[1][1], MTscore[1][0], 'o-', label='i7', color='orange')
plt.plot(MTscore[2][1], MTscore[2][0], 'o-', label='i5', color='limegreen')
plt.plot(MTscore[3][1], MTscore[3][0], 'o-', label='i3', color='blue')

plt.title('MT Performance (date, line)')
plt.xlabel('Year', loc = 'right')
plt.ylabel('Perf.', loc = 'top')
plt.xlim(2007, 2023)
plt.ylim(0, 22000)
plt.xscale('linear')
plt.yscale('linear')

plt.legend(ncol=1, frameon=True, shadow=True)
plt.xticks(np.arange(2008, 2024, 2))
plt.yticks(np.arange(0, 22000, 2000))
#plt.show()
plt.savefig('output\MT Performance (date, line)')


plt.clf()
plt.plot(STscore[0][1], STscore[0][0], 'o-', label='i9', color='red')
plt.plot(STscore[1][1], STscore[1][0], 'o-', label='i7', color='orange')
plt.plot(STscore[2][1], STscore[2][0], 'o-', label='i5', color='limegreen')
plt.plot(STscore[3][1], STscore[3][0], 'o-', label='i3', color='blue')

plt.title('ST Performance (date, line)')
plt.xlabel('Year', loc = 'right')
plt.ylabel('Perf.', loc = 'top')
plt.xlim(2007, 2023)
plt.ylim(0, 2400)
plt.xscale('linear')
plt.yscale('linear')

plt.legend(ncol=1, frameon=True, shadow=True)
plt.xticks(np.arange(2008, 2024, 2))
plt.yticks(np.arange(0, 2400, 200))
#plt.show()
plt.savefig('output\ST Performance (date, line)')


#date, log
plt.clf()
plt.plot(MTscore[0][1], MTscore[0][0], 'o-', label='i9', color='red')
plt.plot(MTscore[1][1], MTscore[1][0], 'o-', label='i7', color='orange')
plt.plot(MTscore[2][1], MTscore[2][0], 'o-', label='i5', color='limegreen')
plt.plot(MTscore[3][1], MTscore[3][0], 'o-', label='i3', color='blue')

plt.title('MT Performance (date, log)')
plt.xlabel('Year', loc='right')
plt.ylabel('Perf.', loc='top')
plt.xlim(2007, 2023)
#plt.ylim(0, 22000)
plt.xscale('linear')
plt.yscale('log')

plt.legend(ncol=1, frameon=True, shadow=True)
plt.xticks(np.arange(2008, 2024, 2))
#plt.yticks(np.arange(0, 22000, 2000))
#plt.show()
plt.savefig('output\MT Performance (date, log)')

plt.clf()
plt.plot(STscore[0][1], STscore[0][0], 'o-', label='i9', color='red')
plt.plot(STscore[1][1], STscore[1][0], 'o-', label='i7', color='orange')
plt.plot(STscore[2][1], STscore[2][0], 'o-', label='i5', color='limegreen')
plt.plot(STscore[3][1], STscore[3][0], 'o-', label='i3', color='blue')

plt.title('ST Performance (date, log)')
plt.xlabel('Year', loc='right')
plt.ylabel('Perf.', loc='top')
plt.xlim(2007, 2023)
#plt.ylim(0, 2400)
plt.xscale('linear')
plt.yscale('log')

plt.legend(ncol=1, frameon=True, shadow=True)
plt.xticks(np.arange(2008, 2024, 2))
#plt.yticks(np.arange(0, 2400, 200))
#plt.show()
plt.savefig('output\ST Performance (date, log)')


#gen, line
plt.clf()
plt.plot(STscore[0][2], STscore[0][0], 'o-', label='i9', color='red')
plt.plot(STscore[1][2], STscore[1][0], 'o-', label='i7', color='orange')
plt.plot(STscore[2][2], STscore[2][0], 'o-', label='i5', color='limegreen')
plt.plot(STscore[3][2], STscore[3][0], 'o-', label='i3', color='blue')

plt.title('ST Performance (gen, line)')
plt.xlabel('Year', loc = 'right')
plt.ylabel('Perf.', loc = 'top')
plt.xlim(0, 13)
plt.ylim(0, 2400)
plt.xscale('linear')
plt.yscale('linear')

plt.legend(ncol=1, frameon=True, shadow=True)
plt.xticks(np.arange(1, 13, 1))
plt.yticks(np.arange(0, 2400, 200))
#plt.show()
plt.savefig('output\ST Performance (gen, line)')

plt.clf()
plt.plot(MTscore[0][2], MTscore[0][0], 'o-', label='i9', color='red')
plt.plot(MTscore[1][2], MTscore[1][0], 'o-', label='i7', color='orange')
plt.plot(MTscore[2][2], MTscore[2][0], 'o-', label='i5', color='limegreen')
plt.plot(MTscore[3][2], MTscore[3][0], 'o-', label='i3', color='blue')

plt.title('MT Performance (gen, line)')
plt.xlabel('Year', loc = 'right')
plt.ylabel('Perf.', loc = 'top')
plt.xlim(0, 13)
plt.ylim(0, 22000)
plt.xscale('linear')
plt.yscale('linear')

plt.legend(ncol=1, frameon=True, shadow=True)
plt.xticks(np.arange(1, 13, 1))
plt.yticks(np.arange(0, 22000, 2000))
#plt.show()
plt.savefig('output\MT Performance (gen, line)')


#gen, log
plt.clf()
plt.plot(STscore[0][2], STscore[0][0], 'o-', label='i9', color='red')
plt.plot(STscore[1][2], STscore[1][0], 'o-', label='i7', color='orange')
plt.plot(STscore[2][2], STscore[2][0], 'o-', label='i5', color='limegreen')
plt.plot(STscore[3][2], STscore[3][0], 'o-', label='i3', color='blue')

plt.title('ST Performance (gen, log)')
plt.xlabel('Year', loc = 'right')
plt.ylabel('Perf.', loc = 'top')
plt.xlim(0, 13)
#plt.ylim(0, 2400)
plt.xscale('linear')
plt.yscale('log')

plt.legend(ncol=1, frameon=True, shadow=True)
plt.xticks(np.arange(1, 13, 1))
#plt.yticks(np.arange(0, 2400, 200))
#plt.show()
plt.savefig('output\ST Performance (gen, log)')


plt.clf()
plt.plot(MTscore[0][2], MTscore[0][0], 'o-', label='i9', color='red')
plt.plot(MTscore[1][2], MTscore[1][0], 'o-', label='i7', color='orange')
plt.plot(MTscore[2][2], MTscore[2][0], 'o-', label='i5', color='limegreen')
plt.plot(MTscore[3][2], MTscore[3][0], 'o-', label='i3', color='blue')

plt.title('MT Performance (gen, log)')
plt.xlabel('Year', loc = 'right')
plt.ylabel('Perf.', loc = 'top')
plt.xlim(0, 13)
#plt.ylim(0, 2400)
plt.xscale('linear')
plt.yscale('log')

plt.legend(ncol=1, frameon=True, shadow=True)
plt.xticks(np.arange(1, 13, 1))
#plt.yticks(np.arange(0, 2400, 200))
#plt.show()
plt.savefig('output\MT Performance (gen, log)')