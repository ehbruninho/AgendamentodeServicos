from controllers.service_controllers import create_service, list_service
from controllers.service_controllers import create_service, list_service
import os

def menu_user():
    op = ""
    print("Bem vindo Usuário")
    while op != 3:
        print("1 - Adicionar Perfil")
        print("2 - Consultar Agenda disponivel")
        print("3 - Agendar Serviço")
        print("4 - Sair")
        op = input("Digite a opção desejada: " )
        os.system('clear')
        if op == '1':
            list_service()
        if op == '2':
            continue
        if op == '4':
            return
        else:
            print("Opção inválida, digite 'sair' para finalizar o programa ou 'continuar' para continuar")
            op = input()
    return