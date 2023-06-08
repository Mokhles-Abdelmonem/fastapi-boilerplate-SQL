import motor.motor_asyncio 
import os
from dotenv import load_dotenv
load_dotenv(".env")


MONGO_URL = os.environ["MONGO_URL"]

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

database = client.TawasolGameMicroServices

buildings_collection = database.get_collection("buildings")
