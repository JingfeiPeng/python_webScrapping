import requests
from bs4 import BeautifulSoup
import re
import time
from informMyself import send_mail

URL = 'https://www.facebook.com/groups/110354088989367/'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}


existingSublets = {"set"}

def checkSubletGroup():
    page = requests.get(URL, headers=headers)
    #soup = BeautifulSoup(page.content, 'html.parser')
    soup = BeautifulSoup(page.text.replace('<--', '').replace('-->', ''), 'html.parser')
    #posts = soup.find_all("div", {"class_" : "userContentWrapper"})
    #posts = soup.find_all("div", {"class_": "text_exposed_root"})
    posts = soup.find_all('div', 'text_exposed_root')

    #print(soup.prettify())
    for post in posts:
        findTarget = re.search(".*(Albert|lester).*", post.text)
        if findTarget:
            print(post.text)
            if post.text not in existingSublets:
                existingSublets.add(post.text)
                send_mail("Found sublet", post.text)
                # stops running when found


while True:
    checkSubletGroup()
    # check every hour
    time.sleep(60*60)
