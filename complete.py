#!/usr/bin/env python
# coding: utf-8

# 1. 必要なモジュールのimport

# In[152]:


# import time
# import requests
# import urllib.request
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager

# # LINE Notify APIのURL
# url = "https://notify-api.line.me/api/notify"
# # LINE Notifyのトークン
# token = 'fmGPY9XHiQzosJq5L8WrUhB4Hg4aRNOdTXvTcDmJkCs'
# headers = {"Authorization" : "Bearer "+ token}

# # ChromeDriverのオプション設定
# options = Options()
# options.add_argument('--headless')
# service = Service(ChromeDriverManager().install())

# while True:
#     driver = webdriver.Chrome(service=service,options=options)
#     driver.get('https://note.com/physy/n/n324d9d0a93e0')  # 空き状況をチェックするURL

#     # XPathを使用して空き状況を取得
#     availability = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/div[1]/article/div[1]/div/div/div[2]/ul/li[1]/p'))).text

#     # 空き状況をLINE通知APIに送信
#     message =  f'空き状況: {availability}'
#     payload = {"message" :  message}
#     r = requests.post(url ,headers = headers ,params=payload)

#     driver.quit()

#     # 10分待つ
#     time.sleep(600)


# In[153]:


import chromedriver_binary
from selenium import webdriver
import urllib.request as req
import requests
import time
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


# 2. chromedriverのGet(インスタンス化)

# In[154]:

# herokuのchromedriverのPATHを指定
driver_path = '/app/.chromedriver/bin/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
#※headlessにしている
# browser = webdriver.Chrome(options=options, executable_path=driver_path)

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(3)


# In[155]:


# ログインページするサイトへアクセス
url_login = "https://reserve.city.ichikawa.lg.jp/(S(moimti55yyzkzs3ayy52xhyn))/Wg_ModeSelect.aspx"
browser.get(url_login)
time.sleep(3)
print("ログインページにアクセスしました")


# In[156]:


browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/table/tbody/tr/td[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/p/table/tbody/tr[1]/td/input').click()


# In[157]:


checkbox1 = browser.find_element_by_id('dgShisetsuList_ctl04_chkSelectLeft')
checkbox2 = browser.find_element_by_id('dgShisetsuList_ctl04_chkSelectRight')
checkbox3 = browser.find_element_by_id('dgShisetsuList_ctl07_chkSelectLeft')
checkbox4 = browser.find_element_by_id('dgShisetsuList_ctl06_chkSelectRight')
checkbox5 = browser.find_element_by_id('dgShisetsuList_ctl05_chkSelectRight')


# In[158]:


# 2つのチェックボックスにチェックを入れる
checkbox1.click()
checkbox2.click()
checkbox3.click()
checkbox4.click()
checkbox5.click()


# In[159]:


browser.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td/div/table/tbody/tr/td[10]/div/input").click()


# In[160]:


checkbox6 = browser.find_element_by_id('rbtnMonth')
checkbox7 = browser.find_element_by_id('chkSat')
checkbox8 = browser.find_element_by_id('chkSun')
checkbox9 = browser.find_element_by_id('chkHol')
# checkbox10 = browser.find_element_by_id('chkFri')


# In[161]:


checkbox6.click()
checkbox7.click()
checkbox8.click()
checkbox9.click()
# checkbox10.click()


# In[162]:


browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td[10]/div/input').click()


# In[163]:


current_url = browser.current_url


# In[164]:


response = req.urlopen(current_url)


# In[165]:


parse_html = BeautifulSoup(response, 'html.parser')


# In[166]:


parse_html


# In[167]:


# aタグをスクレイピング
links = parse_html.find_all('a')

for link in links:
    print(link.text)


# In[168]:


# 新しい配列を作成
triangle_array = []

# aタグをスクレイピング
links = parse_html.find_all('a')

for link in links:
    # リンクテキストに"△"が含まれているかチェック
    if "△" in link.text:
        # "△"が見つかったら配列に追加
        triangle_array.append(link.text)

# "△"が見つかった場合に通知
if triangle_array:
    print("△が見つかりました:", triangle_array)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[169]:


# id属性を持つ要素を探す
element = parse_html.find(id='dlRepeat_ctl00_tpItem_dgTable_ctl02_b20231202')  # 'your_id'は探したいid属性の値に置き換えてください

# 要素のテキストを取得する
text = element.text


# In[170]:


text


# In[171]:


parse_html.id


# In[172]:


print(parse_html)


# In[173]:


url = "https://notify-api.line.me/api/notify"
headers = {'Authorization': "Bearer"+ " " +"MG2P8bEpDlCwN36BK1VcyIVVRxbxq6fgb41ewqSPk87"}
payload = {'message': triangle_array}
requests.post(url, headers=headers, data=payload)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




