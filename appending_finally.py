import pandas as pd
from openpyxl import load_workbook

reader = pd.read_excel(r'Members.xlsx')
df = pd.DataFrame({'NAME': ['jEh','hFk','hGl','Hjgt'],
                   'ID_NO': [100,70,40,60],
                   'HOUSE_NO':[1,2,3,4],
                   'RFID_TAG ': [1,2,3,4] ,
                   'PRINTS':[4,5,6,7]})
book = load_workbook('Members.xlsx')
writer = pd.ExcelWriter('Members.xlsx', engine='openpyxl')
writer.book=book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
df.to_excel(writer,header=False,startrow=len(reader)+1,sheet_name='block_A',index=False)
writer.save()

print(reader)