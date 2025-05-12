import os
import requests
id=1632106161091
session = requests.Session()
session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
            "Referer": "https://libwx1.fjjxu.edu.cn/smfront_mobile/",
            "Origin": "https://libwx1.fjjxu.edu.cn"
        }
resp = session.post(
        url=f"https://libwx1.fjjxu.edu.cn/smserver/public/api/m8/readers/{id}/{id}"
)
resp.raise_for_status()
new_token = resp.json()['data']['jwtToken']
new_token="Bearer "+new_token
for i in range(476,542):
    rese_url=f"https://libwx1.fjjxu.edu.cn/smserver/public/api/seats-do/qh?seat_id={i}&reader_card={id}&reader_pwd={id}"
    session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
            "Referer": "https://libwx1.fjjxu.edu.cn/smfront_mobile/",
            "Origin": "https://libwx1.fjjxu.edu.cn",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Authorization":new_token,
        }
    resp = session.post(
        url=rese_url
    )
    print(resp.text)
    if resp.json()['code']==200:
        break
