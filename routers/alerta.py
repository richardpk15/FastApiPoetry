import os
from typing import Annotated

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Alerta(BaseModel):
    event: str
    resource: str | None = None
    severity: str
    notes: str | None = None


@router.post("/alerta/", tags=["alerta"])
async def criar_alerta(
        alerta: Alerta, token: Annotated[str, Header()]) -> Alerta:
    if token != os.environ.get("token,"):
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    else:
        return alerta
