import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Mini-Bone-Conduction-Open-Ear-Bluetooth-Headphones/dp/B0CYFQ34J1/ref=sr_1_3?crid=29M3OX82GPGPN&dib=eyJ2IjoiMSJ9.C5InMx7IB7wBW7zWzMU_27GxeHYtI-c-S9nLOKz_mZym37Kc9R2NT08MpCA_gWFXloxhr6rnGEXdBssya7VRXT2Z1qiNv_MMbUka-gDJDRyWJ41sf5T0gjzIhOZocW2gVPGdKxSvHnYQU0wcKynXKpb4KZyGcPu-7iL8XVLnENQsrlQXfpb9dFfxxmmudlctoRNI6xj_dDL9vFazNQosGE5CXlXNEFwc0ptZDvOOxI0.5YTdqmdo4e1Y2oJMO8w9TxYzCwCDnCM8UejclkTyM1g&dib_tag=se&keywords=shokz%2Bbone%2Bconduction%2Bheadphones&qid=1737241303&sprefix=shokz%2Caps%2C115&sr=8-3&th=1'

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())