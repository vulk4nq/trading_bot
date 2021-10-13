import requests
import time
coin1= 'btc'
coin2= 'usd'

#print(responce.json())
"""{"btc_usd":{"asks":[[56854.51818155,0.00014801],[56855.88323462,0.00058352],[56908.13540135,0.0001642],[56992.3721239,0.0001443],[57013.3186662,0.00016126],[57025.59496644,0.00010022],[57079.37352191,0.00010022],[57199.89,0.00255729],[57200,0.00719197],[57249.06,0.00011417]],"bids":[[56678,0.00021582],[56677.17005,0.01209451],[56677,0.00532846],[56671.44714812,0.00011022],[56661.35022773,0.80139633],[56619.75964393,0.01606248],[56619.75963393,0.01567132],[56619.75962393,0.01622867],[56555.29,0.00255729],[56555.18,0.01628781]]}}
"""
test = 1000
i = -1
total_bids_s = []
prices = []
while True:
    respons = requests.get(url=f'https://yobit.net/api/3/depth/{coin1}_{coin2}?limit=100000')
    respons_pr = requests.get(url=f'https://yobit.net/api/3/ticker/{coin1}_{coin2}')
    if respons.status_code == 200 and respons_pr.status_code == 200:
        rsp_json = respons.json()
        price_last = respons_pr.json()[f'{coin1}_{coin2}']['last']
        asks = rsp_json[f'{coin1}_{coin2}']['asks']
        bids = rsp_json[f'{coin1}_{coin2}']['bids']
        total_asks =0
        total_bids =0
        for item in asks:
             total_asks += item[0] * item[1]
        for item in bids:
             total_bids += item[0] * item[1]
        i += 1
        total_bids_s.append(total_bids)
        prices.append(price_last)
        print(f'[INFO] -- Total asks: {round(total_asks,10)} {coin2}')
        print(f'[INFO] -- Total bids: {round(total_bids,10)} {coin2}')
        print(f'[INFO] -- Last price = {price_last} {coin2}')
        if i>0:
            print(f'[INFO]--- Total bids last % increase/decrease = {total_bids_s[i]/total_bids_s[i-1]}')
            print(f'[INFO]--- Last prices % increase/decrease = {prices[i] / prices[i - 1]}')
            print(f'[INFO]--- Last prices % increase/decrease from first = {prices[i] / prices[0]}')
            print(f'{i/2} minute/n/n/n')
        time.sleep(1)





