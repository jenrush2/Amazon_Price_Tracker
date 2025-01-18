import requests
from bs4 import BeautifulSoup

#N64 wireless controller
#URL = 'https://www.amazon.com/Classic-Controller-iNNEXT-Joystick-Raspberry/dp/B07449HLKJ/ref=sr_1_4?crid=CAHYDXC65I9Z&dib=eyJ2IjoiMSJ9.mDmQSVgL958XecN7ElCvceFDkESTycrhVaTrZ0TyUC72Y5WxOT93bIbPOzqc9BkIFKesvfP8QdiCEuTId3GjA5EPFP791X_KU0i38PS7Hym63cF9ivfgXWVawC65_CmgMe7rbNRfZFt09uTC8W827Ub5HpIYnwtyIZXSqBcbF8AvQrwBhX4Jo0zoRnR70wPfYZvoaTgTpKLqKmq-EU_lJDplhnBKomSQf7reMK3SgaE.oxQaXTA9y7agnanmR9CF6pLQdLni5irkovj_x_IFI-M&dib_tag=se&keywords=retro%2Bgaming%2Bcontroller%2Busb%2Bwireless%2BN64&qid=1737242984&sprefix=retro%2Bgaming%2Bcontroller%2Busb%2Bwireless%2Bn64%2Caps%2C102&sr=8-4&th=1'

#bluetooth headphones
URL = 'https://www.amazon.com/Mini-Bone-Conduction-Open-Ear-Bluetooth-Headphones/dp/B0CYFQ34J1/ref=sr_1_3?crid=29M3OX82GPGPN&dib=eyJ2IjoiMSJ9.C5InMx7IB7wBW7zWzMU_27GxeHYtI-c-S9nLOKz_mZym37Kc9R2NT08MpCA_gWFXloxhr6rnGEXdBssya7VRXT2Z1qiNv_MMbUka-gDJDRyWJ41sf5T0gjzIhOZocW2gVPGdKxSvHnYQU0wcKynXKpb4KZyGcPu-7iL8XVLnENQsrlQXfpb9dFfxxmmudlctoRNI6xj_dDL9vFazNQosGE5CXlXNEFwc0ptZDvOOxI0.5YTdqmdo4e1Y2oJMO8w9TxYzCwCDnCM8UejclkTyM1g&dib_tag=se&keywords=shokz%2Bbone%2Bconduction%2Bheadphones&qid=1737241303&sprefix=shokz%2Caps%2C115&sr=8-3&th=1'



headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36', 'Accept-Language': 'en-US,en;q=0.5'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

title = soup.find(id="productTitle").get_text(strip=True)

print(title)

price = soup.find('span', {'class': 'a-price-whole'}).get_text(strip=True)
converted_price = float(price[0:3])

print(converted_price)