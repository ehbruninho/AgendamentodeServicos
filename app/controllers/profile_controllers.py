from models.profile_models import Profile
from models.categories_models import Category

profile = Profile

def add_profile(id_user):
        name = input("Digite o nome do perfil: ")
        email = input("Digite o email do perfil: ")
        phone = input("Digite o telefone do perfil: ")
        catUser = input("Digite o tipo do Usuario: \n 1 - Administrador \n 2 - Usuario \n 3 - Prestador de Serviço \n")
        if catUser == '1':
            catUser = 'admin'
            Profile.create_profile_db(id_user,name,email,phone,catUser,0)
        if catUser == '2':
            catUser = 'user'
            Profile.create_profile_db(id_user,name,email,phone,catUser,0)
        if catUser == '3':
            categories = Category.list_categories()
            for category in categories:
                print(f"{category.id} - {category.name}")
            catService = input("Digite o id da categoria: ")
            catUser = 'profissional'
            Profile.create_profile_db(id_user,name,email,phone,catUser,catService)
        
        return True

def list_profile(id_user):
    list_profiles = Profile.list_profile(id_user)
    for profile in list_profiles:
            print(f"Nome: {profile.name} - Catergoria: {profile.catUser}")
            print("")
    return

def delete_profile(id)  :
    resp = input("Deseja realmente deletar o perfil? (s/n)")
    if resp == 'n':
        return False
    
    dp = Profile.delete_profile_db(id)
    if dp:
        return True
    return False            