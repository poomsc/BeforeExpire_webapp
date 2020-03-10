from flask import Flask
from flask import render_template,redirect,url_for
from datetime import datetime,timedelta
from flask import request

app = Flask(__name__)

items = { }

@app.route('/')
def index():  
    time = str(datetime.now())[0:10].split('-')
    time = time[2] + '-' + time[1] + '-' + time[0]
    return  render_template('test.html',
                            time=time,
                            items=items.values())

@app.route('/news/<id>/')
def show_item(id):
    new_item = items[int(id)]
    return render_template('new_item.html',
                            id=new_item['id'],
                            title=new_item['title'],
                            body=new_item['body'])

def new_items(title,body):
    new_id = len(items.keys()) + 1
    return {
            'id' : new_id,
            'title' : title,
            'body' : body
    }

@app.route('/news/create/',methods=['POST'])
def create_new_item():
    item = new_items(request.form['title'],
                    request.form['body'])
    items[item['id']] = item
    return redirect(url_for('index'))
