import requests
import random
from user_agent import generate_user_agent
import time
import webbrowser
ruks1 =("0123456789")
ruks2 =("42",'43','44','45','46','47','48','51','52','53','54','55')
R = '\033[1;37m'
SS = '\033[1;36m'
ruks_ = '\033[1;36m'
jruks = '\033[1;33m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'
	
print (SS+' _   _    _____   _____    _____   _____  ')
print(R+'| | / /  | ____| |  _  \  /  _  \ /  _  \ ')
print(SS+ '| |/ /   | |__   | |_| |  | | | | | | | | ')
print(jruks+'| |\ \   |  __|  |  _  /  | | | | | | | | ')
print(_ruks+'| | \ \  | |___  | | \ \  | |_| | | |_| | ')
print(R+ '|_|  \_\ |_____| |_|  \_\ \_____/ \_____/ ')

print ('='*60)
TOKEN = '2066612331:AAGXFapP9IUN8tRERDT8UMHw2qn839-7ojE'
ID = '2021068735'
def data(k,bin):
		
	name = k.json()["country"]["name"]
	emoji = k.json()["country"]["emoji"]
	scheme = k.json()["scheme"]
	type = k.json()["type"]
	brand = k.json()["brand"] 
	bank_name = k.json()["bank"]["name"]
	
		
	txt_ruks=f""" 𝐁𝐈𝐍 𝐊𝐄𝐑𝐎𝐎
━━━━━ • ஜ • ❈ • ஜ • ━━━━━
BIN : {bin}
CONTROL: {name} {emoji}
TYPE: {type}
━━━━━ • ஜ • ❈ • ஜ • ━━━━━
 """	
	T =(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text='+txt_ruks)
		
	RE = requests.post(T)
	
def extract_bin_ruks3():
	Z=0
		
	while True:
		Z+=1
		time.sleep(1)
		A = str("".join(random.choice(ruks1)for i in range(4)))
		B = str("".join(random.choice(ruks2)for i in range(1)))
			
		headers ={'appCodeName': 'Mozilla',
	 'appName': 'Netscape',
	 'appVersion': generate_user_agent(),
	 'buildID': None,
	 'oscpu': 'Intel Mac OS X 10_8_1',
	 'platform': 'Macintosh; Intel Mac OS X 10_8_1',
	 'product': 'Gecko',
	 'productSub': '20030107',
	 'userAgent': generate_user_agent(),
	 'vendor': 'Google Inc.',
	 'vendorSub': ''}			
		bin =(f"{B}{A}")
		k = requests.get(f"https://lookup.binlist.net/"+bin,headers=headers)
		if "<title>429 Too Many Requests</title>" in k:			
			time.sleep(1.50)		
		try:
			 	
			country = k.json()["country"]["currency"]
			emoji = k.json()["country"]["emoji"]
			print(jruks+'['+_ruks+str(Z)+jruks+']'+jruks+" bin"+BGreen+' work'+R+' | '+bin+R+" | "+emoji+BGreen)
			 	
			if country == "RUB":
				data(k,bin)
			elif country == "IQ":
				data(k,bin)
			
			
		except:
				
			print(jruks+'['+_ruks+str(Z)+jruks+']'+jruks+' bin'+_ruks+' not work'+R+' | '+bin+R+" | "+"False"+BGreen) 
			pass
extract_bin_ruks3()
 	
