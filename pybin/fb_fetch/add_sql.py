import requests
import pandas as pd
import json
import sys
import io
from dateutil.parser import parse
### config ###

target_fanpage = ""

###  data  ###
# 306546406360942 = gf.txwy.tw
fanpage_dict =  [
	{'id':'208298019233442','name':'中正魔術社'},{'id':'306546406360942','name':'少女前線'},{'id':'179873122811969','name':'FF_proj'},
	{'id':'monsterhunter','name':'monsterhunter'},{'id':'shaochienmagic','name':'shaochienmagic'},{'id':'PlayStationTaiwan','name':'PlayStationTaiwan'} ]


bot_token = 'EAAMsLVshZCncBANlNtqVaPmb8OgwQ5W0wCYkZCh3cPfpr5UwW1Gz4hdTZBos69TW6aphwhlx0FtO9JIpBo1sPxGW3M5uP7urvRSa5SXZCgAn1yvySkZCjxiiLfKqU9AlbNa0RnQB3nOyBJYHkScPPvvN37tMPmCIZD'
FF_proj_token = 'EAANkhTurUYMBADOTtlQTZAr9pFfTe6dr9JXtm6kOgFRZC40VJN7L6KsMjJe8AgUClg45kV1Bv4sFc8ARdGaboYtRxAizQ0UCBbZA2uzXqnKZCqDiaQFI9zQkDWeuJR9PEzbZCaHTT2g9erOXGVa2But9Fr7uwJGunJ9p4xAFVMQZDZD'

### function ###
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def ask_fanpage():
	print('Which fan page do u want? Enter number plz : \n')
	idx = 0
	for key in fanpage_dict:
		print('{},{}'.format(idx,key['name']))
		idx+=1
	print('{},other(enter fanpage id)'.format(idx))
	back = input('')
	print('debug: id is {}'.format( int(back) ))
	if int(back) < idx:
		return fanpage_dict[int(back)]['id']
	else :
		return int(back)

def set_parameter(fanpage_id):
	tmp_url = ('https://graph.facebook.com/v2.12/{}?fields=id,posts.limit(10)&access_token={}'.format(fanpage_id, bot_token))
	return tmp_url

def unique_print_post():
	url = set_parameter(ask_fanpage())
	print(url)
	response = requests.get(url) #print(response)
	html = json.loads(response.text)
	#print(html)

	datas = html['posts']['data']
	for i in range(len(datas)):
		print('=========================================')
		if 'message' in datas[i]:
			print('the '+ str(i) + ' post : ')
			print(datas[i]['message'])

def print_all_post():
	for key in fanpage_dict :
		each_id = key['id'];
		url = set_parameter(each_id)
		print("\n\n\n===")
		print(url)
		print("===\n\n")
		response = requests.get(url) #print(response)
		html = json.loads(response.text.encode())
		#print(html)

		datas = html['posts']['data']
		for i in range(len(datas)):
			print('=========================================')
			if 'message' in datas[i]:
				print('the '+ str(i) + ' post : ')
				print(datas[i]['message'])


def test_sql():
	key = fanpage_dict[0]
	each_id = key['id'];
	url = set_parameter(each_id)
	print("\n\n\n===")
	print(url)
	print("===\n\n")
	response = requests.get(url) #print(response)
	html = json.loads(response.text.encode())
	#print(html)
	datas = html['posts']['data']
	#print(key['name']);
	setsal_insert_data( html['id'], key['name'], datas )
	print("Success ? ")



### main
print_all_post()
#test_sql()
