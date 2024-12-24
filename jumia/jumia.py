import requests
import bs4
from bs4 import BeautifulSoup
import csv

preference = input('What product would you want to get info about ?..\n')
preference = preference.lower()

url = f'https://www.jumia.co.ke/catalog/?q={preference}'
response = requests.get(url)
code = response.status_code
print(f'Processing...\nSearching for: {preference}')
if code == 200:
    print(f'{preference} found')
else:
    print(f'{preference} Not found')

soup = BeautifulSoup(response.content, 'html.parser')
products = soup.find_all('div', {'class': 'info'})
   
data = []
#Global variables
name = 'None'
textReview = 'None given'
price = 'None'

for product in products:
    name = product.find('h3',{'class':'name'}).text.strip()
    review = product.find('div',{'class':'rev'})
    if review:  
        textReview = review.text.strip()
    price = product.find('div',{'class':'prc'}).text.strip()
    
    data.append([name,price,textReview])

with open(f'{preference}.csv','w',newline='') as file:
    apply = csv.writer(file)
    apply.writerow(['Product Name','Price','Review'])
    apply.writerows(data)

print(f'Success {preference} saved')


