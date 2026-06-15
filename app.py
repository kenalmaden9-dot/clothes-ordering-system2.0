from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app=Flask(__name__)
DB="clothes.db"

def conn():
    c=sqlite3.connect(DB)
    c.row_factory=sqlite3.Row
    return c

def init_db():
    c=conn()
    c.execute("CREATE TABLE IF NOT EXISTS clothes(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,size TEXT,color TEXT,price REAL,quantity INTEGER)")
    c.commit(); c.close()

@app.route('/')
def index():
    c=conn(); items=c.execute("SELECT * FROM clothes ORDER BY id DESC").fetchall(); c.close()
    return render_template("index.html",items=items)

@app.route('/add',methods=['POST'])
def add():
    c=conn()
    c.execute("INSERT INTO clothes(name,size,color,price,quantity) VALUES (?,?,?,?,?)",(request.form['name'],request.form['size'],request.form['color'],float(request.form['price']),int(request.form['quantity'])))
    c.commit(); c.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>',methods=['GET','POST'])
def edit(item_id):
    c=conn()
    if request.method=='POST':
        c.execute("UPDATE clothes SET name=?,size=?,color=?,price=?,quantity=? WHERE id=?",(request.form['name'],request.form['size'],request.form['color'],float(request.form['price']),int(request.form['quantity']),item_id))
        c.commit(); c.close()
        return redirect(url_for('index'))
    item=c.execute("SELECT * FROM clothes WHERE id=?",(item_id,)).fetchone(); c.close()
    return render_template("edit.html",item=item)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    c=conn(); c.execute("DELETE FROM clothes WHERE id=?",(item_id,)); c.commit(); c.close()
    return redirect(url_for('index'))

if __name__=='__main__':
    init_db()
    app.run(debug=True)
