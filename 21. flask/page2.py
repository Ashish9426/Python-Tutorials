from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return '<h1 style="color: red">welcome to my web server</h1>'


@app.route('/product', methods=['GET'])
def get_products():
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='personsdb')
    query = 'select id, title, description, price from product'
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    products = []
    for (id, title, description, price) in result:
        product = {
            "id": id,
            "title": title,
            "description": description,
            "price": price
        }
        products.append(product)

    connection.close()
    return jsonify(products)


app.run(host='0.0.0.0', port=4000, debug=True)
