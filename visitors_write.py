import pandas as pd

df = pd.DataFrame( {'HOST_NAME': [],
                    'VISISTOR_NAME':[],
                    'ID_NO': [],
                    'HOUSE_NO':[],
                      'TEL_NO ':[],
                    'PRINTS':[],
                    'PHOTO':[]})

writer = pd.ExcelWriter('visitors.xlsx',engine='xlsxwriter')
df.to_excel(writer, sheet_name='block_A',index=False)
writer.save()
print(df)