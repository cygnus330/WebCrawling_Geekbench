import pandas as pd

def listtoxlsx(list, cellname):
    df = pd.DataFrame.from_records(list)
    df.to_excel(cellname)
