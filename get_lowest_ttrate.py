import urllib
import urllib.request
from bs4 import BeautifulSoup

thettrateUrl = "https://hk.ttrate.com/zh_hk/?c=JPY"
thepage = urllib.request.urlopen(thettrateUrl)

soup = BeautifulSoup(thepage, "html.parser")
price_dict = {}

print(soup.title)
#print(soup.find("a",{"class":"rate_link"}))
soup = soup.find("table", {"class":"rate_table"})
'''
for node in soup.tbody.findAll("tr"):
    for index, ahref in enumerate(node.findAll("a", {"class": "rate_link"})):
        if index == 1:
            print(ahref.text, index)
'''
for node in soup.tbody.findAll("tr"):
    for index, tds in enumerate(node.findAll("td")):
        if index == 0:# the 1st column is the bank name
            bank_name = tds.text
            #print(tds.text)
        if index == 1:# the 2nd column is the tt buying price
            pass
        if index == 2:#the 3rd column is the TT selling price
            price = tds.text.strip()
            if price == "-":
                continue
            else:
                #selling_price.append(float(price))
                price_dict[bank_name] = float(price)
                #print(price)
selling_price = list(price_dict.values())
selling_price.sort()
print("Lowest selling price is: ",selling_price[0])
print(price_dict)

