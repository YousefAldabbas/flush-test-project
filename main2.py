from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List, Optional
from db_se import get_db, engine
import model
from schemas import TestSchema

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

    test_obj = model.Test2(**dict_data)
    db.add(test_obj)
    db.commit()
    db.refresh(test_obj)
    return test_in
