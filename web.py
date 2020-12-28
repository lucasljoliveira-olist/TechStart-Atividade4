from flask import Flask, render_template
from MarketPlaces import Marketplace
from Categories import Category, SubCategory
from main import *



if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/category/<marketplace>')
    def list_marketplace_category(marketplace) -> None:
        titulo = 'Categorias'
        return render_template('categories.html', categories = get_categories_txt(), tittle = titulo, marketplace = marketplace)

    @app.route('/')
    def index() -> None:
        titulo = 'Marketplaces'
        return render_template('marketplaces.html', marketplaces = get_marketplaces_txt(), tittle = titulo)

    @app.route('/listsubcategory/<category>')
    def list_subcategory(category) -> None:
        titulo = 'Subcategorias'
        return render_template('subcategories.html', subcategories = get_subcategories_txt(), tittle = titulo, category = category)

    app.run(debug = True)
