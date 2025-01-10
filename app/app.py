from models import Base, get_engine, create_session, User
from controllers import user_controller, profile_controllers
from menus import menu_professional
from controllers.profile_controllers import add_profile
from controllers.user_controller import login_usuario, add_usuario, list_usuario, check_profile
from menus.menu_professional import menu_profissional
from menus.menu_users import menu_user
import os

def inicial_program():
    op = 0
    while op != 3:
        print("1 - Entrar")
        print("2 - Cadastrar")
        print("3 - Sair")
        print("")

        op = input("Digite a opção desejada: " )


        if (op == '1'):
            
            id_user = login_usuario()
            if not id_user:
                print("Usuário ou senha incorretos! Tente novamente")
                print("")
            else:
                sp = check_profile(id_user) # Verifica se o usuário é profissional ou usuário - Finalizado
                if not sp:
                    print("Usuario sem perfil, cadastre seu perfil!")
                    profile = add_profile(id_user)
                    if profile:
                        print("Perfil cadastrado com sucesso!")
                    continue
                if sp == "profissional":
                    menu_profissional(id_user)
                if sp == "user":
                    menu_user(id_user)
                
        if op == '2':
                opt = add_usuario()
                os.system('clear')
                if opt:
                    print("Usuário cadastrado com sucesso!")
                else:
                    print("Ja existe um cadastro com esse nome! Tente novamente")
                print("")
        
        if op == '3':
            break
        
if __name__ == '__main__':
    inicial_program()

    