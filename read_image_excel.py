import cv2
import pandas as pd

input_name = input('enter person print')
input_name=input_name.upper()
dataframe_member = pd.read_excel('Members.xlsx', sheet_name='block_A')
tag = dataframe_member['PRINTS'].tolist()
print(tag)
if input_name  in tag:

    indx = tag.index(input_name)
    photo = dataframe_member.iloc[0, 6]
    print(photo)
    a = cv2.imread(photo)
    cv2.imshow('q',a)
cv2.waitKey(0)
cv2.destroyAllWindows()
