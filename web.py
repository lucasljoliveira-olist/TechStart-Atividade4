from flask import Flask
from MarketPlaces import Marketplace
from Categories import Category, SubCategory

category_list = [Category(1, 'Veículos'), 
                Category(2, 'Tecnologia'), 
                Category(3, 'Casa e Eletrodomésticos'),
                Category(4, 'Esporte e Lazer'), 
                Category(5, 'Brinquedos'), 
                Category(6, 'Imóveis'), 
                Category(7, 'Beleza e Cuidados Pessoais')]

subcategory_list = [SubCategory(1, 'Celulares', category_list[1]), 
                    SubCategory(2, 'Cameras', category_list[1]), 
                    SubCategory(3, 'Games', category_list[1]), 
                    SubCategory(4, 'Utilidades Domésticas', category_list[2]), 
                    SubCategory(5, 'Jardins e Exteriores', category_list[2])]

marketplace_list = [Marketplace(1, 'Americanas', category_list), 
                    Marketplace(2, 'Submarino', category_list), 
                    Marketplace(3, 'Shoptime', category_list), 
                    Marketplace(4, 'Casas Bahia', category_list), 
                    Marketplace(5, 'Ponto Frio', category_list), 
                    Marketplace(6, 'Shopee', category_list), 
                    Marketplace(7, 'Magazine Luiza', category_list)]



if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/marketplacecategory/<marketplace>')
    def list_marketplace_category(marketplace) -> None:
        ol = '<ul>'
        h1 = '<h1> Categorias </h1>'
        for m in marketplace_list:
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
        for c in marketplace_list:
            ol += "<li><a href = '/marketplacecategory/" + str(c.get_id()) + "'>" + c.get_name()+ "</a></li> </br>"
        ol += '<ul>'
        return h1 + ol

    @app.route('/listsubcategory/<category>')
    def list_subcategory(category) -> None:
        ol = '<ul>'
        h1 = '<h1> Subcategorias </h1>'
        for sc in subcategory_list:
            if sc.get_parent().get_id() == int(category):
                ol += "<li>" + sc.get_name()+ "</li> </br>"
        ol += '<ul>'
        voltar = '<a href="/">Voltar!</a>'
        return h1 + ol + voltar

    app.run(debug = True)
