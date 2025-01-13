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

    def createService(id):
        name = input("Digite o nome do serviço: ")
        description = input("Digite a descrição do serviço: ")
        price = input("Digite o preço do serviço: R$")
        try:
            service = Service(name=name,description=description,price=price,user_id=id,cat_id=1)
            session.add(service)
            session.commit()
            print("Serviço cadastrado com sucesso!")
            return service
        except:
            print("Erro ao cadastrar serviço!")
            return False
        

    def listService(id):
        services = session.query(Service).filter(Service.user_id == id).all()
        print("Serviços cadastrados:")
        for service in services:
            print(f"Nome: {service.name}")
            print(f"Descrição: {service.description}")
            print(f"Preço: R${service.price}")
            print("")