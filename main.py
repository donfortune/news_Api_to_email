import requests
api_key = 'caaad31c3aae4af7a92c2df85bfa5d78'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-03-12&sortBy=publishedAt&apiKey=caaad31c3aae4af7a92c2df85bfa5d78'

request = requests.get(url)
content = request.json()

for article in content['articles']:
    print(article['title'])

