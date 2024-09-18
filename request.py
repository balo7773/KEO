import requests

response_2 = requests.get("https://financialmodelingprep.com/api/v3/fmp/articles?page=5&size=15&apikey=l0PIZQxrsDN5gjx2CvDaIwShIlCf9UwL")

if response_2.status_code == 200:
    post_data = response_2.json()
    
    article = post_data.get('content', [])
    print(article[0]['content'])

def api_req():
    
    return