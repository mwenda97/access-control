import pandas as pd
from openpyxl import load_workbook
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import read_registered_members as rdm
import read_or_write_visitor as rwv

dataframe_member = pd.read_excel('Members.xlsx', sheet_name='block_A')
dataframe_visitor = pd.read_excel('Visitors.xlsx', sheet_name='block_A')


def all():
    host_name_list = dataframe_visitor['HOST_NAME'].tolist()
    bn = 'name of member detected'
    cvb = 'visitros finger prints'

    data_member = rdm.read_member(dataframe_member)
    host_name, house_no = data_member
    new_visitors = rwv.new_visitor(host_name, house_no, dataframe_member)
    existing_visitors = rwv.existing_members.read_database(host_name_list, bn, cvb, dataframe_visitor)
    return dataframe_member


def trial():
    host_name_list = dataframe_visitor['HOST_NAME'].tolist()
    while True:
        print('Welcome to Konza city')
        #a = input('is there anyone y for yes or n for no')
        #a = a.upper()
        a = 'Y'
        if a == 'Y':
         #   print('A person has been detected')
            data_member = rdm.read_member(dataframe_member)
            var, tag, my_tag = data_member
            if var == 1:
                print_data = rdm.read_print(dataframe_member, tag, my_tag)
                alert, member, house_no = print_data

                if alert == 0:
                    print('Do you have any vistors')
                    your_ans = input('y  for yes or n for no')
                    your_ans = your_ans.upper()
                    if your_ans == 'Y':
                        how_many = int(input('how many?'))
                        count = 0
                        new_old = input('has your visitor/s been here before? y for yes or n for no')
                        new_old = new_old.upper()

                        if new_old == 'Y':
                            while count < how_many:
                                visiting_prints = input('hello visitor,please scan your prints')
                                visiting_prints = visiting_prints.upper()
                                existing_visitors = rwv.existing_members.read_database(host_name_list, member,
                                                                                       visiting_prints,
                                                                                       dataframe_visitor)

                                count = count + 1
                                pass

                        if new_old == 'N':
                            while count < how_many:
                                new_visitors = rwv.new_visitor(member, house_no, dataframe_member)
                                count = count + 1
                                pass

                    elif your_ans == 'N':
                        print('***WELCOME***')

                elif alert == 1:
                    print('sending alert to security desk')

            elif var == 0:
                print('card ID not known,please try again or consult the security desk')
                pass
        if a == 'N':
            pass



trial()
