import pandas as pd
import glob
import os
path=r'C:\Users\........' #Folder name
filenames=glob.glob(path+ "/*.xlsx")
filenames # output will be the name of files present in the folder
#initializing data frame
concat7=pd.DataFrame()  
df=pd.DataFrame()  
for file in filenames:
    df=pd.read_excel(file,sheet_name=None,header=0,dtype=object)
#                      coverters={'C1':str,'C2':str,'C3':str})
#  skiprows=None,nrows=None,usecols=None,index_col=None,  
    concat2=pd.concat(df,sort=False)
    concat7=concat7.append(concat2)
concat7
#reset index
concat7.reset_index(inplace=True)
concat7
#to remove extra columns
con=pd.DataFrame()
con=concat7.iloc[:,2:]
con
#Convert in to excel
writer=pd.ExcelWriter(r'C:\\Users\......\\FinalBook.xlsx') #path where you want new file to be created
con.to_excel(writer)
writer.save()