import requests
from bs4 import BeautifulSoup
import smtplib
import time
from credentials import gmailMailPassword

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
        send_mail()
        return True
    return False


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("pengjefferbms@gmail.com", gmailMailPassword)

    subject = "Test successful"
    body = "check Link: " + URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "pengjefferbms@gmail.com",
        "jf2peng@edu.uwaterloo.ca",
        msg
    )
    print("Email sent")
    server.quit()


while True:
    if checkName():
        break
    time.sleep(30)
