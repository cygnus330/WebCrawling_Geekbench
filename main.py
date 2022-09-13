from readcell import readCPUlist
from crawling import crawlpage
#import openpyxl
#from crawling import

CPU_RAWlist = readCPUlist()
CPU_list = []
Score_list = []
for gen in range(2, 14):
    mylist = []
    mylist.append(CPU_RAWlist.cell(row=gen, column=1).value)
    mylist.append(CPU_RAWlist.cell(row=gen, column=3).value)
    mylist.append(CPU_RAWlist.cell(row=gen, column=4).value)
    mylist.append(CPU_RAWlist.cell(row=gen, column=5).value)
    mylist.append(CPU_RAWlist.cell(row=gen, column=6).value)
    CPU_list.append(mylist)

print(crawlpage('Core i3-12100', 1))