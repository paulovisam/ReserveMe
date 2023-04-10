from ..config.connection import DBConnectionHandler
from ..entities.reserve import Reserve
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import joinedload
from datetime import date, datetime
from typing import Optional

class ReserveRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Reserve).all()
                return data
            except NoResultFound:
                return None
            except Exception as error:
                db.session.rollback()
                raise error
    def select_by(self, field, value: any):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Reserve).filter(field == value).first()
                return data
            except NoResultFound:
                return None
            except Exception as error:
                db.session.rollback()
                raise error

    def insert(
            self,
            hardware_id,
            name_teacher,
            loan_date,
            return_date,
            comments
    ) -> None:
        with DBConnectionHandler() as db:
            try:
                data_insert = Reserve(
                hardware_id=hardware_id,
                name_teacher=name_teacher,
                loan_date=loan_date,
                return_date=return_date,
                comments=comments
                )
                db.session.add(data_insert)
                db.session.commit()
            except NoResultFound:
                return None
            except Exception as error:
                db.session.rollback()
                raise error

    def update(
        self,
        where_id: int,
        hardware_id: Optional[int] = None,
        name_teacher: Optional[str] = None,
        loan_date: Optional[any] = None,
        return_date: Optional[any] = None,
        comments: Optional[str] = None
    ) -> None:
        with DBConnectionHandler() as db:
            try:
                reserve = (
                    db.session.query(Reserve)
                    .filter(Reserve.id == where_id)
                    .first()
                )
                hardware_id = (
                    hardware_id if hardware_id is not None else reserve.name
                )
                name_teacher = (
                    name_teacher if name_teacher is not None else reserve.name
                )
                loan_date = (
                    loan_date if loan_date is not None else reserve.description
                )
                return_date = (
                    return_date if return_date is not None else reserve.amount
                )
                comments = (
                    comments if comments is not None else reserve.status
                )

                db.session.query(Reserve).filter(Reserve.id == where_id).update(
                    {
                        'hardware_id': hardware_id,
                        'name_teacher':name_teacher,
                        'loan_date':loan_date,
                        'return_date':return_date,
                        'comments':comments
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
                db.session.query(Reserve).filter(
                    field == value
                ).delete()
                db.session.commit()
            except NoResultFound:
                return None
            except Exception as error:
                db.session.rollback()
                raise error