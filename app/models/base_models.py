from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Declarative base para os modelos
Base = declarative_base()

# Função para obter o engine
def get_engine():
  
    return create_engine('sqlite:///banco.db')

# Função para criar sessões
def create_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
