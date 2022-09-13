from openpyxl import load_workbook

'''
import pandas as pd

def readexcel():
    cellread = pd.read_excel("CPUlist.xlsx")
    return cellread
'''
def readCPUlist():
    wb = load_workbook("CPUlist.xlsx") #CPUlist.xlsx 파일에서 wb를 불러옴
    ws = wb.active #활성화된 시트
    return ws



