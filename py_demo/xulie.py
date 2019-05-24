import re

from bs4 import BeautifulSoup
from selenium import webdriver

WIDTH = 480
HEIGHT = 800
PIXEL_RATIO = 3.0
UA = 'User-Agent: MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

url='https://app.86crossocean.com/dr9/'
mobile_driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
mobile_driver.get(url)
html2 = mobile_driver.find_element_by_xpath("//*").get_attribute("outerHTML")
soup2 = BeautifulSoup(html2, 'lxml')
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
apk = re.findall(pattern,html2)
print('apk链接序列：',apk)
for t in apk:
    if t.find('apk') > -1:
        print('if链接：',t)
mobile_driver.close()