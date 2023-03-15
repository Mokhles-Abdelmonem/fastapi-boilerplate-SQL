from fastapi import FastAPI 
from routes.user import user_router
import uvicorn

app = FastAPI()

app.include_router(user_router)








if __name__ == '__main__':
    uvicorn.run('index:app', reload=True)
