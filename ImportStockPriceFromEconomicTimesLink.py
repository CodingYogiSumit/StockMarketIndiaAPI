import requests

#the required first parameter of the 'get' method is the 'url':
http = requests.get('https://economictimes.indiatimes.com/dlf-ltd/stocks/companyid-12393.cms')
# http = requests.get('https://economictimes.indiatimes.com/lupin-ltd/stocks/companyid-10743.cms')
x=http.text
# print the response text (the content of the requested file):
# print(type(x))



# The count() method returns the number of times a specified value appears in the string.
y=x.count('data-ltp=')
# print(y)

# The find() method finds the first occurrence of the specified value.
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
# print(z)
price = float(x[y+10:z])
print(price)
# print(type(price))
# print(x[y])
# print(http.content)
# print(http.status_code)
# print(http.headers['content-type'])
# print(http.json)