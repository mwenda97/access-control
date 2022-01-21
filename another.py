import new_try as nt
import pandas as pd
import read_or_write_visitor as rw
import cv2

df = pd.read_excel('Members.xlsx', sheet_name='block_A')
row_list = []
f = df.columns
tag = df['NAME'].tolist()
bn = 'STEVE MWENDA'

#a = rw.existing_members.read_database(tag,bn,312345)
# print(a)
# print('one', a[2])
#www=[]
#for i, x in enumerate(tag):
#    if x == bn:
#        www.append(i)
#print('see',www)

person = df.iloc[7, 0]
print(person)
a=cv2.imread(person)
cv2.imshow('dd',a)
cv2.waitKey(0)
cv2.destroyAllWindows()
