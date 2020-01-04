import requests
from bs4 import BeautifulSoup
import time
from informMyself import send_mail

URL = 'https://jingfeipeng.github.io/'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}


def checkName():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="headerNameText").get_text()
    # print(soup.prettify())
    title = title.strip()
    print(title)
    if title == "JEFFER PENG":
        send_mail("Test successful","check Link: " + URL)
        return True
    return False


while True:
    if checkName():
        break
    time.sleep(30)
