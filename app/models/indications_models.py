from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from .base_models import Base,create_session
from sqlalchemy.orm import relationship

session = create_session()

class Indication(Base):
    
    __tablename__ = 'indications'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(100), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'))
    user_orig = Column(Integer, ForeignKey('users.id'))
    cat_id = Column(Integer, ForeignKey('categories.id'))
    date = Column(Date, nullable=False)
    
    def __init__(self,description, service_id, user_orig, user_dest, cat_id, date):
        self.description = description
        self.service_id = service_id
        self.user_orig = user_orig
        self.user_dest = user_dest
        self.cat_id = cat_id
        self.date = date

    def createIndication(description,service_id,user_orig, user_dest,cat_id, date):
        try:
            indication = Indication(description=description,service_id=service_id,user_orig=user_orig,user_dest=user_dest,cat_id=cat_id,date=date)
            session.add(indication)
            session.commit()
            print("Indicação cadastrada com sucesso!")
            return indication
        except:
            print("Erro ao cadastrar indicação!")
            return False
        
   