from flask import Flask
from flask import render_template, redirect, url_for
from datetime import datetime, timedelta
from flask import request

app = Flask(__name__)

items = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    time = str(datetime.now())[0:10].split('-')
    time = time[2] + '-' + time[1] + '-' + time[0]
    return render_template('create.html',
                           time=time,
                           items=items.values())

@app.route('/new/<id>/')
def show_item(id):
    new_item = items[int(id)]
    return render_template('new_item.html',
                           id=new_item['id'],
                           #image=new_item['image'],
                           name=new_item['name'],
                           date=new_item['date'])


def new_items(name, date):
    new_id = len(items.keys()) + 1
    return {
        'id': new_id,
        'name': name,
        'date': date
    }


@app.route('/new/create/', methods=['POST'])
def create_new_item():
    item = new_items(request.form['name'],
                     request.form['date'])
    items[item['id']] = item
    return redirect(url_for('index'))
