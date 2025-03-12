from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Boolean, Date
from .base_models import Base,create_session
from sqlalchemy.orm import relationship
from datetime import datetime

session = create_session()

class RequestService(Base):
        __tablename__ = 'request_service'

        id = Column(Integer, primary_key=True, autoincrement=True)
        date = Column(Date, nullable=False) 
        hour = Column(String(5), nullable=False)
        service_id = Column(Integer, ForeignKey('services.id')) 
        user_orig = Column(Integer, ForeignKey('users.id'))
        user_dest = Column(Integer, ForeignKey('users.id'))
        status = Column(Enum('Em aberto', 'Aceito', 'Recusado'), nullable=False, default='Em aberto')
        finshed = Column(Boolean, nullable=False, default=False)


        def __init__(self, date, hour, service_id, user_orig, user_dest):
            self.date = date
            self.hour = hour
            self.service_id = service_id
            self.user_orig = user_orig
            self.user_dest = user_dest


        def create_request_service(date, hour, service_id, user_orig, user_dest):
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d").date()
                hour_obj = datetime.strptime(hour, "%H:%M")
                request_service = RequestService(date_obj, hour_obj,service_id=service_id, user_orig=user_orig, user_dest=user_dest)
                session.add(request_service)
                session.commit()
                print("Solicitação de serviço cadastrada com sucesso!")
                return request_service
            except Exception as e:
                print(f"Erro ao cadastrar solicitação de serviço! Erro: {e}")
                return False

        def list_all_request_service():
            try:
                request_service = session.query(RequestService).all()
                return request_service
            except Exception as e:
                print(f"Erro ao listar solicitações de serviço! Erro: {e}")
                return False

        def list_request_service_per_user(user_id):
            from .users_models import User
            from .service_models import Service
            try:
                request_service = session.query(
                     User.username, RequestService.id,RequestService.date,Service.name, RequestService.status).join(User, User.id == RequestService.user_orig).join(Service, RequestService.service_id == Service.id).filter(RequestService.status=="Em aberto").filter(RequestService.user_dest == user_id).all()
                return request_service
            except Exception as e:
                print(f"Erro ao listar solicitações de serviço! Erro: {e}")
                return False
        
        def update_request_service_status(user_id,request_id,status):
            try:
                request_service = session.query(RequestService).filter(RequestService.id == request_id).filter(RequestService.user_dest == user_id).first()
                request_service.status = status
                session.commit()
                print("Status da solicitação de serviço atualizado com sucesso!")
                return request_service
            except Exception as e:
                print(f"Erro ao atualizar status da solicitação de serviço! Erro: {e}")
                return False