# ver1.py

import base64
import cv2
import datetime
import io
import numpy as np
import os
import pandas as pd
import pathlib
import platform
from PIL import Image
import sys
import time

def yes_no_input():
	while True:
		choice = input("Please respond with 'today? yes' or 'no' [y/N]: ").lower()
		if choice in ['y', 'ye', 'yes']:
			return True
		elif choice in ['n', 'no']:
			return False

def diff_num(s):
	if len(s) == 2824:
		return (np.int64(0))
	else:
		pilim = Image.open(io.BytesIO((base64.b64decode(s))))
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

def csv_stdout(df_c):
	return df_c.to_csv(sys.stdout)

TOP_DIR = os.path.dirname(__file__)
LIST_DIR = os.path.join(TOP_DIR, 'dailist/')
ZERO_IMG = os.path.join(TOP_DIR, 'graph.png')


main_df = pd.read_csv('datapy.txt',names=('eigenvalue','dai','Rotation','BB','RB','difference','max','machine'))
slump_df = pd.read_csv('py.txt',names=('eigenvalue','base64'))
dfm = pd.merge(main_df, slump_df)
diff_num_base64 = dfm['base64'].values
zeroim = np.rot90((cv2.cvtColor(cv2.imread(ZERO_IMG), cv2.COLOR_BGR2GRAY))[16:208,9:])

diff_num_list = []
for (s) in diff_num_base64:
	print (diff_num(s))
	diff_num_list.append(diff_num(s))

dfm['difference'] = diff_num_list
comp = dfm.drop(columns = ['base64','eigenvalue'])

#2/1quatoro daicount judge tonanor156 2/2 la328+2 ktaka 399+1 o-kura 259+44
#dailist series to df
#len(df)q=282
'''
def holl_judge(c):
	if len(c) == 200:
		return "inter"
	elif len(c) == 259:
		return "o-kura"
	elif len(c) == 399:
		return "ktakaoka"
	elif len(c) == 280:
		return "taiyotakaoka"
	elif len(c) == 328:
		return "lapark"
	elif len(c) == 324:
		return "kakeo"
	elif len(c) == 225:
		return "himi"
	elif len(c) == 192:
		return "yosi"
	elif len(c) == 156:
		return "tonanor"
	elif len(c) == 212:
		return "tonasupa"
	elif len(c) == 297:
		return "quatoro"
'''

if  len(comp) == 282: #Q
	list_df = pd.read_csv('./dailist/quatorodailist.csv',names=('dai','hoge'))
	merged_df = pd.merge(comp,list_df, on='dai' ,how='outer').drop( columns = 'hoge')
	fillnaed_df = merged_df.fillna(0)
	int_df = fillnaed_df.astype({'dai': 'int64','Rotation':'int64','BB':'int64','RB':'int64','difference':'int64','max':'int64','machine':'str'})
	comp = int_df.drop_duplicates(subset=['dai']).sort_values('dai')


elif len(comp) == 156: #tonanor
	print("tonanor_ok")
elif len(comp) == 328: #la
	posdai = comp.loc[:,'dai'].unique()
	comp.insert(0,'posdai',posdai)
	dailist = pd.read_csv('./dailist/laparkdailist.csv',names=('posdai','kuu'))
	comp = pd.merge(comp, dailist, how='outer')
	comp = comp.reindex(columns=['posdai','Rotation','BB','RB','difference','max','machine'])
	comp = comp.fillna(0)
	comp = comp.astype({'posdai': 'int64','Rotation':'int64','BB':'int64','RB':'int64','difference':'int64','max':'int64','machine':'str'})
	comp = comp.sort_values('posdai')
	print("la_2daiplus")
elif len(comp) == 399: #ktaka
	posdai = comp.loc[:,'dai'].unique()
	comp.insert(0,'posdai',posdai)
	dailist = pd.read_csv('./dailist/ktakaokadailist.csv',names=('posdai','kuu'))
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
#defdai = comp.loc[:,'machine'].unique()

#series to df
#defdaidf = pd.DataFrame(defdai)
#defdaidf.insert(0,'namebank', defdai)
#dainame = pd.read_csv('namebank.csv',names=('namebank','neoname'))
#drop_duplicates(subset=['namebank']
#dainame = dainame.drop_duplicates(subset=['namebank'])
#newdailist = pd.merge(defdaidf, dainame, how='outer')
#newdailist = newdailist.reindex(columns=['namebank','neoname'])
#newdailist.to_csv('./namebank.csv', header=False, index=False)


#auto machine_name_bank
machine_name_df = pd.DataFrame(comp['machine'].drop_duplicates())
machine_name_df['fuga'] = '0'
rename_list_df = pd.read_csv('namebank.csv',names=('machine','renamed_machine_name'))
merged_machine_name_df = pd.merge(machine_name_df, rename_list_df , how='outer').drop(columns='fuga')
sorted_machine_df = merged_machine_name_df.sort_values('renamed_machine_name', na_position='first')
sorted_machine_df.to_csv('./namebank.csv', header=False, index=False)

empty_value = (sorted_machine_df['renamed_machine_name'].isnull())
if empty_value.sum() > 0 :
	print("new machine arrive")
	print("open namebank.txt. register the update name")
	print("Please re-execute after registration")
	csv_stdout(sorted_machine_df)
	quit()
else:
	print("all model name has arrived")


#rename
dailist_df=  pd.read_csv('namebank.csv', header=None)
longname_list = (dailist_df.iloc[:,0]).values.tolist()
shortname_list = (dailist_df.iloc[:,1]).values.tolist()
comp = comp.replace(longname_list,shortname_list)


#datetime to date

today = datetime.datetime.now()
intdt= int(today.strftime('%Y%m%d'))
print(f'datetime is{intdt}?')

if __name__ == '__main__':
	if yes_no_input():
		d = datetime.datetime.now()
	else:
		d = datetime.datetime.now() - datetime.timedelta(days=1)

intdt= int(d.strftime('%Y%m%d'))
print(intdt)
comp['date'] = intdt

now = datetime.datetime.now()
strdate = now.strftime('%m:%d %H:%M:%S')
comp.to_csv(f'/Users/mac2018/Applications/Collection/linkdata/{strdate}.csv', header=False, index=False)
#comp.to_csv(sys.stdout)
csv_stdout(comp)

if (comp.isnull().values.sum() != 0):
	print ("missing value")
	print (comp.shape)
else:
	print ("OK")
	print (comp.shape)
quit()