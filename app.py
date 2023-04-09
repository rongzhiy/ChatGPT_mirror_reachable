from flask import Flask, render_template
import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


app = Flask(__name__)

def read_url():
    # 读取available的csv文件并显示所有内容，并复制给result
    urls = []
    with open('./data/available.csv', 'r') as f:
        for line in f.readlines():
            # print(line.strip().split(','))
            urls.append(line.strip().split(','))
    return urls

@app.route('/')
def index():
    results = []
    urls = read_url()
    for url in urls:
        results.append(url)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run()
