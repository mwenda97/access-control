import pandas as pd
from openpyxl import load_workbook
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import take_save_pic as tsp
import read_registered_members as rdm


# reads = rdm.read_member()
# host_name, house_no = reads


def new_visitor(host_name, house_no, members_dataframe):
    print('follow the guide lines to register yourself visitor')
    name = input('\n Enter your Names:')
    names = name
    name = name.upper()
    id_no = int(input('\nEnter your ID_no'))
    prints = input('enter finger print id')
    prints = prints.upper()
    tel_no = int(input('enter your phone number'))
    reader = pd.read_excel(r'Visitors.xlsx')
    tsp.take_photo(names)
    members_dataframe = pd.DataFrame({'HOST_NAME': [host_name],
                                      'NAME': [name],
                                      'ID_NO': [id_no],
                                      'HOUSE_NO': [house_no],
                                      'TEL_NO': [tel_no],
                                      'PRINTS': [prints],
                                      'PHOTO':['captured_photo/' + names + '.jpg']})
    book = load_workbook('Visitors.xlsx')
    writer = pd.ExcelWriter('Visitors.xlsx', engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    members_dataframe.to_excel(writer, header=False, startrow=len(reader) + 1, sheet_name='block_A', index=False)
    writer.save()


# new_visitor()
class existing_members:
    def read_database(self, host_name, visiting_prints, visitor_dataframe):
        # print('this is just another check')
        host_name_list = []
        for i, x in enumerate(self):
            if x == host_name:
                host_name_list.append(i)
        # print('new list', host_name_list)
        # print('my list', len(host_name_list))

        count = 0
        visitor_print = []
        for j in range(len(host_name_list)):
            list_number = host_name_list[count]
            visit_print = visitor_dataframe.iloc[list_number, 5]
            visitor_print.append(visit_print)
            count = count+1
        if visiting_prints in visitor_print:
            tag = visitor_dataframe['PRINTS'].tolist()
            name_position = tag.index(visiting_prints)
            print('welcome our guest', visitor_dataframe.iloc[name_position, 1])

        else:
            print('unknown visitor please sign in')
