import requests
from send_mail import send_email

api_key = 'caaad31c3aae4af7a92c2df85bfa5d78'
url = 'https://newsapi.org/v2/everything?q=apple&from=2023-04-12&to=2023-04-12&sortBy=popularity&apiKey=caaad31c3aae4af7a92c2df85bfa5d78'

response = requests.get(url)
content = response.json()

body = ''
for article in content['articles']:
    body = body + article['title'] + '\n' + article['description'] + 2*'\n'
body = body.encode('utf-8')
send_email(message=body)
