from sqlalchemy import Column, Integer, String, ForeignKey, Float, ForeignKey
from .base_models import Base,create_session
from sqlalchemy.orm import relationship

session = create_session()

class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    cat_id = Column(Integer, ForeignKey('categories.id'))

    def __init__(self, name, description, price, user_id, cat_id):
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id
        self.cat_id = cat_id

    def create_service(id, name, description, price, cat_id):
        try:
            service = Service(name=name,description=description,price=price,user_id=id,cat_id=cat_id)
            session.add(service)
            session.commit()
            print("Serviço cadastrado com sucesso!")
            return service
        except:
            print("Erro ao cadastrar serviço!")
            return False
        

    def list_service():
        return session.query(Service).all()
       
    def list_service_per_category(id_category):
        return session.query(Service).filter(Service.cat_id == id_category).all()
    
    def list_service_per_user(id):
        return session.query(Service).filter(Service.user_id == id)
    
    def list_service_per_id(id):
        from .users_models import User
        return session.query(User.username, User.id).join(Service, User.id == Service.user_id).filter(Service.id == id).all()
    