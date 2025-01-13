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

    def listProfile(id_user):
        from .users_models import User
        profiles = session.query(Profile).join(User).filter(Profile.user_id == User.id).filter(User.id == id_user).all()
        return profiles
        

    def create_profile_db(id, name,email,phone,catProf):
        try:
            profile = Profile(name=name,email=email,phone=phone,catProf=catProf,user_id=id)
            session.add(profile)
            session.commit()
            return True 
        except Exception as e:
            print(f"Erro ao cadastrar perfil! Erro {e}")	
            return False
  
    def delete_profile_db(id):
        try:
            profile = session.query(Profile).filter(Profile.id == id).first()
            session.delete(profile)
            session.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar perfil! Erro {e}")
            return False