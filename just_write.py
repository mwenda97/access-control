import pandas as pd

df = pd.DataFrame({'NAME': [],
                   'ID_NO': [],
                   'HOUSE_NO': [],
                   'RFID_TAG ': [],
                   'TEL_NO': [],
                   'PRINTS': [],
                   'PHOTO': []})

writer = pd.ExcelWriter('Members.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='block_A', index=False)
writer.save()
print(df)
