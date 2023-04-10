from sqlalchemy import Column, Integer, String, Enum
from ..config.base import Base
from sqlalchemy.orm import relationship



class Hardware(Base):
    __tablename__ = 'hardwares'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=True)
    amount = Column(Integer, nullable=False)
    status = Column(Enum('disponivel', 'ocupado', 'manutenção', name='status_equipamento'), nullable=False)

    reserve = relationship('Reserve', back_populates='hardware', lazy='joined')
    def __repr__(self) -> str:
        return f"(id={self.id}, name={self.name}, description={self.description}, amount={self.amount}, status={self.status})"

