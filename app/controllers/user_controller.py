from models.users_models import User 
user = User

def add_usuario():
    name = input("Digite o nome do usuário: ")
    password = input("Digite a senha do usuário: ")
    user = User.check_user(name)
    if user:
        return False
    User.create_user(name, password)
    return True

def list_usuario():
    print("Lista de usuários cadastrados:")
    users = User.list_user()
    for user in users:
        print(f"ID: {user.id} Nome: {user.username}")
        print("")
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



     