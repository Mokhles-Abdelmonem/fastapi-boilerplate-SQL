from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI()
    from app.users.router import users_router
    app.include_router(users_router)

    @app.get("/")
    async def root():
        return {"message": "Hello from fastapi boilerplate ! go to (/docs) to get the documentation"}

    return app
