import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

import random

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    html = 'https://b.hatena.ne.jp/hotentry/all'
    with urlopen(html) as res:
        html = res.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.select('.entrylist-contents-title a')
    article = random.choice(articles)

    return json.dumps({
        "content" : article.text,
        "link" : article['href']
    })

@app.route("/api/xxxx")
def api_xxxx():
    """
    こっちはこれからやります
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
    pass

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5004)
