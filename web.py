from flask import Flask, render_template
from MarketPlaces import Marketplace
from Categories import Category, SubCategory
from main import *



if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/category/<marketplace>')
    def list_marketplace_category(marketplace) -> None:
        titulo = 'Categorias'
        return render_template('categories.html', marketplaces = get_marketplaces(), tittle = titulo, marketplace = int(marketplace))

    @app.route('/')
    def index() -> None:
        titulo = 'Marketplaces'
        return render_template('marketplaces.html', marketplaces = get_marketplaces(), tittle = titulo)

    @app.route('/listsubcategory/<category>')
    def list_subcategory(category) -> None:
        titulo = 'Subcategorias'
        return render_template('subcategories.html', subcategories = get_subcategories(), tittle = titulo, category = int(category))

    app.run(debug = True)
