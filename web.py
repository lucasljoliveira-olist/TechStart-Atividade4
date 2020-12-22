from flask import Flask
from MarketPlaces import Marketplace
from Categories import Category, SubCategory
from main import *



if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/marketplacecategory/<marketplace>')
    def list_marketplace_category(marketplace) -> None:
        ol = '<ul>'
        h1 = '<h1> Categorias </h1>'
        for m in get_marketplaces():
            if m.get_id() == int(marketplace):
                for c in m.get_categories():
                    ol += "<li><a href = '/listsubcategory/" + str(c.get_id()) + "'>" + c.get_name()+ "</a></li> </br>"

        ol += '<ul>'
        voltar = '<a href="/">Voltar!</a>'
        return h1 + ol + voltar

    @app.route('/')
    def index() -> None:
        h1 = '<h1> Marketplaces </h1>'
        ol = '<ul>'
        for c in get_marketplaces():
            ol += "<li><a href = '/marketplacecategory/" + str(c.get_id()) + "'>" + c.get_name()+ "</a></li> </br>"
        ol += '<ul>'
        return h1 + ol

    @app.route('/listsubcategory/<category>')
    def list_subcategory(category) -> None:
        ol = '<ul>'
        h1 = '<h1> Subcategorias </h1>'
        for sc in get_subcategories():
            if sc.get_parent().get_id() == int(category):
                ol += "<li>" + sc.get_name()+ "</li> </br>"
        ol += '<ul>'
        voltar = '<a href="/">Voltar!</a>'
        return h1 + ol + voltar

    app.run(debug = True)
