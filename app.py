import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route to display cars with sorting
@app.route('/')
def index():
    sort_by = request.args.get('sort_by', 'car_model')  # Default sort by car_model
    order = request.args.get('order', 'asc')
    reverse_order = 'desc' if order == 'asc' else 'asc'

    conn = sqlite3.connect('cars.db')
    c = conn.cursor()
    query = f"SELECT * FROM cars ORDER BY {sort_by} {order}"
    c.execute(query)
    cars = c.fetchall()
    conn.close()

    return render_template('index.html', cars=cars, sort_by=sort_by, order=order, reverse_order=reverse_order)

# Route to add a new car
@app.route('/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        car_model = request.form['car_model']
        year_of_production = request.form['year_of_production']
        engine_volume = request.form['engine_volume']
        mileage = request.form['mileage']
        fuel = request.form['fuel']
        steering_wheel_location = request.form['steering_wheel_location']
        color = request.form['color']
        body_type = request.form['body_type']
        location = request.form['location']
        price_in_usd = request.form['price_in_usd']

        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        c.execute('''INSERT INTO cars (car_model, year_of_production, engine_volume, mileage, fuel, steering_wheel_location, color, body_type, location, price_in_usd)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (car_model, year_of_production, engine_volume, mileage, fuel, steering_wheel_location, color, body_type, location, price_in_usd))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('add_car.html')

# Route to delete a car
@app.route('/delete/<int:car_id>', methods=['POST'])
def delete_car(car_id):
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()
    c.execute('DELETE FROM cars WHERE rowid = ?', (car_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
