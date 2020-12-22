from MarketPlaces import Marketplace
from Categories import Category, SubCategory
from main import *

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


while (True):
    opcao = input("    1. Listar Marketplaces\n    2. Listar Categorias de um marketplace \n    3. Listar Subcategorias de uma categoria\n    4. \n    0. Sair\nInsira uma opção: ")

    if opcao == '1':
        list_marketplace(marketplace_list)
    elif opcao == '2':
        list_marketplace(marketplace_list)
        opcao = input("Insira um ID Marketplace: ")
        for m in marketplace_list:
            if m.get_id() == int(opcao):
                list_marketplace_categories(m)
                break
    elif opcao == '3':
        list_categories(category_list)
        opcao = input("Insira um ID Marketplace: ")
        for m in category_list:
            if m.get_id() == int(opcao):
                list_subcategories(m, subcategory_list)
                break
    elif opcao == '4':
        pass#print(f"Total multiplicação: {multiplicacao(v1, v2)}")
    elif opcao == '0':
        print('Saindo!!')
        break
    else:
        print("Opção inválida, tente novamente.")
