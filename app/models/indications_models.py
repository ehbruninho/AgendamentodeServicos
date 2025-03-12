from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, Boolean
from .base_models import Base,create_session
from sqlalchemy.orm import relationship

session = create_session()


class Indication(Base):
    
    __tablename__ = 'indications'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(100), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'))
    user_orig = Column(Integer, ForeignKey('users.id'))
    user_dest = Column(Integer, ForeignKey('users.id'))
    cat_id = Column(Integer, ForeignKey('categories.id'))
    visualized = Column(Boolean, default=False)
    date = Column(Date, nullable=False)
    
    def __init__(self,description, service_id, user_orig, user_dest, cat_id, date):
        self.description = description
        self.service_id = service_id
        self.user_orig = user_orig
        self.user_dest = user_dest
        self.cat_id = cat_id
        self.date = date

    user_origin = relationship("User", foreign_keys=[user_orig])
    user_destination = relationship("User", foreign_keys=[user_dest])

    def add_indication(description,service_id,user_orig, user_dest,cat_id, date):
        try:
            indication = Indication(description=description,service_id=service_id,user_orig=user_orig,user_dest=user_dest,cat_id=cat_id,date=date)
            session.add(indication)
            session.commit()
            print("Indicação cadastrada com sucesso!")
            return indication
        except Exception as e:
            print(f"Erro ao cadastrar indicação! Erro: {e}")
            return False
    
    def notific_indications(id_user):
        from .users_models import User
        try:
            indications = session.query(User.username).join(Indication, User.id == Indication.user_orig).filter(Indication.visualized == False).all()
            return indications
        except Exception as e:
            print(f"Erro ao buscar indicações! Erro: {e}")
            return False
        
    def att_visualized(id_user):
        try:
            indication = session.query(Indication).filter(Indication.user_dest == id_user).update({Indication.visualized:True})
            session.commit()
            return indication
        except Exception as e:
            print(f"Erro ao atualizar indicação! Erro: {e}")
            return False
   
    def search_indication(id_user):
        try:
            indications = session.query(Indication).filter(Indication.user_dest == id_user).all()
            return indications
        except Exception as e:
            print(f"Erro ao buscar indicações! Erro: {e}")
            return False