from models.profile_models import Profile

profile = Profile

def add_profile(x):
        name = input("Digite o nome do perfil: ")
        email = input("Digite o email do perfil: ")
        phone = input("Digite o telefone do perfil: ")
        catProf = input("Digite o tipo do perfil: \n 1 - admin \n 2 - user \n 3 - profissional \n")
        if catProf == '1':
            catProf = 'admin'
        if catProf == '2':
            catProf = 'user'
        if catProf == '3':
            catProf = 'profissional'
        
        Profile.create_profile_db(x,name,email,phone,catProf)
        return True

def list_profile():
    profile.listProfile()
    return

def delete_profile(id)  :
    dp = Profile.delete_profile_db(id)
    if dp:
        return True
    return False            
    return