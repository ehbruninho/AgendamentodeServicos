from controllers.service_controllers import create_service, list_service
import os

def menu_profissional(id_user):
     op = ""
     print("Bem vindo Profissional")
     while op != 4:
        print("1 - Cadastrar serviço")
        print("2 - Listar serviços")
        print("3 - Alterar status do serviço")
        print("4 - Sair")
        op = input("Digite a opção desejada: " )
        os.system('clear')
        if op == '1':
            create_service(id_user)
        if op == '2':
            list_service(id_user)
        if op == '3':
            continue
        if op == '4':
            break
        else:
            print("Opção inválida, digite 'sair' para finalizar o programa ou 'continuar' para continuar")
            op = input()
     return