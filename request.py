import requests
from datetime import date, timedelta

current_date = date.today().isoformat()
three_days_bfor_cd = (date.today() - timedelta(days=3)).isoformat()

response_2 = requests.get("https://financialmodelingprep.com/api/v3/fmp/articles?page=5&size=15&apikey=l0PIZQxrsDN5gjx2CvDaIwShIlCf9UwL")

if response_2.status_code == 200:
    post_data = response_2.json()
    
    article = post_data.get('content', [])
    print(article[0]['content'])

def search_api(keyword):
    search_post = []
    url = f"https://newsapi.org/v2/everything?q={keyword}&from={three_days_bfor_cd}&to={current_date}&sortBy=popularity&pageSize=12&apiKey=7bce52cd1385491385d8146e1f2caaea"
    search_response = requests.get(url)
    