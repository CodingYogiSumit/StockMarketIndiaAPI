# step-1 : search the stock price from economic times
# step-2:copy the link of economicstimes which is showing you the stock price
# step-3: paste the link in the link in the fifth line with the inverted comma around
import requests
Link='https://economictimes.indiatimes.com/lupin-ltd/stocks/companyid-10743.cms'
#the required first parameter of the 'get' method is the 'url':
http = requests.get('https://economictimes.indiatimes.com/dlf-ltd/stocks/companyid-12393.cms')
# http = requests.get(Link)
x=http.text



y=x.count('data-ltp=')
# print(y)

y = x.find('data-ltp=')
# print(y)
# print(x[y])
z=y
counter=0
while(1):
    if(x[z]=='"'):
        counter=counter+1
    if(counter==2):
        break
    # print(x[y])
    z=z+1
price = float(x[y+10:z])
print(price)
