from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["HU2 - Pago y emisión"])


@router.post("/iniciar-pago", summary="Iniciar pago de una cotización (HU2)")
def iniciar_pago():
    # TODO: delegar en PagoService
    raise HTTPException(status_code=501, detail="Pendiente de implementar")


@router.post("/webhook-pagos", summary="Webhook de la pasarela de pagos (HU2)")
def webhook_pagos():
    # TODO: delegar en PagoService
    raise HTTPException(status_code=501, detail="Pendiente de implementar")
