# ver1.py
import cv2
import base64
import numpy as np
from PIL import Image
import io
import pandas as pd
import os
import pathlib
import datetime
import time
import platform

zeroim = np.rot90((cv2.cvtColor(cv2.imread('/Users/mac2018/Applications/Collection/sise/tmp/graph.png'), cv2.COLOR_BGR2GRAY))[16:208,9:])

datapy = pd.read_csv('datapy.txt',names=('eigenvalue','dai','Rotation','BB','RB','difference','max','machine'))
py = pd.read_csv('py.txt',names=('eigenvalue','base64st'))
dfm = pd.merge(datapy, py)
dfm_num = dfm['base64st'].values

def samai(sgraph):
	if len(sgraph) == 2824:
		return (np.int64(0))
	else:
		pilim = Image.open(io.BytesIO((base64.b64decode(sgraph))))
		numim = np.array(pilim)
		numim = cv2.cvtColor(numim, cv2.COLOR_BGR2GRAY)
		numim = np.rot90(numim[16:208,9:])
		im_diff = zeroim.astype(int) - numim.astype(int)
		im_diff = im_diff[22:,:]
		if (im_diff.max()) < np.int64(50):
			return (np.int64(0))
		else:
			l_diff = list(zip(*np.where( im_diff > 60 )))
			return ((94 - (l_diff[0][1]))*53)

result = []
for (sgraph) in dfm_num:
	print (samai(sgraph))
	result.append(samai(sgraph))

samai = pd.Series(result)
dfm.loc[:,'difference'] = samai
comp = dfm.iloc[:,1:8]

#2/1quatoro daicount judge tonanor156 2/2 la328+2 ktaka 399+1 o-kura 259+44
#dailist series to df
#len(df)q=282
if len(comp) == 282: #Q
	posdai = comp.loc[:,'dai'].unique()
	comp.insert(0,'posdai',posdai)
	dailist = pd.read_csv('./dailist/quatorodailist.csv',names=('posdai','kuu'))
	comp = pd.merge(comp, dailist, how='outer')
	comp = comp.reindex(columns=['posdai','Rotation','BB','RB','difference','max','machine'])
	comp = comp.fillna(0)
	comp = comp.astype({'posdai': 'int64','Rotation':'int64','BB':'int64','RB':'int64','difference':'int64','max':'int64','machine':'str'})
	comp = comp.sort_values('posdai')
	print("Q_")
elif len(comp) == 156: #tonanor
	print("tonanor_ok")
elif len(comp) == 328: #la
	posdai = comp.loc[:,'dai'].unique()
	comp.insert(0,'posdai',posdai)
	dailist = pd.read_csv('./dailist/ladailist.csv',names=('posdai','kuu'))
	comp = pd.merge(comp, dailist, how='outer')
	comp = comp.reindex(columns=['posdai','Rotation','BB','RB','difference','max','machine'])
	comp = comp.fillna(0)
	comp = comp.astype({'posdai': 'int64','Rotation':'int64','BB':'int64','RB':'int64','difference':'int64','max':'int64','machine':'str'})
	comp = comp.sort_values('posdai')
	print("la_2daiplus")
elif len(comp) == 399: #ktaka
	posdai = comp.loc[:,'dai'].unique()
	comp.insert(0,'posdai',posdai)
	dailist = pd.read_csv('./dailist/ktakadailist.csv',names=('posdai','kuu'))
	comp = pd.merge(comp, dailist, how='outer')
	comp = comp.reindex(columns=['posdai','Rotation','BB','RB','difference','max','machine'])
	comp = comp.fillna(0)
	comp = comp.astype({'posdai': 'int64','Rotation':'int64','BB':'int64','RB':'int64','difference':'int64','max':'int64','machine':'str'})
	comp = comp.sort_values('posdai')
	print("ktaka_1daiplus")
elif len(comp) == 259: #o-kura
	posdai = comp.loc[:,'dai'].unique()
	comp.insert(0,'posdai',posdai)
	dailist = pd.read_csv('./dailist/o-kuradailist.csv',names=('posdai','kuu'))
	comp = pd.merge(comp, dailist, how='outer')
	comp = comp.reindex(columns=['posdai','Rotation','BB','RB','difference','max','machine'])
	comp = comp.fillna(0)
	comp = comp.astype({'posdai': 'int64','Rotation':'int64','BB':'int64','RB':'int64','difference':'int64','max':'int64','machine':'str'})
	comp = comp.sort_values('posdai')
	print("o-ku_44daiplus")
else:
	print("no missing dai")

#1/30auto seriesmachine bank
#pd.Series.unique()
defdai = comp.loc[:,'machine'].unique()

#series to df
defdaidf = pd.DataFrame(defdai)
defdaidf.insert(0,'namebank', defdai)
dainame = pd.read_csv('namebank.csv',names=('namebank','neoname'))
#drop_duplicates(subset=['namebank']
dainame = dainame.drop_duplicates(subset=['namebank'])
newdailist = pd.merge(defdaidf, dainame, how='outer')
newdailist = newdailist.reindex(columns=['namebank','neoname'])
newdailist.to_csv('./namebank.csv', header=False, index=False)


#1/30,name.txt to String conversion
dainame = pd.read_csv('namebank.csv', header=None)
#tolist
machinename = (dainame.iloc[:,0]).values.tolist()
newname = (dainame.iloc[:,1]).values.tolist()
#replace
comp = comp.replace(machinename,newname)

#y/n date today?
#y/Ndef
def yes_no_input():
	while True:
		choice = input("Please respond with 'today? yes' or 'no' [y/N]: ").lower()
		if choice in ['y', 'ye', 'yes']:
			return True
		elif choice in ['n', 'no']:
			return False
'''
datetime to date
'''
if __name__ == '__main__':
	if yes_no_input():
		d = datetime.datetime.now()
	else:
		d = datetime.datetime.now() - datetime.timedelta(days=1)
#8 digits to int
intdt= int(d.strftime('%Y%m%d'))
print(intdt)
#'date'.values replace intdt all
comp['date'] = intdt

now = datetime.datetime.now()
strdate = now.strftime('%m:%d %H:%M:%S')
comp.to_csv(f'/Users/mac2018/Applications/Collection/linkdata/{strdate}.csv', header=False, index=False)

if (comp.isnull().values.sum() != 0):
	print ("Missing value")
	print (comp.shape)
else:
	print ("OK")
	print (comp.shape)
quit()