from sqlalchemy import Column, Integer, String
from .base_models import Base,create_session
from sqlalchemy.orm import relationship

session = create_session()

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __init__(self,name):
        self.name = name

    def create_category(name):
        try:
            category = Category(name=name)
            session.add(category)
            session.commit()
            print("Categoria cadastrada com sucesso!")
            return category
        except:
            print("Erro ao cadastrar categoria!")
            return False
        
    def list_categories():
        return session.query(Category).all()