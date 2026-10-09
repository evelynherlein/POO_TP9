from http.client import HTTPResponse
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/escanear-acceso", tags=["HU3 - Control de acceso"])


@router.post("", summary="Escanear QR en puerta (HU3)")
def escanear_acceso():
    # TODO: delegar en AccesoService
    raise HTTPException(status_code=501, detail="Pendiente de implementar")

@router.post("/prueba", summary="Escanear QR en puerta (HU3)")
def escanear_acceso_prueba():
    print("Escanear QR en puerta (HU3)")
    return JSONResponse(
        content={"mensaje": "Todo bien"},
        status_code=200
    )
