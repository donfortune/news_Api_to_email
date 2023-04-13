import requests
from send_mail import send_email
topic = 'tesla'
api_key = 'caaad31c3aae4af7a92c2df85bfa5d78'
url = "https://newsapi.org/v2/everything?" \
      "q=tesla&" \
      "from=2023-03-13&" \
      "sortBy=publishedAt&" \
      "apiKey=caaad31c3aae4af7a92c2df85bfa5d78&language=en"

response = requests.get(url)
content = response.json()

body = ''

for article in content['articles'][:20]:
    if article["description"] is not None:
        body = "subject: Today's News" + '\n' + body + article['title'] + '\n' + article['description'] + '\n' + article['url'] + 2*'\n'
body = body.encode('utf-8')
send_email(message=body)
