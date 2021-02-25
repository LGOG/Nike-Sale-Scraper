import requests
from bs4 import BeautifulSoup
URL = "https://www.nike.com/w/mens-sale-shoes-3yaepznik1zy7ok" 
res = requests.get(URL)

soup = BeautifulSoup(res.text, 'lxml')
hi = soup.select('title')

print (hi[0].getText())

print ('\n')

Items = soup.select('.product-card__body') 

#Name
for Item in Items:
	name = (Item.div.img["alt"])
	
#Price Old
x = Item.select(".product-card__info")
price_x = (str(x))
old_prices =  (price_x.split(">$"))
x_price = (old_prices[1].split("<"))
old_price = x_price[0]

#New Price
new_prices =  (price_x.split(">$"))


y_price = (new_prices[2].split('<'))
new_price = y_price[0]


print ("Name: " + name)
print ("The old price was: $" + old_price)
print ("the new price is : $" + new_price)
x = round(float(old_price))
y = round(float(new_price)) 
z = (y - x ) * 100
print ("You saved {}%!".format( z//y)  )
print ("\n")
