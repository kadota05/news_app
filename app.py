from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://news.yahoo.co.jp/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    article_links = []
    for a in soup.find_all('a', href=True):
        if 'articles' in a['href']:
            article_links.append(a['href'])

    random_article_link = random.choice(article_links)

    return render_template('home.html', link=random_article_link)

if __name__ == "__main__":
    app.run(debug=True)
