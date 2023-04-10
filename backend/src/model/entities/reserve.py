from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from ..config.base import Base


class Reserve(Base):
    __tablename__ = 'reserves'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hardware_id = Column(Integer, ForeignKey('hardwares.id'), nullable=False)
    name_teacher = Column(String(200), nullable=False)
    loan_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=False)
    comments = Column(String(200), nullable=True)

    hardware = relationship('Hardware', back_populates='reserve', lazy="joined")

    def __repr__(self) -> str:
        return f"(id={self.id}, hardware={self.hardware}, name_teacher={self.name_teacher}, loan_date={self.loan_date}, return_date={self.return_date}, comments={self.comments})"
