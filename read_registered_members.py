import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#dataframe_member = pd.read_excel('Members.xlsx', sheet_name='block_A')


def read_member(members_dataframe,id_tag):
    tag = members_dataframe['RFID_TAG '].tolist()
    #my_tag = input('\n place your card on the reader')
    #my_tag = my_tag.upper()
    my_tag = id_tag
    if my_tag in tag:
        b = 1
        return b, tag, my_tag
    elif my_tag not in tag:
        b = 0
        return b, tag, my_tag


def read_print(members_dataframe, tag, my_tag,pi_print):
    count = 0
    while count < 2:
        prnts = members_dataframe['PRINTS'].tolist()
       # my_print = input('scan your prints on the reader')
       # my_print = my_print.upper()
        my_print = pi_print
        indx = tag.index(my_tag)
        person = members_dataframe.iloc[indx, 4]
        if my_print == person:
            print('hello\n', members_dataframe.iloc[indx, 0], '\n welcome to Konza')
            member = members_dataframe.iloc[indx, 0]
            house_no = members_dataframe.iloc[indx, 2]
            count = count + 2
            alert = 0
            return alert, member, house_no

        else:
            print('not recognized,please try again')
            count = count + 1
            if count == 2:
                print('please consult with the the security desk')
                alert = 1
                member = 0
                house_no = 0
                return alert, member, house_no

# read_print()
