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


options = Options()
options.add_argument('--headless') #browser操作を確認しない場合
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(3)


# ログインページするサイトへアクセス
url_login = "https://reserve.city.ichikawa.lg.jp/(S(moimti55yyzkzs3ayy52xhyn))/Wg_ModeSelect.aspx"
browser.get(url_login)
time.sleep(3)
print("ログインページにアクセスしました")

browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/table/tbody/tr/td[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/p/table/tbody/tr[1]/td/input').click()
time.sleep(3)

checkbox1 = browser.find_element_by_id('dgShisetsuList_ctl04_chkSelectLeft')
checkbox2 = browser.find_element_by_id('dgShisetsuList_ctl04_chkSelectRight')
checkbox3 = browser.find_element_by_id('dgShisetsuList_ctl07_chkSelectLeft')
checkbox4 = browser.find_element_by_id('dgShisetsuList_ctl06_chkSelectRight')
checkbox5 = browser.find_element_by_id('dgShisetsuList_ctl05_chkSelectRight')

# 2つのチェックボックスにチェックを入れる
checkbox1.click()
checkbox2.click()
checkbox3.click()
checkbox4.click()
checkbox5.click()
time.sleep(3)

browser.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td/div/table/tbody/tr/td[10]/div/input").click()
time.sleep(3)

checkbox6 = browser.find_element_by_id('rbtnMonth')
checkbox7 = browser.find_element_by_id('chkSat')
checkbox8 = browser.find_element_by_id('chkSun')
checkbox9 = browser.find_element_by_id('chkHol')
# checkbox10 = browser.find_element_by_id('chkFri')


checkbox6.click()
checkbox7.click()
checkbox8.click()
checkbox9.click()
# checkbox10.click()
time.sleep(3)


browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td[10]/div/input').click()
time.sleep(3)


current_url = browser.current_url


response = req.urlopen(current_url)


parse_html = BeautifulSoup(response, 'html.parser')

# aタグをスクレイピング
links = parse_html.find_all('a')

for link in links:
    print(link.text)

# ブラウザを終了する
browser.close()

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
else:
    print("空きがありませんでした")


url = "https://notify-api.line.me/api/notify"
headers = {'Authorization': "Bearer"+ " " +"MG2P8bEpDlCwN36BK1VcyIVVRxbxq6fgb41ewqSPk87"}
payload = {'message': triangle_array}
requests.post(url, headers=headers, data=payload)

