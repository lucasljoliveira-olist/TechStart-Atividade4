from MarketPlaces import Marketplace
from Categories import Category, SubCategory
from datetime import datetime
from pathlib import Path


path_categories = '21.12.2020/Atividade 4/data/categorias.txt'
path_marketplaces = '21.12.2020/Atividade 4/data/marketplaces.txt'
path_logs = '21.12.2020/Atividade 4/data/olist_logs.txt'

def save_log(texto:str) -> None:
    fileObj = Path(path_logs)
    if fileObj.is_file():
        log_file = open(path_logs, 'a')
    else:
        log_file = open(path_logs, 'x')
    datahora = datetime.now()
    datahora = datahora.strftime('%d/%m/%Y %H:%M')
    log_file.write(f'{datahora} - {texto}\n')
    log_file.close()

def get_subcategories_txt() -> list:
    fileObj = Path(path_categories)
    if fileObj.is_file():
        subcategories_file = open(path_categories, 'r')
    else:
        subcategories_file = open(path_categories, 'x')
    subcategories = []
    for c in subcategories_file:
        aux = c.split(';')
        if aux[1].strip() != '':
            subcategories.append(SubCategory(aux[0].strip(), aux[1].strip(), ''))
    subcategories_file.close()

    save_log('get_subcategories_txt (ler subcategorias)')
    return subcategories

def get_categories_txt() -> list:
    fileObj = Path(path_categories)
    if fileObj.is_file():
        categories_file = open(path_categories, 'r')
    else:
        categories_file = open(path_categories, 'x')
    categories = []
    for c in categories_file:
        aux = c.split(';')
        if aux[1].strip() == '':
            categories.append(Category(aux[0].strip(), aux[2].strip()))
    categories_file.close()

    save_log('get_categories_txt (ler categorias)')

    return categories

def get_marketplaces_txt() -> list:
    fileObj = Path(path_marketplaces)
    if fileObj.is_file():
        marketplaces_file = open(path_marketplaces, 'r')
    else:
        marketplaces_file = open(path_marketplaces, 'x')
    marketplaces = []
    for m in marketplaces_file:
        marketplaces.append(Marketplace(m.strip(), []))
    marketplaces_file.close()

    save_log('get_marketplaces_txt (ler marketplaces)')

    return marketplaces

