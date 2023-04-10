from typing import Optional

from fastapi import (
    Request,
    Header,
    Body,
    APIRouter,
    HTTPException,
    Response,
    Depends,
    status,
)
from fastapi.responses import HTMLResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.base import BaseHTTPMiddleware


from src.model.repository.reserves_repository import ReserveRepository
from src.model.entities.reserve import Reserve
from src.schemas.reserve import ReserveBase, ReserveUpdate, ReserveInDBBase

router = APIRouter(prefix="/reserve")
db_reserve = ReserveRepository()

@router.post("", status_code=201, tags=[''])
def create_hardware(data: ReserveBase = Body(), res: Response = None):
    try:
        db_reserve.insert(
            data.hardware_id,
            data.name_teacher,
            data.loan_date, 
            data.return_date,
            data.comments
        )
        return True
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=error)        

@router.get("", response_model=ReserveInDBBase, status_code=200, tags=[''])
def read_user(id: int):
    try:
        if id:
            result: ReserveInDBBase = db_reserve.select_by(Reserve.id, id)
            if result is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")    
            return result
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="expected query ID parameter")    
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'error')

@router.put("", response_model=ReserveInDBBase, status_code=200, tags=[''])
def update_user(data: ReserveUpdate = Body(), res: Response = None):
    try:
        db_reserve.update(
            data.id,
            data.hardware_id,
            data.name_teacher,
            data.loan_date, 
            data.return_date,
            data.comments
        )
        return db_reserve.select_by(Reserve.id, data.id)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

@router.delete("", status_code=204, tags=[''])
def delete_user(id: int, res: Response = 204):
    try:
        if id:
            db_reserve.delete_by(Reserve.id, id)
            return
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="expected query ID parameters")
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)