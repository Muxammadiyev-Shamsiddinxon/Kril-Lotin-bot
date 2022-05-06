
import requests
from pprint import pprint as print

kod =  'bfb4ae90a65e63cc7a717986'  #API dan olgan kodim ExchangeRate-API
 
# ozbek somi kursi 

url_uzb=f"https://v6.exchangerate-api.com/v6/{kod}/pair/USD/UZS"
uzb = requests.get(url_uzb) # Saytdan qaytgan javob <requests.get> taminlayapmiz
uzb=uzb.json()
uzb=uzb['conversion_rate']
print(f"Bugungi kurs: 1 $  =  {uzb}-So'm ")

#hamma davlatlar kursi

davlat='latest'    
url=f"https://v6.exchangerate-api.com/v6/{kod}/{davlat}/USD"

javob = requests.get(url)  #Saytdan qaytgan javob <requests.get> taminlayapmiz
javob = javob.json()
for davlat,son  in javob['conversion_rates'].items():
    print(f"Bugungi kurs: 1 $  = {davlat} - {son}  ")

