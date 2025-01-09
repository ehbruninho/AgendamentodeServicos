from models.profile_models import Profile

profile = Profile

def add_profile(x):
    sp = profile.createProfile(x)
    return sp

def list_profile():
    profile.listProfile()
    return

def search_profile(x):
    sp = profile.searchProfile(x)
    if sp == None:
        print("\n Sem perfil cadastrado, por favor efetue o cadastro! \n")
        mp = profile.createProfile(x)
    return sp
    