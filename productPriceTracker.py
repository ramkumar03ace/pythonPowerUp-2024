import request
from bs4 import BeautifulSoup
import time

product_url="https://www.flipkart.com/apple-2023-macbook-pro-m3-18-gb-1-tb-ssd-macos-sonoma-mrx43hn-a/p/itmea1733d7de471?pid=COMGUTX7QF7FHNKD&lid=LSTCOMGUTX7QF7FHNKDG2WQ7T&marketplace=FLIPKART&q=macbook&store=6bo%2Fb5g&srno=s_1_4&otracker=search&otracker1=search&fm=Search&iid=a96b89b8-846d-4a24-8ed5-aecae96b5c2c.COMGUTX7QF7FHNKD.SEARCH&ppt=sp&ppn=sp&ssid=3gerng12o00000001711182216158&qH=864faee128623e2f"

target_price=299000

def check_price():
    r=requests.get(product_url)
    soup=BeautifulSoup(r.content)
    price=soup.find('div',attrs={"class":"_16Jk6d"}).text
    price_without_rs=price[1:]
    without_comma=price_without_rs.replace(',','')
    int_price=int (price_without_rs)
    return int_price

cur_price=check_price()
print(f"Current Price is {cur_price}")
print("we will inform u when the price si less than the target peice")
print("waiting")
while True:
    cur_price=check_price()
    if cur_price<=target_price:
        print (f"Traget Price reached")
        break
time.sleep(60)
