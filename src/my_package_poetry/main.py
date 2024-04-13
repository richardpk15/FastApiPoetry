import uvicorn
from fastapi import FastAPI
from routers import alerta, hello

app = FastAPI()

app.include_router(alerta.router)
app.include_router(hello.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
