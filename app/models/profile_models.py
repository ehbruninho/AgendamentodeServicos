from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from .base_models import Base,create_session


session = create_session()

class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    catProf = Column(Enum('admin','user','profissional'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, name, email, phone,catProf, user_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.catProf = catProf
        self.user_id = user_id

    def listProfile():
        profiles = session.query(Profile).all()
        print("Perfis cadastrados:")
        print("")
        for profile in profiles:
            print(f"ID: {profile.id} - Nome: {profile.name}")
            print("")

    def createProfile(id):
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
    
        try:
            profile = Profile(name=name,email=email,phone=phone,catProf=catProf,user_id=id)
            session.add(profile)
            session.commit()
            print("Perfil cadastrado com sucesso!")
            return 
        except:
            print("Erro ao cadastrar perfil!")
            return False
