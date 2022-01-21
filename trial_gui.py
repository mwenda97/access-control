import pandas as pd
from openpyxl import load_workbook
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import read_registered_members as rdm
import read_or_write_visitor as rwv

dataframe_member = pd.read_excel('Members.xlsx', sheet_name='block_A')
dataframe_visitor = pd.read_excel('Visitors.xlsx', sheet_name='block_A')

