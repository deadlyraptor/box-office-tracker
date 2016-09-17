from flask import Flask, render_template, redirect, request, flash, session
import db
import settings
from distributor import Distributor
from film import Film

app = Flask(__name__)

app.database = settings.database
app.secret_key = settings.key


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/distributor')
def distributor():
    return render_template('distributor.html')


@app.route('/film')
def film():
    return render_template('film.html')


@app.route('/distributor', methods=['POST'])
def addDis():
    var = Distributor(request.form['name'], request.form['payee'],
                      request.form['address'], request.form['city'],
                      request.form['state'], request.form['zip'],
                      request.form['attn'])
    sql = '''INSERT INTO distributors VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)'''
    params = [var.name, var.payee, var.address, var.city, var.state, var.zip,
              var.attn]
    db.save(sql, params)
    flash('The distributor was successfully added.')
    return render_template('index.html')


@app.route('/film', methods=['POST'])
def addFilm():
    var = Film(request.form['title'], request.form['distributor'],
               request.form['start'], request.form['end'],
               request.form['percentage'], request.form['guarantee'])
    sql = ('''INSERT INTO films VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
          ?, ?, ?, ?, ?)''')
    params = [var.title, var.distributor, var.start_date, var.end_date,
              var.percentage, var.guarantee, 0.0, 0.0, 0.0, 0.0, None, None,
              None, None, False, False]
    db.save(sql, params)
    flash('The film was successfully added.')
    return render_template('index.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
