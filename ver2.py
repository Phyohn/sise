# ver1.py
#python -i
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
import readline


def yes_no_input():
	while True:
		choice = input("        OK? yes' or 'no' [y/N]:  ( q = quit )").lower()
		if choice in ['y', 'ye', 'yes']:
			return True
		elif choice in ['n', 'no']:
			return False
		elif choice in ['q', 'Q']:
			return quit()

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
			try:
				return ((94 - (l_diff[0][1]))*53)
			except IndexError as e:
				return(00)
				print("IndexError")

def csv_stdout(df_c):
	return df_c.to_csv(sys.stdout)

top_d = "/Users/mac2018/Applications/Collection/sise/tmp/"
#TOP_DIR = os.path.dirname(__file__)
TOP_DIR = os.path.dirname(top_d)
LIST_DIR = os.path.join(TOP_DIR, 'dailist/')
ZERO_IMG = os.path.join(TOP_DIR, 'graph.png')

#holl stock
inter_ls = ('pmc=26036001', 200, 'inter')
o_kura_ls = ('pmc=17008002', 2590, 'o_kura')
ktakaoka_ls = ('pmc=21018018', 4000, 'ktakaoka')
taiyo_ls = ('pmc=18001006', 280, 'taiyo')
lapark_ls = ('pmc=21018015', 3240, 'lapark')
kakeo_ls = ('pmc=16006037', 324, 'kakeo')
himi_ls = ('pmc=16006008',  225, 'himi')
yosi_ls = ('pmc=16006002', 192, 'yosi')
tonanor_ls = ('pmc=16006020', 156, 'tonanor')
tonasupa_ls = ('pmc=26036006', 212, 'tonasupa')
quatoro_ls = ('pmc=18007010', 288, 'quatoro')



main_df = pd.read_csv('datapy.txt',names=('eigenvalue','dai','Rotation','BB','RB','difference','max','model','hollcode'))
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

#hollname_list
hollname_list = comp['hollcode'].drop_duplicates().tolist()

#4.9
#auto model_name_bank
today_df = pd.DataFrame(comp['model'].drop_duplicates())
today_df['fuga'] = '0'
stock_df = pd.read_csv('namebank.csv',names=('model','renamed_model_name'))
today_merged = pd.merge(today_df, stock_df  , how='outer').drop(columns='fuga')
na_posi_df  =  today_merged.sort_values('renamed_model_name', na_position='first')
empty_value_bool = (na_posi_df['renamed_model_name'].isnull())
new_model_list = (na_posi_df['model'])[empty_value_bool].tolist()

#4.9
#empty judgment
if len(new_model_list)!=0:
	print("new_machine_arrive!")

	renamed_new_model_list = []
	for new_model in new_model_list:
		print (new_model)
		newshortname = input("new_machine_name_input ( q = quit ):")
		if newshortname == "q" :
			print("Finish!")
			quit()
			brake
		else:
			print(newshortname)
			renamed_new_model_list.append(newshortname)
	zippedlist =  list(zip(new_model_list, renamed_new_model_list))
	print(zippedlist)
	df_by_list = pd.DataFrame(zippedlist, columns = ['model', 'renamed_model_name'])
	added_sorted_model_df = pd.merge(na_posi_df, df_by_list, on=('model', 'renamed_model_name'), how = 'outer').drop_duplicates(subset='model', keep='last')
	sorted_model_df = added_sorted_model_df.sort_values('renamed_model_name', na_position='first')
	sorted_model_df.to_csv('./namebank.csv', header=False, index=False)
	print("New_machine_names_addition completed")

time.sleep(1)


"""
if empty_value.sum() > 0 :
	csv_stdout(sorted_model_df)
	new_model_list = (sorted_model_df['model'])[empty_value].tolist()
	renamed_new_model_list = []
	for new_model in new_model_list:
		newshortname = input(f"new model arrive. {new_model}  (q = quit) Input newname. ")
		if newshortname == "q" :
			print("Finish!")
			quit()
			brake
		else:
			print(f'{new_model} is "{newshortname}"')
			if yes_no_input():
				renamed_new_model_list.append(newshortname)	
			else:
				pass
	'''	
	create a zipped list of tuples from above lists
	'''
	
	zippedlist =  list(zip(new_model_list, renamed_new_model_list))
	
	'''
	create df
	'''
	df_by_list = pd.DataFrame(zippedlist, columns = ['model', 'renamed_model_name'])
	added_sorted_model_df = pd.merge(sorted_model_df, df_by_list, on=('model', 'renamed_model_name'), how = 'outer').drop_duplicates(subset='model', keep='last')
	#sorted_model_df = sorted_model_df.replace( new_model_list, renamed_new_model_list)
	print("done!")
	sorted_model_df = added_sorted_model_df.sort_values('renamed_model_name', na_position='first')
else:
	pass
print("all model name has arrived")
sorted_model_df.to_csv('./namebank.csv', header=False, index=False)
"""

