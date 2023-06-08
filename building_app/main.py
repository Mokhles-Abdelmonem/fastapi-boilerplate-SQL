import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    app = FastAPI()
    from buildings.router import buildings_router
    app.include_router(buildings_router)
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
    return app




app = create_app()

if __name__ == '__main__':
    
    uvicorn.run('main:app', reload=True, port=7000)
