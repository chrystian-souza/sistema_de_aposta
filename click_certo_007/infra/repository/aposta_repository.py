from click_certo_007.infra.configs.connection import DBConnectionHandler
from click_certo_007.infra.entities.aposta import Aposta



class Aposta_repository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Aposta).all()
            return data

    def select(self, vencedor):
        with DBConnectionHandler() as db:
            data = db.session.query(Aposta).filter(Aposta.vencedor == 'C').all()
            return data


    def insert(self, aposta):
        with DBConnectionHandler() as db:
            try:
                db.session.add(aposta)
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e

