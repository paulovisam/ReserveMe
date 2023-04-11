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


from src.model.repository.hardwares_repository import HardwareRepository
from src.model.entities.hardware import Hardware
from src.schemas.hardware import HardwareBase, HardwareUpdate, HardwareInDBBase

router = APIRouter(prefix="/hardware")
db_hardware = HardwareRepository()


@router.post("", response_model=HardwareInDBBase, status_code=201, tags=[''])
def create_hardware(data: HardwareBase = Body(), res: Response = None):
    try:
        return db_hardware.insert(
            data.name, 
            data.description,
            data.amount,
            data.status
        )
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=error)        

@router.get("", response_model=Optional[HardwareInDBBase | list], status_code=200, tags=[''])
def read_user(id: int = None):
    try:
        if id:
            result: HardwareInDBBase = db_hardware.select_by(Hardware.id, id)
            if not result:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")    
            return result
        else:
            result = db_hardware.select_all()
            return result
    except HTTPException as httperror:
        raise httperror
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error)

@router.put("", response_model=HardwareInDBBase, status_code=200, tags=[''])
def update_user(data: HardwareUpdate = Body(), res: Response = None):
    try:
        db_hardware.update(
            data.id,
            data.name, 
            data.description,
            data.amount,
            data.status
        )
        return db_hardware.select_by(Hardware.id, data.id)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

@router.delete("", status_code=204, tags=[''])
def delete_user(id: int = None, res: Response = 204):
    try:
        if id:
            db_hardware.delete_by(Hardware.id, id)
            return
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="expected query ID parameters")
    except HTTPException as httperror:
        raise httperror
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)