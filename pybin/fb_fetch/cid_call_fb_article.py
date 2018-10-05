import requests
import pandas as pd
import json
import sys
import os
import io

from select_from_table import * 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
### Our FB access token ###
bot_token = os.getenv('FB_TOKEN')

### Just for test, so I create a local dictionary ###
fanpage_dict =  [
	{'id':'208298019233442','name':'中正魔術社'},{'id':'306546406360942','name':'少女前線'},{'id':'179873122811969','name':'FF_proj'},
	{'id':'monsterhunter','name':'monsterhunter'},{'id':'shaochienmagic','name':'shaochienmagic'},{'id':'PlayStationTaiwan','name':'PlayStationTaiwan'} ]




#############################################
################## Code #####################

def set_parameter(fanpage_id, article_number):
	tmp_url = ('https://graph.facebook.com/v2.12/{}?fields=id,posts.limit({})&access_token={}'.format(fanpage_id, article_number, bot_token))
	return tmp_url

def print_all_post( start_cid, timeout_limit, article_number ):

	# get the cid list and trimmed it
	# Notice : the return list is tuple of array(list).
	# So I will extract it in below code. 
	cid_list = select_cid_list_from_table("fb_fetch_club")
	cid_list = cid_list[start_cid:]
	last_cid = cid_list[len(cid_list)-1][0]
	
	# Declare a empty array, put all article in this.
	all_article_info = []

	# set a timeout. (Just a count, not releated to time)
	timeout = 0

	# Just a little fun XD
	if_master = input("Do you like be called \"Master\" ? LoL (y or n) ")
	if if_master == "y":
		master = True
		print("Hey Master :>")
	else : 
		master = False
		print("Oh ざんねん desu:<")
		
	for key in cid_list :
		each_id = key[0]
		url = set_parameter(each_id, article_number)
		print("I general a URL !\n--------------------------------------------------------------------------------")
		print(url)
		print("--------------------------------------------------------------------------------\n\n")
		response = requests.get(url) #print(response)
		html = json.loads(response.text.encode())
		#call_limit = {"call_count"    : 0, "total_time"    : 0, "total_cputime" : 0}
		call_limit = json.loads(response.headers['x-app-usage'])
		print("Now, Facebook call count is",call_limit['call_count'],"be careful that if you exceed 80% maybe ... ")

		if 'posts' not in html.keys():
			print("\nHey ... ... \nMaybe you occurred LIMITED By Facebook, QQQ")
			print("Let me print the content of return infomation ...")
			print("\n----------------------------------------The Infomation----------------------------------------\n\n")
			print(html)
			print("----------------------------------------------------------------------------------------------\n\n")
		else :
			datas = html['posts']['data']
		print("OK, I get the id:{}'s datas ! (Make sure data field) ".format(each_id))
		
		'''
		# print data
		for i in range(len(datas)):
			print('=========================================')
			if 'message' in datas[i]:
				print('the '+ str(i) + ' post : ')
				print(datas[i]['message'])
		'''

		# FB keys : created_time  message  id  story
		# DB keys : id cid textid content created_at

		# Convert the FB's keys to Our DB's keys
		for i in range(len(datas)):
			if 'message' not in datas[i].keys():
				print("\nHmm ... I catch someting interseting.\nLet me print tihs : \n", datas[i], "\nBut it isn't a problem. (Maybe)\n")
				continue
			tmp_dict = {}
			tmp_dict['cid'] = each_id
			tmp_dict['textid'] = datas[i]['id']
			tmp_dict['content'] = datas[i]['message']
			tmp_dict['created_at'] = datas[i]['created_time']
			all_article_info.append(tmp_dict)
		#input()
		timeout += 1 
		if timeout >= timeout_limit or last_cid == each_id :
			print("\nHey Master ! I get the ",timeout-1," club's info ! I prepare to wirte in ...")
			insert_data("fb_fetch_article", all_article_info)
			print("Ok, done :)\nThe First club's cid of this batch is ",all_article_info[0]['cid']," , and the last is", all_article_info[timeout-1]['cid'],"\n")
			timeout = 1
			all_article_info=[]
			#input()
					
	#return all_article_info



def main():
	print("\n-----------------------------------\nWelcome to auto crawler system :>\n-----------------------------------\n")
	if len(sys.argv) < 3 : 
		start = 0
		print("Usage: $python cid_call_fb_article.py [start_number] [timeout_limit] [each club how many article]\nYou don't set argv so Default = (0,15,20) !\n")
	else : 
		start = int(sys.argv[1])
		timeout_limit = int(sys.argv[2])
		art_num = int(sys.argv[3])
		print("Setting ... Start to crawler at ", start , "'s club!\nAnd every time I get the ",timeout_limit," club information I will write into Database.(Each club catch ",art_num,"article)\n")
	print_all_post(start, timeout_limit, art_num)
	#insert_data("fb_fetch_article", print_all_post())


if __name__ == '__main__':
    main()

