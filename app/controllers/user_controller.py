from models.users_models import User 
from werkzeug.security import generate_password_hash, check_password_hash

user = User

def add_usuario():
    name = input("Digite o nome do usuário: ")
    password = input("Digite a senha do usuário: ")
    user = User.check_user(name)
    if user:
        return False
    
    password = generate_password_hash(password)
    User.create_user(name, password)
    return True

def list_usuario():
    print("Lista de usuários cadastrados:")
    users = User.list_user()
    
    for user in users:
        print(f"ID: {user.id} Nome: {user.username}")
        print("")


    op =''
    while op != 2:
        print(" Deseja editar algum usuario?")
        print("1 - Sim 2 - Sair")
        print("")
        op = input("Digite a opção desejada: ")
            
        if op == '1':
            update_user_name()
            
        if op == '2':
            break
    return

def update_user_name():
    id_user = input("Digite o ID do usuário que deseja editar: ")
    print ("Digite o campo que deseja editar")
    print ("1 - Nome ")
    op  = input("Digite a opção desejada: ")
                
    if op == '1':
        name = input("Digite o novo nome:")
        user.update_username(id_user,name)
    return

def login_usuario():
    name = input("Login: ")
    password = input("Senha: ")   
    user = User.login_user(name, password)    
    if not user:
        return False
    else:
        id = User.get_user_id(name)
        return id

def check_profile(id):
    profile = User.check_profile_User(id)
    return profile



     