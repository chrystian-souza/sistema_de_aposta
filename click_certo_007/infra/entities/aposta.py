from click_certo_007.infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Aposta(Base):
    __tablename__ = 'aposta'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome_do_apostador = Column(String(length=100), nullable=False)
    time_casa = Column(String(length=100), nullable=False)
    time_visistante = Column(String(length=100), nullable=False)
    placar_casa = Column(Integer, nullable=False)
    placar_visitante = Column(Integer, nullable=False)
    resultado = Column(Integer, nullable=False)



