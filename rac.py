from codecs import unicode_escape_decode
from unicodedata import unidata_version
from requests import session

uid_tiktok= 'duongthanhtuyen20'
token_tds = '&access_token=TDS0nIwEjclZXZzJiOiIXZ2V2ciwiI5Ijbp12Zu92YiojIyV2c1Jye'

url_cauhinh = 'https://traodoisub.com/api/?fields=tiktok_run&id='+uid_tiktok+token_tds
url_nhiemvu = 'https://traodoisub.com/api/?fields=tiktok_like&access_token='+token_tds

all_urlsetting = url_cauhinh
all_url_like = url_nhiemvu + token_tds
s = session()
def setting_cau_hinh():
    url_get = s.get(all_urlsetting)
    print(url_get.text)
    
def list_nhiemvu_like():
    url_get = s.get(url_nhiemvu)
    for x in url_get.json ()['data']:
        if 'link' in x:
            print(x['link'])

setting_cau_hinh()
list_nhiemvu_like()
