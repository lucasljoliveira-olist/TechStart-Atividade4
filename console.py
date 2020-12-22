from MarketPlaces import Marketplace
from Categories import Category, SubCategory
from main import *

while (True):
    opcao = input("    1. Listar Marketplaces\n    2. Listar Categorias de um marketplace \n    3. Listar Subcategorias de uma categoria\n    4. \n    0. Sair\nInsira uma opção: ")

    if opcao == '1':
        list_marketplace(get_marketplaces())
    elif opcao == '2':
        list_marketplace(get_marketplaces())
        opcao = input("Insira um ID Marketplace: ")
        for m in get_marketplaces():
            if m.get_id() == int(opcao):
                list_marketplace_categories(m)
                break
    elif opcao == '3':
        list_categories(get_categories())
        opcao = input("Insira um ID Marketplace: ")
        for m in get_categories():
            if m.get_id() == int(opcao):
                list_subcategories(m, get_subcategories())
                break
    elif opcao == '4':
        pass#print(f"Total multiplicação: {multiplicacao(v1, v2)}")
    elif opcao == '0':
        print('Saindo!!')
        break
    else:
        print("Opção inválida, tente novamente.")
