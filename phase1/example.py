import requests
from bs4 import BeautifulSoup

res = requests.get('http://api.carmd.com/v3.0/decode?vin=1GNALDEK9FZ108495', 
headers={
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-US,en;q=0.8',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    'Partner-Token': '9e67ff29a1524bbdb27654d74300519c', 
    'Authorization': 'Basic OWU1NTMzNGYtZjVjYS00MzQ1LTkzM2YtNDcyNDNlNDgzODdl'})

if res:
    print('Response OK')
else:
    print('Response Failed')

print(res.json())
#soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())
#output = open('index.html', 'w')
#output.write(res.text)
#output.close()
