from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from click_certo_007.infra.configs.base import Base


# class DBConnectionHandler:
#     def __init__(self):
#         self.__connection_string = 'mysql+pymysql://root:Senac2021@localhost:3306/click'
#         self.__engine = self.__create_database_engine()
#         self.session = None
#         self.__create_database()
#
#     def __create_database(self):
#         engine = create_engine(self.__connection_string, echo=True)
#         try:
#             engine.connect()
#         except Exception as e:
#             if '1049' in str(e):
#                 engine = create_engine(self.__connection_string.rsplit('/', 1)[0], echo=True)
#                 conn = engine.connect()
#                 statement = text(f"CREATE DATABASE IF NOT EXISTS {(self.__connection_string.rsplit('/', 1)[1])}")
#                 conn.execute(statement)
#                 conn.close()
#                 print('Banco Criado!')
#                 self.__create_table()
#             else:
#                 raise e
#
#
#     def __create_table(self):
#         engine = create_engine(self.__connection_string, echo=True)
#         Base.metadata.create_all(bind=engine)
#         print("Tabela criada com sucesso!")
#
#     def __create_database_engine(self):
#         engine = create_engine(self.__connection_string)
#         return engine
#
#     def get_engine(self):
#         return self.__engine
#
#     # Funções mágicas que definem qualquer comportamento ao serem geradas instâncias
#     def __enter__(self):
#         session_make = sessionmaker(bind=self.__engine)
#         print('Gerando Conexão ...')
#         self.session = session_make()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Fechando Conexão ...')
#         self.session.close()

class DBConnectionHandler:
    def __init__(self):
        self.database_name = 'click_certo'
        self.__connection_string = f'sqlite:///{self.database_name}?mode=memory&cache=shared'
        self.__engine = self.__create_database_engine()
        self.session = self.__create_session()
        self.__create_tables()
        self.session.close()

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def __create_session(self):
        Session = sessionmaker(bind=self.__engine)
        session = Session()
        return session

    def __create_tables(self):
        Base.metadata.create_all(bind=self.__engine)

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


