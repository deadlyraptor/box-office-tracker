from flask import Flask, render_template, redirect, request, flash, session
import db

app = Flask(__name__)

app.database = '/database/box_office_tracker.db'
app.secret_key = 'kdm'

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
    sql = '''INSERT INTO distributors VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)'''
    params = [request.form['name'], request.form['payee'],
              request.form['address'], request.form['city'],
              request.form['state'], request.form['zip'],
              request.form['attn']]
    db.save(sql, params)
    flash('The distributor has been added.')
    return render_template('index.html')


@app.route('/film', methods=['POST'])
def addFilm():
    sql = '''INSERT INTO films VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    params = [request.form['title'], request.form['distributor'],
              request.form['start'], request.form['end'],
              request.form['percentage'], request.form['guarantee'], 0.0, 0.0,
              0.0, 0.0, None, None, None, None, False, False]
    db.save(sql, params)
    flash('The film was successfully added.')
    return render_template('index.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
