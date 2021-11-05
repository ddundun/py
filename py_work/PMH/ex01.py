from openpyxl import Workbook

wb= Workbook()
ws= wb.active

ws.title='rrr'
wb.save('a.xlsx')
wb.close() # 파일 닫는것
