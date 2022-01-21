import pandas as pd


writer = pd.ExcelWriter('Visitors.xlsx',engine='xlsxwriter')
writer_m = pd.ExcelWriter('Members.xlsx',engine='xlsxwriter')
#writer = pd.ExcelWriter('Members.xlsx',engine='xlsxwriter')
writer.save()
writer_m.save()