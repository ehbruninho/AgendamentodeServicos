
from controllers.user_controller import list_usuario
from controllers.profile_controllers import list_all_profi
from controllers.service_controllers import list_all_services
from controllers.service_controllers import list_all_services


def menu_admin(id_user):
    op = 0
    while op != 5:
        print("Seja bem vindo Administrador")
        print("1 - Listar Usuarios")
        print("2 - Listar Profissionais")
        print("3 - Listar Serviços")
        print("4 - Listar Solicitações de Serviços")
        print("5 - Sair")
        print("")

        op = input("Digite a opção desejada: ")
   
        if op == '1':
            list_usuario()
        if op == '2':
            list_all_profi()
        if op == '3':
            list_all_services()
        if op == '4':
            list_all_services()
        if op == '5':
            break
    return

