from flask import Flask
from flask_cors import CORS
from flask import request
import requests

app = Flask(__name__)
CORS(app)


@app.route('/api/day')
def day():
    headers = {
        'Referer': 'https://m.blog.naver.com',
    }

    blog_id = request.args.get('blog_id')

    response = requests.get(
        f'https://m.blog.naver.com/api/blogs/{blog_id}', headers=headers)

    return response.content


@app.route('/api/popular-post-list')
def popular_post_list():
    headers = {
        'Referer': 'https://m.blog.naver.com',
    }

    blog_id = request.args.get('blog_id')

    response = requests.get(
        f'https://m.blog.naver.com/api/blogs/{blog_id}/popular-post-list', headers=headers)

    return response.content


@app.route('/api/keyword-list')
def keyword_list():

    headers = {
        'Referer': 'https:/m.blog.naver.com',
    }

    blog_id = request.args.get('blog_id')
    log_no = request.args.get('log_no')

    keyword = requests.get(
        f'https://m.blog.naver.com/{blog_id}/{log_no}', headers=headers)

    split_keyword = ''.join(keyword.text)

    trim_keyword = split_keyword.replace(' ', '').split()

    found_keyword = ''

    for word in trim_keyword:
        if 'vargsTagName="' in word:
            found_keyword = word

    replace_found_keyword = found_keyword.replace(
        'vargsTagName="', '').replace('"', '').replace(';', '')

    split_replace_keyword = replace_found_keyword.split(',')

    result = []

    for text in split_replace_keyword:
        result.append('#'+text)

    res = ','.join(result)

    replace_res = res.replace(',', ' ')

    return replace_res
