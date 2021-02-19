import requests
from bs4 import  BeautifulSoup
import smtplib
import time
URL = 'https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_3?dchild=1&keywords=sony+a7riii&qid=1613716408&sr=8-3'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"}



def check_price():


    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converterd_price = price[0:10]
    converterd_price = converterd_price.replace('₹', '')

    converterd_price = converterd_price.replace(',', '')

    Price = float(converterd_price)
    if(Price < 165000):
        send_mail()
    print(Price)
    print(title.strip())

    if(Price>165000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('adi.kumar652@gmail.com','nnfqrkjheqgyovqb')

    subject = 'Price fell down!!'

    body = 'Check the amazon link https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_3?dchild=1&keywords=sony+a7riii&qid=1613716408&sr=8-3'

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(

        'aditya.kumar652@gmail.comm',
        'adityakumar09@outlook.com',
        msg
    )

    print("HEY EMAIL HAS BEEN SENT!!")

    server.quit()


check_price()

# To run the script automatically after a fixed interval like in this case i have specified 60*60 seconds inside sleep method.
# while(True):
#     check_price()
#     time.sleep(60*60)

























