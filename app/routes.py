from flask import render_template, redirect, url_for, flash
from app import db
from app.models import Product

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    # Lógica para adicionar produtos
    pass
