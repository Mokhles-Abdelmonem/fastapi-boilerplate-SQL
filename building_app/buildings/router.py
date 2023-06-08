from fastapi import Depends, HTTPException, APIRouter
from .schemas import CreatedBuilding
from typing import Annotated
from core.db import buildings_collection
import json
from grpc_building.greeter_client  import run
import http3

buildings_router = APIRouter(
    prefix="/buildings",
    tags=["buildings"]
)


async def make_request():
    url = 'http://users_app:8000/users/hello/'

    client = http3.AsyncClient()
    response = await client.get(url=url)
    print("status_code > ",  response.status_code)
    print("res >  ",  response.text)


@buildings_router.post("/create_building/", response_model=CreatedBuilding)
async def create_building(
    user_id : int , 
    building : CreatedBuilding,
    ):

    run()
    building_json = json.loads(building.json())
    building_json.update({"user_id": user_id})
    await buildings_collection.insert_one(building_json)
    return building_json


@buildings_router.get("/hello/", status_code=201)
async def hello():
    await make_request()
    return {"new_user", "hello from server"}
