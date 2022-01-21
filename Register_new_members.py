import pandas as pd
from openpyxl import load_workbook
import take_save_pic as tsp


def input_member_deta():
    print('follow the guidelines to register new member')
    name = input('\n Enter Member Names:')
    names = name
    name = name.upper()
    id_no = int(input('\nEnter Members ID_no'))
    house = input('\nEnter house number')
    house = house.upper()
    rfid = input('enter rfid uid')
    rfid = rfid.upper()
    tel_no = int(input('enter your phone number'))
    prints = input('enter finger print id')
    prints = prints.upper()
    tsp.take_photo(names)

    reader = pd.read_excel(r'Members.xlsx')
    df = pd.DataFrame({'NAME': [name],
                       'ID_NO': [id_no],
                       'HOUSE_NO': [house],
                       'RFID_TAG ': [rfid],
                       'TEL_NO': [tel_no],
                       'PRINTS': [prints],
                       'PHOTO': ['captured_photo/' + names + '.jpg']})
    book = load_workbook('Members.xlsx')
    writer = pd.ExcelWriter('Members.xlsx', engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    df.to_excel(writer, header=False, startrow=len(reader) + 1, sheet_name='block_A', index=False)
    writer.save()


input_member_deta()
