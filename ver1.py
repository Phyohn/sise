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

now = datetime.datetime.now()
strdate = now.strftime('%m:%d %H:%M:%S')
comp.to_csv(f'../{strdate}.csv', header=False, index=False)

if (comp.isnull().values.sum() != 0):
	print ("Missing value")
	print (comp.shape)
else:
	print ("OK")
	print (comp.shape)
quit()