import requests
import json
from bs4 import BeautifulSoup
class yobit():

    def get_ticker(self, coin1='btc', coin2='usd'):
        responce = requests.get(url=f'https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1')
        print(f"{coin1} - {coin2} = {responce.status_code}")
        if responce.status_code == 200:
            return responce
        else: return 0
    def get_avg_price(self, coin1='btc',coin2='usd'):
        return self.get_ticker(coin1,coin2).json()[f'{coin1}_{coin2}']['avg']
    def get_last_price(self, coin1='btc',coin2='usd'):
        x = self.get_ticker(coin1, coin2)
        if x == 0:
            return 0
        else:
            return x.json()[f'{coin1}_{coin2}']['avg']
    def get_rates(self):#return : 0 - usd_rub : 1- eur_usd : 2- pound_usd
        usd_rub_url = 'https://www.google.com/search?q=usd+rub'
        eur_usd_url = 'https://www.google.com/search?q=eur+usd'
        pound_usd_url = 'https://www.google.com/search?q=pound+usd'

        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        headers = {"user-agent": USER_AGENT}
        resp1 = requests.get(usd_rub_url, headers=headers)
        resp2 = requests.get(eur_usd_url, headers=headers)
        resp3 = requests.get(pound_usd_url, headers=headers)
        soup1 = BeautifulSoup(resp1.content, "html.parser")
        soup2 = BeautifulSoup(resp2.content, "html.parser")
        soup3 = BeautifulSoup(resp3.content, "html.parser")

        return [soup1.find('span',{'class':'DFlfde SwHCTb'})['data-value'], soup2.find('span',{'class':'DFlfde SwHCTb'})['data-value'],
                soup3.find('span',{'class':'DFlfde SwHCTb'})['data-value']]



