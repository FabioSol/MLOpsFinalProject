from ucimlrepo import fetch_ucirepo
from app.data.controller import AidsController


def migration_1():
    source = fetch_ucirepo(id=890)
    df = source.data.original
    AidsController.create_many(df=df)


if __name__ == '__main__':
    migration_1()