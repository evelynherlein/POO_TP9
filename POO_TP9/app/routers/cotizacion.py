from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/cotizar", tags=["HU1 - Cotización"])


@router.post("", summary="Cotizar entradas (HU1)")
def cotizar():
    # TODO: delegar en CotizacionService
    raise HTTPException(status_code=501, detail="Pendiente de implementar")
