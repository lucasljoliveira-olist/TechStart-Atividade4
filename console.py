from MarketPlaces import Marketplace
from Categories import Category, SubCategory
from main import *

def list_marketplace_categories(marketplace : Marketplace):
    marketplaces = get_marketplaces_txt()
    for m in marketplaces:
        if m.get_name() == marketplace.get_name():
            for c in m.get_categories():
                print(' - ' + c.get_name())
            break

def list_categories(categories : list):
    for c in categories:
        print(' - ' + c.get_name())


def list_marketplace(marketplaces : list):
    for c in marketplaces:
        print(' - ' + c.get_name())

def list_subcategories(category : Category, subcategories: list):
    for c in subcategories:
        if c.get_parent() == category.get_name():
            print(' - ' + c.get_name())

while (True):
    opcao = input("    1. Listar Marketplaces\n    2. Listar Categorias de um marketplace \n    3. Listar Subcategorias de uma categoria\n    4. \n    0. Sair\nInsira uma opção: ")

    if opcao == '1':
        list_marketplace(get_marketplaces_txt())
    elif opcao == '2':
        list_marketplace(get_marketplaces_txt())
        opcao = input("Insira o nome do Marketplace: ")
        for m in get_marketplaces_txt():
            if m.get_name() == opcao:
                list_marketplace_categories(m)
                break
    elif opcao == '3':
        list_categories(get_categories_txt())
        opcao = input("Insira o nome de uma Categoria: ")
        for m in get_categories_txt():
            if m.get_name() == opcao:
                list_subcategories(m, get_subcategories_txt())
                break
    elif opcao == '4':
        pass#print(f"Total multiplicação: {multiplicacao(v1, v2)}")
    elif opcao == '0':
        print('Saindo!!')
        break
    else:
        print("Opção inválida, tente novamente.")
