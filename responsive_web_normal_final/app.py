from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
@app.route('/index')
def index():
    return '메인페이지'


@app.route('/sub')
def about():
  return '상세 페이지'