#rename
dailist_df=  pd.read_csv('namebank.csv', header=None, names=('model','shortnames'))
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


#namebank.csvの撤去台情報を削除する

#dailist_dfはカラム名をつけて使い回し
#最新台番はmain_dfからハードコピー
#現在の台用のファイルが必要tmp_dai.txt
#tmp_dai.txtを出力後同じdfでdailist_dfとインナーマージ
#初回は貯まるまで最終マージできない


#名前追加時のif文で分岐とする
if len(new_model_list)!=0:
	tmp_dai = pd.read_csv('tmp_dai.txt', names=('model', 'day'))
	today_df = main_df.iloc[:,7:9].copy()
	dup_today_df = today_df.drop_duplicates(subset='model', keep='last').copy()
	dup_today_df['day'] = intdt
	drop_today_df = dup_today_df.drop(columns='hollcode')
	new_tmp_dai = pd.merge(drop_today_df, tmp_dai, how = 'outer', on ='model').drop(columns='day_x')
	sorted_new_tmp_dai = new_tmp_dai.sort_values('model', na_position='first')
	dropna_new_tmp_dai = sorted_new_tmp_dai.dropna(subset=['model'], axis=0)
	dup_new_tmp_dai = dropna_new_tmp_dai.drop_duplicates(subset='model')
	dup_new_tmp_dai.to_csv('./tmp_dai.txt', header=False, index=False)
	inner_name_df = pd.merge(dup_new_tmp_dai, dailist_df, how = 'inner', on ='model').drop(columns='day_y')
	droped_inner_df = inner_name_df.sort_values('model', na_position='first').dropna(subset=['model'], axis=0)
	droped_inner_df.to_csv('./namebank.csv', header=False, index=False)



#hollname sequence

def test(str1, int, str2):
	test_df =  (comp[comp['hollcode'] == str1]).sort_values('dai')
	if  len(test_df) == int:
		test_df_st = test_df.drop(columns=['hollcode'])
		test_df_st.to_csv(f'/Users/mac2018/Applications/Collection/linkdata/{str2}.csv', header=False, index=False)
	else:
		test_df.insert(0,'dai_num_check',test_df.loc[:,'dai']) 
		dai_num_check_df = pd.read_csv(f'./dailist/{str2}dailist.csv',names=('dai_num_check','empty'),dtype='int64')
		merged_df = pd.merge(test_df, dai_num_check_df, how='outer')
		droped_df = merged_df.drop(columns=['hollcode','dai','empty'])
		droped_df['date'] = droped_df['date'].fillna(method='ffill')
		droped_df['model'] = droped_df['model'].fillna('空台')
		fillnaed_df = droped_df.fillna(0)
		int_df = fillnaed_df.astype({'dai_num_check': 'int64','Rotation':'int64','BB':'int64','RB':'int64','difference':'int64','max':'int64','model':'str','date':'int64'})
		test_df_re = int_df.drop_duplicates(subset=['dai_num_check']).sort_values('dai_num_check')
		test_df_re.to_csv(f'/Users/mac2018/Applications/Collection/linkdata/{str2}.csv', header=False, index=False)

#loop hollname_list
for holl in hollname_list :
	if holl == 'pmc=26036001':
		test(*inter_ls)
		print('inter')
	elif holl == 'pmc=17008002':
		test(*o_kura_ls)
		print('o_kura')
	elif holl == 'pmc=21018018':
		test(*ktakaoka_ls)
		print('ktakaoka')
	elif holl == 'pmc=18001006':
		test(*taiyo_ls)
		print('taiyo')
	elif holl == 'pmc=21018015':
		test(*lapark_ls)
		print('lapark')
	elif holl == 'pmc=16006037':
		test(*kakeo_ls)
		print('kakeo')
	elif holl == 'pmc=16006008':
		test(*himi_ls)
		print('himi')
	elif holl == 'pmc=16006002':
		test(*yosi_ls)
		print('yosi')
	elif holl == 'pmc=16006020':
		test(*tonanor_ls)
		print('tonanor')
	elif holl == 'pmc=26036006':
		test(*tonasupa_ls)
		print('tonasupa')
	elif holl == 'pmc=18007010':
		test(*quatoro_ls)
		print('quatoro')
	else:
		pass

#*tuple open
#test(*inter_ls)
#test(*o_kura_ls)
#test(*ktakaoka_ls)
#test(*taiyo_ls)
#test(*lapark_ls)
#test(*kakeo_ls)
#test(*himi_ls)
#test(*yosi_ls)
#test(*tonanor_ls)
#test(*tonasupa_ls)
#test(*quatoro_ls)

#str1 = 'pmc=21018015'
#int = 3240
#str2 = 'lapark'




'''
#output 
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
'''
quit()