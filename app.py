from flask import Flask, redirect, request, render_template, flash
import sys
from flask_sqlalchemy import SQLAlchemy
from weather_api_requests import fetch_weather, is_city_real

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, db.Identity(start=0, cycle=True), primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), unique=True, nullable=False)

    def __repr__(self):
        return f'<City name is {self.name}>'


@app.route('/', methods=['GET', 'POST'])
def index():
    cities = City.query.all()
    list_of_cities = [(item.name, item.id) for item in cities]
    list_of_weathers = [fetch_weather(city, city_id) for city, city_id in list_of_cities]
    return render_template('index.html', weathers=list_of_weathers)


@app.route(f'/delete/<city_id>', methods=['GET', 'POST'])
def delete(city_id):
    city = City.query.filter_by(id=city_id).first()
    db.session.delete(city)
    db.session.commit()
    return redirect('/')


@app.route('/add', methods=['POST'])
def choose_city():
    city = request.form['city_name']
    if not (is_city_real(city)) or city == 'The city that doesn\'t exist!':
        flash('The city doesn\'t exist!')
        return redirect('/')
    'The city doesn\'t exist!'
    db_cities = City.query.all()
    list_of_cities = set([item.name for item in db_cities])
    if city in list_of_cities:
        flash("The city has already been added to the list!")
    else:
        new_city = City(name=city)
        db.session.add(new_city)
        db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    db.create_all()
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
