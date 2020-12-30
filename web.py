from flask import Flask, render_template, request
from MarketPlaces import Marketplace
from Categories import Category, SubCategory
from main import *



if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    
    @app.route('/addmarketplace')
    def add_marketplace():
        titulo = 'marketplace'
        return render_template('add_things.html', add = set_marketplace_txt(request.args.get('new_marketplace')), tittle = titulo, arg = request.args.get('new_marketplace'))

    @app.route('/addcategory')
    def add_category():
        titulo = 'category'
        print(request.args.get('marketplace'))
        return render_template('add_things.html', add = set_category_txt(request.args.get('marketplace'), request.args.get('new_category')), tittle = titulo, arg = request.args.get('new_category'))

    @app.route('/addsubcategory')
    def add_subcategory():
        titulo = 'subcategory'
        return render_template('add_things.html', add = set_subcategory_txt(request.args.get('category'), request.args.get('new_subcategory')), tittle = titulo, arg = request.args.get('new_subcategory'))

    @app.route('/category/<marketplace>')
    def list_marketplace_category(marketplace : str):
        titulo = 'Categorias ' + marketplace
        return render_template('categories.html', categories = get_categories_txt(), tittle = titulo, marketplace = marketplace)

    @app.route('/')
    def index():
        titulo = 'Marketplaces'
        return render_template('marketplaces.html', marketplaces = get_marketplaces_txt(), tittle = titulo)

    @app.route('/listsubcategory/<category>')
    def list_subcategory(category : str):
        titulo = 'Subcategorias'
        return render_template('subcategories.html', subcategories = get_subcategories_txt(), tittle = titulo, category = category)

    app.run(debug = True)
