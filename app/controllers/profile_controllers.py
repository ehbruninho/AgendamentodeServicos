from models.profile_models import Profile

profile = Profile

def add_profile(x):
        name = input("Digite o nome do perfil: ")
        email = input("Digite o email do perfil: ")
        phone = input("Digite o telefone do perfil: ")
        catProf = input("Digite o tipo do perfil: \n 1 - Administrador \n 2 - Usuario \n 3 - Prestador de Serviço \n")
        if catProf == '1':
            catProf = 'admin'
        if catProf == '2':
            catProf = 'user'
        if catProf == '3':
            catProf = 'profissional'
        
        Profile.create_profile_db(x,name,email,phone,catProf)
        return True

def list_profile(id_user):
    list_profiles = Profile.list_profile(id_user)
    for profile in list_profiles:
            print(f"Nome: {profile.name} - Catergoria: {profile.catProf}")
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