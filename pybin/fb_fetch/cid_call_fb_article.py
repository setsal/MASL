import requests
import pandas as pd
import json
import sys
import io

from select_from_table import * 

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

### Just for test, so I create a local dictionary ###
fanpage_dict =  [
	{'id':'208298019233442','name':'中正魔術社'},{'id':'306546406360942','name':'少女前線'},{'id':'179873122811969','name':'FF_proj'},
	{'id':'monsterhunter','name':'monsterhunter'},{'id':'shaochienmagic','name':'shaochienmagic'},{'id':'PlayStationTaiwan','name':'PlayStationTaiwan'} ]

### Our FB access token ###

bot_token = 'EAAMsLVshZCncBANlNtqVaPmb8OgwQ5W0wCYkZCh3cPfpr5UwW1Gz4hdTZBos69TW6aphwhlx0FtO9JIpBo1sPxGW3M5uP7urvRSa5SXZCgAn1yvySkZCjxiiLfKqU9AlbNa0RnQB3nOyBJYHkScPPvvN37tMPmCIZD'
FF_proj_token = 'EAANkhTurUYMBADOTtlQTZAr9pFfTe6dr9JXtm6kOgFRZC40VJN7L6KsMjJe8AgUClg45kV1Bv4sFc8ARdGaboYtRxAizQ0UCBbZA2uzXqnKZCqDiaQFI9zQkDWeuJR9PEzbZCaHTT2g9erOXGVa2But9Fr7uwJGunJ9p4xAFVMQZDZD'

def set_parameter(fanpage_id):
	tmp_url = ('https://graph.facebook.com/v2.12/{}?fields=id,posts.limit(20)&access_token={}'.format(fanpage_id, bot_token))
	return tmp_url

def print_all_post():
	cid_list = select_cid_list_from_table("fb_fetch_club")
	all_article_info = []

	timeout = 0

	for key in cid_list :
		each_id = key[0]
		url = set_parameter(each_id)
		print("\n\n\n===")
		print(url)
		print("===\n\n")
		response = requests.get(url) #print(response)
		html = json.loads(response.text.encode())
		#print(html)

		datas = html['posts']['data']
		print("I get the id:{}'s datas !  ".format(each_id))
		
		'''
		# print data
		for i in range(len(datas)):
			print('=========================================')
			if 'message' in datas[i]:
				print('the '+ str(i) + ' post : ')
				print(datas[i]['message'])
		'''
		# FB : created_time  message  id  story
		# DB : id cid textid content created_at
		for i in range(len(datas)):
			if 'message' not in datas[i].keys():
				continue
			tmp_dict = {}
			tmp_dict['cid'] = each_id
			tmp_dict['textid'] = datas[i]['id']
			tmp_dict['content'] = datas[i]['message']
			tmp_dict['created_at'] = datas[i]['created_time']
			all_article_info.append(tmp_dict)
		#input()
		timeout += 1 
		if timeout > 5:
			insert_data("fb_fetch_article", all_article_info)
			timeout = 1
			all_article_info=[]
					
	#return all_article_info



def main():
	print(print_all_post())
	#insert_data("fb_fetch_article", print_all_post())


if __name__ == '__main__':
    main()

