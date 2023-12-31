from click_certo_007.infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Aposta(Base):
    __tablename__ = 'aposta'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome_do_apostador = Column(String(length=100), nullable=False)
    gols_casa = Column(Integer, nullable=False)
    gols_visitante = Column(Integer, nullable=False)
    valor_da_aposta = Column(Integer, nullable=False)
    vencedor = Column(String(length=1))





