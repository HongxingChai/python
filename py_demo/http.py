import requests
import re

url = """https://m.biquku.com/6/6343/13201070.html"""
headers = {'User-Agent': 'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}
response = requests.get(url,headers=headers)
raw_url = response.url
# print(response.headers)
print(raw_url)
# print(response.text)
# html2 = raw_url.find_element_by_xpath("//*").get_attribute("outerHTML")
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
apk = re.findall(pattern,response.text)
print(apk)
