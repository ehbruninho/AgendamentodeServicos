from models.indications_models import Indication
from .user_controller import User
from .service_controllers import Service
from datetime import datetime
from .categories_controller import list_category
from models.categories_models import Category


def add_indication(id_user):
    print("")
    print("Cadastrar indicação")
    print("")
    description = input("Descrição: ")
    Service.list_service(id_user)

    service_id = int(input("Id do serviço: "))
    user = User.list_user()

    for users in user:
        print(f"ID: {users.id} Nome: {users.username}")
        print("")

    user_dest = int(input("ID Prestador de Serviço: "))
    categories = Category.list_categories()
    
    for category in categories:
        print(f"ID: {category.id} Categoria: {category.name}")
        print("")

    cat_id = int(input("Id da categoria: "))
    date_att = datetime.now().date()
    indication = Indication.add_indication(description,service_id,id_user,user_dest,cat_id,date_att)
    return indication

def get_indications(id_user):
    indications = Indication.notific_indications(id_user)
    if indications:
        print("Você possui novas indicações")
        for indication in indications:
            print(f"Inidicador: {indication.username}")
            print("")
            
    else:
        print("Sem indicações")
        print("")


    return indications

def att_visulization(id_user):
    indications = Indication.search_indication(id_user)
    for indication in indications:
        print(f"Indicação: {indication.description}")
        print(f"Data: {indication.date}")
        print("")
        Indication.att_visualized(id_user)
    return indications