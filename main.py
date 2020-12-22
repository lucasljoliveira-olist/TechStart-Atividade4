from MarketPlaces import Marketplace
from Categories import Category, SubCategory

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
