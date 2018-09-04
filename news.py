import newspaper
from newspaper import Article
from newspaper import fulltext
from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/article/html',methods = ['POST'])
def parse_article():
    article_url = get_article_url()
    article = download_it(article_url,False)
    return article.html

@app.route('/article/authors',methods = ['POST'])
def article_authors():
    article_url = get_article_url()
    article = download_it(article_url)
    return jsonify(article.authors)

@app.route('/article/imglink',methods = ['POST'])
def article_image():
    article_url = get_article_url()
    article = download_it(article_url)
    return jsonify(article.top_image)

@app.route('/article/text',methods = ['POST'])
def article_text():
    article_url = get_article_url()
    article = download_it(article_url)
    return jsonify(article.text)

@app.route('/article/publish_date',methods = ['POST'])
def publish_date():
    article_url = get_article_url()
    article = download_it(article_url)
    return jsonify(article.publish_date)

@app.route('/article/keywords',methods = ['POST'])
def keywords():
    article_url = get_article_url()
    article = download_it(article_url)
    return jsonify(article.keywords)

@app.route('/article/summary',methods = ['POST'])
def summary():
    article_url = get_article_url()
    article = download_it(article_url)
    return jsonify(article.summary)

@app.route('/newspaper/article_urls',methods = ['POST'])
def newspaper_build():
    post_json = request.get_json()
    newspaper_url = post_json['newspaper']
    language = post_json['language']
    if language:
        paper  = newspaper.build(newspaper_url,language=language)
    else:
        paper  = newspaper.build(newspaper_url)
    articles = []
    for article in paper.articles:
        articles.append(article)
    return jsonify(articles)

def get_article_url():
    if request.args.get('article') is None:
        post_json = request.get_json()
        return post_json['article']
    else:
        return request.args.get('article')
    
def download_it(url,parse=True):
    print(url)
    article = Article(url)
    article.download()
    if parse:
        article.parse()
    return article

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
