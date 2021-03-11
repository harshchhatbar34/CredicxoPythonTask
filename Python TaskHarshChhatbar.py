import requests
from bs4 import BeautifulSoup
import pprint
saving = requests.get('https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1')
soup = BeautifulSoup(saving.content,'html.parser')
with open('htmlPage.html', 'w') as f:
    f.write(str(saving.content))

output = []
for mainContainer in soup.find_all('div',class_='product-container'):
    for blockContainer in mainContainer.find_all('div',class_="product"):
        tempDict = {}

        #for title
        for dicribtionContainer in blockContainer.find_all('div',class_='product-description'):
            for productName in dicribtionContainer.find_all('a',class_='catalog-item-name'):
                tempDict['title'] = productName.text

        #for Manufacturer
        for manufactur in blockContainer.find_all('div',class_='catalog-item-brand-item-number'):
            for brand in manufactur.find_all('a',class_='catalog-item-brand'):
                tempDict['manufacturer'] = brand.text

        #for price
        for priceContainer in blockContainer.find_all('div',class_='price-rating-container'):
            for itemPriceList in priceContainer.find_all('div',class_='catalog-item-price'):
                for productPrice in itemPriceList.find_all('span',class_='price'):
                    tempDict['price'] = float(productPrice.text[1:])

        #for In Stock Or not
                for productStatus in itemPriceList.find_all('span',class_='status'):
                    if productStatus.text == 'Out of Stock':
                        tempDict['status'] = False
                    else:
                        tempDict['status'] = True

        output.append(tempDict)
pprint.pprint(output)
