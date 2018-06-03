import xlrd

workbook = xlrd.open_workbook('sample.xlsx')
worksheet=workbook.sheet_by_name('Sheet1')

