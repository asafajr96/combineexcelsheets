#Make sure this python script is in the same folder as all the excel sheets you wish to combine.

import os
import pandas as pd  #if you get 'unable to install pandas' error. run  'pip install pandas' in your terminal.
cwd = os.path.abspath('') #Insert path to folder containing excel
files = os.listdir(cwd)  
df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file), ignore_index=True) 
df.head() 
df.to_excel('merged.xlsx')