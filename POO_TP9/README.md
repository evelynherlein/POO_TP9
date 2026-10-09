# SmartTicket - esqueleto (TP 9)

## Levantar el proyecto
```
python -m venv venv
venv\Scripts\activate        # Windows  (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Swagger: http://127.0.0.1:8000/docs
Se crea el archivo `smartticket.db` (SQLite) al primer arranque.

## Estructura
- `app/database.py`: engine, sesión y `get_db`
- `app/models.py`: Lugar, Sector, Evento, PrecioSector, Entrada, Cliente, Venta
- `app/routers/`: controladores vacíos (cotizar, iniciar-pago, webhook-pagos, escanear-acceso)
