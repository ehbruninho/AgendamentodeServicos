from controllers.service_controllers import create_service, list_service_per_user
from controllers.profile_controllers import delete_profile, list_profile


import os

def menu_user(id_user):
    op = ""
    print("Bem vindo Usuário")
    while op != 3:
        print("1 - Adicionar Perfil")
        print("2 - Adicionar Indicação")
        print("3 - Agendar Serviço")
        print("4 - Deletar Perfil")
        print("5 - Listar Perfil")
        print("6 - Sair")
        op = input("Digite a opção desejada: " )
        os.system('clear')
        if op == '1':
            list_service_per_user(id_user)
        if op == '2':
            from controllers.indication_controller import add_indication
            add_indication(id_user)
        if op == '3':
            from controllers.service_controllers import add_request_service
            add_request_service(id_user)
        if op == '4':
            delete_profile(id_user)
        if op == '5':
            list_profile(id_user)
        if op == '6':
            break
        else:
            print("Opção inválida, digite 'sair' para finalizar o programa ou 'continuar' para continuar")
            op = input()
    return