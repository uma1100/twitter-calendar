import json
import requests
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み


app_id = "APP_ID"
url_chrono = "https://labs.goo.ne.jp/api/chrono"

# See sample response below.
def chrono(sentence, class_filter, request_id="record002"):
	payload = {"app_id": app_id, "request_id": request_id, "sentence": sentence, "class_filter": class_filter}
	headers = {'content-type': 'application/json'}
	r = requests.post(url_chrono, data=json.dumps(payload), headers=headers)
	return (r.text)