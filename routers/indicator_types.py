from fastapi import APIRouter
from database import Database
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
import crud

router = APIRouter(
    prefix="/api/v1/indicator_types",
    tags=["Indicator Types"]
)
db_initial = Database()
db_initial.create_engine()

# @router.post("") # For creating new data
# @router.get("") # For reading data
# @router.put("") # For updating data
# @router.delete("") # For deleting data
