import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile





class existing_members:
    def duplicates(lst, item):
        www = []
        for i, x in enumerate(lst):
            if x == item:
                www.append(i)
        print('see', www)
        m = len(www)
        print('my people',m)


