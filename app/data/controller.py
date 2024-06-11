import pandas as pd
from peewee import DoesNotExist

from app.data.schema import Patient
from functools import wraps

def db_query(func):
    """
    Decorator for database query methods.
    Converts the query result to a Pandas DataFrame.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            return pd.DataFrame(result)
        elif hasattr(result, 'dicts'):
            return pd.DataFrame(list(result.dicts()))
        else:
            raise ValueError("Unsupported query result type. Expected list or query object with 'dicts' attribute.")
    return wrapper

class AidsController:

    @staticmethod
    def create_many(df:pd.DataFrame):
        for _, row in df.iterrows():
            Patient.create(**row)

    @staticmethod
    @db_query
    def read_all():
        return Patient.select()
    @staticmethod
    @db_query
    def read_used():
        return Patient.select().where(Patient.used_for_training == True)

    @staticmethod
    @db_query
    def read_new():
        return Patient.select().where(Patient.used_for_training == False)

    @staticmethod
    def update_to_used(pidnums: list):
        try:
            # Update records where pidnum is in the list
            Patient.update(used_for_training=True).where(Patient.pidnum.in_(pidnums)).execute()
        except DoesNotExist:
            # Handle the case where one of the provided pidnums doesn't exist
            pass

if __name__ == '__main__':
    print(AidsController.read_used())
