from sqlalchemy import Column, Integer, String
from .base_models import Base,create_session
from .profile_models import Profile

session = create_session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def createUser(name,password):
        try:
            usuario = User(username=name,password=password)
            session.add(usuario)
            session.commit()

        except Exception as e:
                print(f"Erro ao cadastrar usuário: {e}!")
                return 
        
    def checkUser(name):
        user = session.query(User).filter(User.username == name).first()
        if user:
            return True
        return False
           
    def listUser():
        # Bruno - 07/01 - Comando select * from users
        return session.query(User).all()

    def loginUser(name,password):
        try:
            user = session.query(User).filter(User.username == name).filter(User.password == password).all()
            if user:
                return True
            return False
        except Exception as e:
            print(f"Erro ao logar usuário! {e}")
            return 
        
    def getUserId(name):
        user = session.query(User).filter(User.username == name).filter(User.id).first()
        return user.id
    
    def check_profile_User(id):
        # Bruno - 07/01 - Tive que fazer um join para pegar o catProf
        user = (session.query(Profile).join(User, Profile.user_id == User.id).filter(User.id == id).first())
        if user:
            return user.catProf
        return False
    
    def deleteUser(id):
        try:
            user = session.query(User).filter(User.id == id).first()
            session.delete(user)
            session.commit()
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}!")
            return