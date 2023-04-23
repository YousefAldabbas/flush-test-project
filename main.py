from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List, Optional
from broker import Broker
from db import get_db, engine
import model
from model import Test
from schemas import TestSchema

from crud import CRUD

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", response_model=Any)
def beat(
    db: Session = Depends(get_db),
) -> Any:
    return {"message": "ok"}


@app.post("/")
def create_item(
    *,
    db: Session = Depends(get_db),
    test_in: TestSchema,
) -> Any:
    """
    Create new test.
    """
    dict_data = test_in.dict()
    test_obj_1 = Test(id=1, text=test_in.text)
    db.add(test_obj_1)
    # CRUD.pre_save_check(db, test_obj_1)
    CRUD.pre_save_mult_check(db)
    Broker(service=2).create(test_obj_1)
    db.commit()
    db.refresh(test_obj_1)

    return test_in
