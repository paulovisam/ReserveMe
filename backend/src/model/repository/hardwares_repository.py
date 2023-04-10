from ..config.connection import DBConnectionHandler
from ..entities.hardware import Hardware
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import joinedload
from datetime import date, datetime
from typing import Optional

class HardwareRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Hardware).all()
                return data
            except NoResultFound:
                return None
            except Exception as error:
                db.session.rollback()
                raise error
    def select_by(self, field, value: any):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Hardware).filter(field == value).first()
                return data
            except NoResultFound:
                return None
            except Exception as error:
                db.session.rollback()
                raise error

    def insert(
            self,
            name,
            description,
            amount,
            status
    ) -> None:
        with DBConnectionHandler() as db:
            try:
                data_insert = Hardware(
                    name=name,
                    description=description,
                    amount=amount,
                    status = status
                )
                db.session.add(data_insert)
                db.session.commit()
                # return data_insert
            except NoResultFound:
                return None
            except Exception as error:
                db.session.rollback()
                raise error

    def update(
        self,
        where_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        amount: Optional[int] = None,
        status: Optional[str] = None
    ) -> None:
        with DBConnectionHandler() as db:
            try:
                hardware = (
                    db.session.query(Hardware)
                    .filter(Hardware.id == where_id)
                    .first()
                )
                name = (
                    name if name is not None else hardware.name
                )
                description = (
                    description if description is not None else hardware.description
                )
                amount = (
                    amount if amount is not None else hardware.amount
                )
                status = (
                    status if status is not None else hardware.status
                )

                db.session.query(Hardware).filter(Hardware.id == where_id).update(
                    {
                        "name": name,
                        "description": description,
                        "amount": amount,
                        "status":status
                    }
                )
                db.session.commit()
            except NoResultFound:
                return None
            except Exception as error:
                db.session.rollback()
                raise error

    def delete_by(self, field, value: str) -> None:
        with DBConnectionHandler() as db:
            try:
                db.session.query(Hardware).filter(
                    field == value
                ).delete()
                db.session.commit()
            except NoResultFound:
                return None
            except Exception as error:
                db.session.rollback()
                raise error