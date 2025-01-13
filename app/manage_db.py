from .models import Base, get_engine, create_session, User, Profile, Service

def criar_banco():
    engine = get_engine()
    Base.metadata.create_all(engine)
    print("Banco de dados e tabelas criados com sucesso.")

if __name__ == '__main__':
    criar_banco()

    