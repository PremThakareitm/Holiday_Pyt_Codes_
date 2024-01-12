import requests
api_key = "65a84ed61a806ba4e196b8be0ef37f89"

url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}"

city=str(input("Enter city to search: "))

dict_para={'q':city, 'api':api_key}
response=requests.get(url=url, params=dict_para)

data=response.json()

# print(data)
f=(data['list'][0]['main']['temp'])
print("Temperature:",f-273.5)
