from models.service_models import Service
from models.categories_models import Category
from models.requestService_models import RequestService
import os

service = Service

def create_service(user_id):

    name = input("Digite o nome do serviço: ")
    description = input("Digite a descrição do serviço: ")
    price = input("Digite o preço do serviço: R$")
    
    print ("Categoria de Serviço:")

    categories = Category.list_categories()
    for category in categories:
        print(f"ID: {category.id} Categoria: {category.name}")
        print("")

    cat_id = input("Digite o id da categoria: ")

    service.create_service(user_id, name, description, price, cat_id)
    
    return 

def list_service_per_user(id):
    service = Service.list_service_per_user(id)
    if service == []:
        print("Nenhum serviço cadastrado para esse usuario.")
        return False
    else:
        for services in service:
                print(f"Nome: {services.name}")
                print(f"Descrição: {services.description}")
                print(f"Preço: R${services.price}")
                print("")
    return 

def list_service_per_categories(cat_id):
    service = Service.list_service_per_category(cat_id)
    if service == []:
        print("Nenhum serviço cadastrado para essa categoria.")
        return False
    else:
        for services in service:
                print(f"Nome: {services.name}")
                print(f"Descrição: {services.description}")
                print(f"Preço: R${services.price}")
                print("")
    return

def add_request_service(user_id):

    print("")
    date = input("Digite data para o serviço (aaaa/mm/dd): ")
    print("")
    hour = input("Digite o horário para o serviço (hh:mm): ")
    print("")
    print("Selecione a categoria de serviço:")
    
    categories = Category.list_categories()
    
    for category in categories:
        print(f"ID: {category.id} Categoria: {category.name}")
        print("")

    cat_id = input("Digite o ID da categoria desejada: ")
    print("")
    print("Lista de serviços disponíveis na categoria:")

    service = Service.list_service_per_category(cat_id)

    for services in service:
        print(f"ID: {services.id} Nome: {services.name}")
        print("")

    service_id = input("Digite o ID do serviço desejado: ")
    
    users_dest = Service.list_service_per_id(service_id)
    for user in users_dest:
        print(f"ID: {user.id} Profissional: {user.username}")
       
        print("")

    user_dest = input("Digite o ID do usuário destinatário: ")
    RequestService.create_request_service(date,hour, service_id, user_id,user_dest)
    print("")
    return True

def list_request_service_users(user_id):
    request_service = RequestService.list_request_service_per_user(user_id)
    if request_service == []:
        print("Nenhuma solicitação de serviço em aberto para esse usuário.")
        return False
    else:
        for request in request_service:
            print(f"ID:  {request.id}")
            print(f"Solicitante: {request.username}")
            print(f"Data: {request.date}")
            print(f"Serviço: {request.name}")
            print(f"Status: {request.status}")
            print("")
    return

def update_request_service_status(user_id):
    print("")
    print("Lista de solicitações de serviço:")
    request = list_request_service_users(user_id)
    if request:
        request_id = input("Digite o ID da solicitação de serviço: ")
        status = input("Digite o status da solicitação de serviço (Aceito/Recusado): ")
        request_service = RequestService.update_request_service_status(user_id,request_id,status)
    else:
        print("")
        return False
    
def list_all_services():
    services = Service.list_service()
    for service in services:
        print(f"ID: {service.id} Nome: {service.name}")
        print(f"Descrição: {service.description}")
        print(f"Preço: R${service.price}")
        print("")
    return

def list_all_request_service():
    request_service = RequestService.list_all_request_service()
    if request_service == []:
        print("Nenhuma solicitação de serviço cadastrada.")
        return False
    else:
        for request in request_service:
            print(f"ID: {request.id}")
            print(f"Data: {request.date}")
            print(f"Horário: {request.hour}")
            print(f"Status: {request.status}")
            print("")
    return