import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    with urlopen("https://hatenablog.com/ranking") as res:
        html = res.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.select(".ranking-entry-list")
    shuffle(titles)
    titles = titles[0]
    print(titles)
    return json.dumps({
        "content" : titles.find("h3").string,
        # "link" : item.find("link").string
        "link": titles.get('rdf:about')
    })

if __name__ == "__main__":
    app.run(debug=True, port=5004)
