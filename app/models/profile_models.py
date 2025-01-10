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

    def create_profile_db(id, name,email,phone,catProf):
        try:
            profile = Profile(name=name,email=email,phone=phone,catProf=catProf,user_id=id)
            session.add(profile)
            session.commit()
            return True 
        except Exception as e:
            print(f"Erro ao cadastrar perfil! Erro {e}")	
            return False
  