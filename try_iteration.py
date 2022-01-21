import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('Members.xlsx', sheet_name='block_A')
row_list = []
f = df.columns
tag = df['NAME'].tolist()
bn = 'STEVE MWENDA'


# print(tag)


def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


a = duplicates(tag, bn)
print(a)
print('one', a[2])
# person = df.iloc[1, 0]
# print(person)
x = len(a)
print('number', x)
count = 0
we = []

for i in range(x):
    work=a[count]
    print('shjf',work)
    person = df.iloc[work, 0]
    k = we.append(person)
    count = count + 1
    print('motherfucker you gotta work', person)
print('we', we)
if 'JOJO' in we:
    print('hello JOJO')
