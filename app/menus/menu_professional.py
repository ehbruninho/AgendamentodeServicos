from controllers.service_controllers import create_service, list_service_per_user

from controllers.indication_controller import get_indications, att_visulization
import os


def menu_profissional(id_user):
     op = ""
     os.system('clear')
     print("")
     print("Bem vindo Profissional")
     get_indications(id_user)
     while op != 4:
        print("1 - Cadastrar serviço")
        print("2 - Listar serviços")
        print("3 - Visualizar indicações")
        print("4 - Verificar solicitações de serviço")
        print("5 - Sair")
        print("")
        op = input("Digite a opção desejada: " )
        os.system('clear')
        if op == '1':
            create_service(id_user)
        if op == '2':
            list_service_per_user(id_user)
        if op == '3':
            att_visulization(id_user)
            continue
        if op == '4':
            from controllers.service_controllers import list_request_service_users
            list_request_service_users(id_user)
        if op == '5':
            break
     return