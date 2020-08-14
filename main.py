import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"

querystring = {"symbol":"AMD"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "2f135f7b00mshbe98d68dab3e754p134048jsn3cd062fbb583"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)