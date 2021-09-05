import requests
link='https://www.moneycontrol.com/india/stockpricequote/infrastructure-general/jaiprakashassociates/JA02'
#the required first parameter of the 'get' method is the 'url':
http = requests.get(link)
# http = requests.get('https://economictimes.indiatimes.com/lupin-ltd/stocks/companyid-10743.cms')
x=http.text
# print the response text (the content of the requested file):
# print(type(x))



# The count() method returns the number of times a specified value appears in the string.
y=x.count('nprevclose')
# print(y)

# The find() method finds the first occurrence of the specified value.
y = x.find('nprevclose')+33

# print(y)
# print(x[y+32])
# print(x[z])
z=y
counter=0
while(1):
    if(x[z]=='"'):
        break
    z=z+1
# print(x[y])
# print(x[z-1])
price = float(x[y:z])
print(price)