from click_certo_007.infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Apostador(Base):
    __tablename__ = 'apostador'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(20), nullable=False)

