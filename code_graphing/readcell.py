import openpyxl

def read_cell_line(line, cellname, start, end):
    wb = openpyxl.load_workbook(cellname)
    ws = wb.active

    mylist = []
    for gen in range(start, end+1):
        mylist.append(ws.cell(row=gen, column=line).value)

    return mylist