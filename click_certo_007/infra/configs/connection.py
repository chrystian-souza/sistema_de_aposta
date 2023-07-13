from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from click_certo_007.infra.configs.base import Base


class DBConnectionHandler:
    def __init__(self):
        self.database_name = 'click_certo_007'
        self.__connection_string = 'mysql+pymysql://root:Senac2021@localhost:3306/notas'
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
