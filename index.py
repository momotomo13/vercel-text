from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def get_body_content():
    if request.method == 'POST':
        url = request.form['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        body_content = soup.body.get_text()
        return f"<pre>{body_content}</pre>"
    return '''
        <form method="post">
            <input type="text" name="url" placeholder="URLを入力してください">
            <input type="submit" value="送信">
        </form>
    '''