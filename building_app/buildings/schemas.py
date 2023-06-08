from pydantic import BaseModel, validator, Field
from typing import Union
from datetime import datetime 

class Coordinates(BaseModel):
    x: float
    y: float
    z: float 


class BuildingPosition(BaseModel):
    worldPos: Coordinates 
    localScale: Coordinates
    maxScale: Coordinates


class CreatedBuilding(BuildingPosition):
    buildingLevel: int 
    upgradeEndTime: Union[datetime, None] = datetime.utcnow()
    upgradeBuildTime: int = 0
    isUpgrading: bool = False
    isEstablishing: bool = True

