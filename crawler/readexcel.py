import  xlrd

excelList = xlrd.open_workbook("/Users/wsjswy/Downloads/111.xlsx")

print excelList.nsheets


sh = excelList.sheet_by_index(0)

print sh.nrows

cell = sh.cell_value(100, 0)

print  cell
