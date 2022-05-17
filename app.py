

import psycopg2
from flask import Flask,render_template,request,url_for,redirect

app=Flask(__name__)

def get_db_connection():
    conn=psycopg2.connect(host='localhost',
    database='flask_db',
    user="bibek",
    password="broke")
    return conn
@app.route('/')
def index():
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute('select*from pl;')
    pl=cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html',pl=pl)

@app.route('/fetch/', methods=['GET'])
def fetch():
    data=request.get('fetch.html')
    return data
        
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        id= int(request.form['id'])
        name = request.form['name']
        planguage =request.form['planguage']
        info= request.form['info']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO pl(id,name,planguage,info)'
                    'VALUES (%s, %s, %s, %s)',
                    (id, name,planguage,info))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')


