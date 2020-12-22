from MarketPlaces import Marketplace
from Categories import Category, SubCategory


categories_list = [Category(1, 'Veículos'), 
                Category(2, 'Tecnologia'), 
                Category(3, 'Casa e Eletrodomésticos'),
                Category(4, 'Esporte e Lazer'), 
                Category(5, 'Brinquedos'), 
                Category(6, 'Imóveis'), 
                Category(7, 'Beleza e Cuidados Pessoais')]

subcategories_list = [SubCategory(1, 'Celulares', categories_list[1]), 
                    SubCategory(2, 'Cameras', categories_list[1]), 
                    SubCategory(3, 'Games', categories_list[1]), 
                    SubCategory(4, 'Utilidades Domésticas', categories_list[2]), 
                    SubCategory(5, 'Jardins e Exteriores', categories_list[2])]

marketplace_list = [Marketplace(1, 'Americanas', categories_list), 
                    Marketplace(2, 'Submarino', categories_list), 
                    Marketplace(3, 'Shoptime', categories_list), 
                    Marketplace(4, 'Casas Bahia', categories_list), 
                    Marketplace(5, 'Ponto Frio', categories_list), 
                    Marketplace(6, 'Shopee', categories_list), 
                    Marketplace(7, 'Magazine Luiza', categories_list)]


def list_marketplace_categories(marketplace : Marketplace):
    h1 = '<h1> Categorias do marketplaceMarketplaces </h1>'
    ol = '<ul>'
    for c in marketplace.get_categories():
        print(str(c.get_id()) + ' - ' + c.get_name())
        ol += f'<li><a href = "/listcategory">{c.get_name()}</a></li> </ br>'
    ol += '<ul>'
    return h1 + ol

def list_categories(categories : list):
    h1 = '<h1> Categorias </h1>'
    ol = '<ul>'
    for c in categories:
        print(str(c.get_id()) + ' - ' + c.get_name())
        ol += f'<li><a href = "/listsubcategory">{c.get_name()}</a></li> </ br>'
    ol += '<ul>'
    return h1 + ol

def list_marketplace(marketplaces : list):
    h1 = '<h1> Marketplaces </h1>'
    ol = '<ul>'
    for c in marketplaces:
        print(str(c.get_id()) + ' - ' + c.get_name())
        ol += f'<li><a href = "/listcategory/{{category.get_name()}}">{c.get_name()}</a></li> </ br>'
    ol += '<ul>'
    return h1 + ol

def list_subcategories(category : Category, subcategories: list):
    h1 = '<h1> Subcategorias </h1>'
    ol = '<ul>'
    for c in subcategories:
        if c.get_parent_name() == category.get_name():
            print(str(c.get_id()) + ' - ' + c.get_name())
            ol += f'<li><a href = "/listcategory">{c.get_name()}</a></li> </ br>'
    
    ol += '<ul>'
    return h1 + ol

def get_marketplaces() -> list:
    return marketplace_list

def get_subcategories() -> list:
    return subcategories_list

def get_categories() -> list:
    return categories_list
