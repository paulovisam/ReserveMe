import uvicorn
from alembic.config import Config
from alembic.command import upgrade

from fastapi import FastAPI, status, Response, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from src.routers import router_hardware, router_reserve


#Objects/vars
prefix = '/api/v1'

app = FastAPI()

origins = [
    "http://localhost",
    "https://localhost:8080",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.add_middleware(HTTPSRedirectMiddleware)
# app.add_middleware(BaseHTTPMiddleware, dispatch=timer_res)

# Routers
prefix = '/api/v1'
app.include_router(router_hardware.router, prefix=prefix)
app.include_router(router_reserve.router, prefix=prefix)


@app.get(f'{prefix}/feature')
def test_feature(res_code: Response = None):
    res_code.status_code = status.HTTP_202_ACCEPTED
    return {'status': True}

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host='127.0.0.1', reload=True)