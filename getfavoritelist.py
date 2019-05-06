# -*- coding: utf-8 -*-
import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み
import datetime
import time
import pytz
import textanalyze


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

def jst_ymd(at):
	t = time.strptime(at,'%a %b %d %H:%M:%S +0000 %Y')
	utc = pytz.timezone('UTC')
	d = datetime.datetime(*t[:6], tzinfo=utc)
	tm = d.astimezone(pytz.timezone('Asia/Tokyo'))
	zn = tm.strftime('%Y-%m-%d %H:%M:%S %Z%z')
	ymd = tm.strftime('%Y-%m-%d')
	
	return(ymd)

def get_list(account_id):

	url = "https://api.twitter.com/1.1/favorites/list.json?screen_name="+account_id #タイムライン取得エンドポイント

	params ={'count' : 100} #取得数
	res = twitter.get(url, params = params)
	reg_date = False
	data = []

	if res.status_code == 200: #正常通信出来た場合
		timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
		for line in timelines: #タイムラインリストをループ処理
			text = textanalyze.chrono(line['text'],'')
			text = json.loads(text)
			if len(text['datetime_list']) > 0:
				print(text['datetime_list'])
				print(line['user']['name']+'::'+line['text'])
				created_at = jst_ymd(line['created_at'])
				date = text['datetime_list'][0][0]
				twitter_url = 'https://twitter.com/'+ line['user']['screen_name'] + '/status/' + line['id_str']
				if '今日' == date or '本日' == date:
					reg_date = created_at
				else:
					reg_date = text['datetime_list'][0][1]

				start_dt = datetime.datetime.strptime(reg_date,'%Y-%m-%d')
				end_dt = start_dt+datetime.timedelta(days=1)
				start_dt = start_dt.strftime('%Y%m%d')
				end_dt = end_dt.strftime('%Y%m%d')
				line['text'] = line['text'].replace(" ","")
				line['text'] = line['text'].replace("\n","")

				cal_url = 'http://www.google.com/calendar/event?action=TEMPLATE&text='+line['text'][1:20]+'&details='+line['text']+'&dates='+start_dt+'/'+end_dt
				

				data_dic = {}
				data_dic['date'] = reg_date
				data_dic['text'] = line['text']
				data_dic['twi_url'] = twitter_url		
				data_dic['cal_url'] = cal_url		

				data.append(data_dic)
	else: #正常通信出来なかった場合
		print("Failed: %d" % res.status_code)

	return data