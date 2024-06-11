from build import create_tables
from migrations import migration_1


if __name__ == '__main__':
    create_tables()
    migration_1()
