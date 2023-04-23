from db import get_db
from sqlalchemy.orm import Session


class CRUD:
    def __init__(self) -> None:
        pass

    def add(self, db: Session, data: dict) -> None:
        db.add(data)

    def pre_save_check(self, db: Session, obj) -> None:
        """
        check if object can be saved in the database
        this function created to handle atomic transaction fails
        Args:
            db (Session): opened session with database
            obj (dict): object to check
        """

        try:
            db.flush([obj])
        except Exception as e:
            raise e
    @classmethod
    def pre_save_mult_check(cls, db: Session) -> None:
        """
        same as pre_save_check function but its checking all
        the object that been added to the session
        Args:
            db (Session): opened session with database
        """
        try:
            db.flush()
        except Exception as e:
            raise e
