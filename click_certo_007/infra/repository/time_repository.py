from click_certo_007.infra.configs.connection import DBConnectionHandler
from click_certo_007.infra.entities.time import Time
from click_certo_007.infra.entities.apostador import Apostador
from sqlalchemy import func



class Time_repository:

    def insert(self, time):
        with DBConnectionHandler() as db:
            try:
                db.session.add(time)
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e