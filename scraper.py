import requests
from bs4 import BeautifulSoup
import smtplib
import time

#bluetooth headphones -- replace the URL below with whichever one you would like.
URL = 'https://www.amazon.com/Mini-Bone-Conduction-Open-Ear-Bluetooth-Headphones/dp/B0CYFQ34J1/ref=sr_1_3?crid=29M3OX82GPGPN&dib=eyJ2IjoiMSJ9.C5InMx7IB7wBW7zWzMU_27GxeHYtI-c-S9nLOKz_mZym37Kc9R2NT08MpCA_gWFXloxhr6rnGEXdBssya7VRXT2Z1qiNv_MMbUka-gDJDRyWJ41sf5T0gjzIhOZocW2gVPGdKxSvHnYQU0wcKynXKpb4KZyGcPu-7iL8XVLnENQsrlQXfpb9dFfxxmmudlctoRNI6xj_dDL9vFazNQosGE5CXlXNEFwc0ptZDvOOxI0.5YTdqmdo4e1Y2oJMO8w9TxYzCwCDnCM8UejclkTyM1g&dib_tag=se&keywords=shokz%2Bbone%2Bconduction%2Bheadphones&qid=1737241303&sprefix=shokz%2Caps%2C115&sr=8-3&th=1'



headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36', 'Accept-Language': 'en-US,en;q=0.5'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify()) to see what's on the page.

    #inspect the website to pull the id as seen below
    title = soup.find(id="productTitle").get_text(strip=True)

    print(title)

    #inspect the website to pull the class from the website
    price = soup.find('span', {'class': 'a-price-whole'}).get_text(strip=True)
    converted_price = float(price[0:3])

    print(converted_price)

    if(converted_price < 115):
        send_mail()
    




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #set up two step verification to allow the program to use gmail on your computer
    server.login('jennifer.rush2@gmail.com', 'kqvi ykah hqkb xmso')

    subject = 'Price dropped on headphones!'
    body = 'Check the amazon link: https://www.amazon.com/Mini-Bone-Conduction-Open-Ear-Bluetooth-Headphones/dp/B0CYFQ34J1/ref=sr_1_3?crid=29M3OX82GPGPN&dib=eyJ2IjoiMSJ9.C5InMx7IB7wBW7zWzMU_27GxeHYtI-c-S9nLOKz_mZym37Kc9R2NT08MpCA_gWFXloxhr6rnGEXdBssya7VRXT2Z1qiNv_MMbUka-gDJDRyWJ41sf5T0gjzIhOZocW2gVPGdKxSvHnYQU0wcKynXKpb4KZyGcPu-7iL8XVLnENQsrlQXfpb9dFfxxmmudlctoRNI6xj_dDL9vFazNQosGE5CXlXNEFwc0ptZDvOOxI0.5YTdqmdo4e1Y2oJMO8w9TxYzCwCDnCM8UejclkTyM1g&dib_tag=se&keywords=shokz%2Bbone%2Bconduction%2Bheadphones&qid=1737241303&sprefix=shokz%2Caps%2C115&sr=8-3&th=1'

    msg = f"Subject: {subject}\n\n{body}"

    #from email is first, to email is second
    server.sendmail(
        'jennifer.rush2@gmail.com',
        'rush.jillian@yahoo.com',
        msg
    )

    print('Hey! Email has been sent!')

    server.quit()


while(True):
    check_price()
    #sends repeatedly once per day
    time.sleep(86400)