import pandas as pd
import openpyxl

def listtoxlsx(list, cellname):
    df = pd.DataFrame.from_records(list)
    df.to_excel(cellname)
