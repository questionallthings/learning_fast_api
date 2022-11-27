import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database:
    def __init__(self,
                 #db_host='192.168.1.201',
                 db_host='192.168.1.105',
                 db_port='3306',
                 #db_port='5432',
                 db_name='thanatosdb',
                 #db_user='postgres',
                 db_user='root',
                 db_password='42B-=-edA?ucH3bA',
                 #db_engine_type='postgresql'):
                 db_engine_type='memsql'):
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_engine_type = db_engine_type
        self.db_engine_url = ''
        self.db_engine = ''
        self.db_base = declarative_base()

        if self.db_engine_type.lower() == 'postgresql':
            self.db_engine_url = f'postgresql+psycopg2://' \
                                 f'{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{db_name}'
        elif self.db_engine_type.lower() == 'mysql':
            self.db_engine_url = f'mysql://' \
                                 f'{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{db_name}'
        elif self.db_engine_type.lower() == 'memsql':
            self.db_engine_url = f'mysql+pymysql://' \
                                 f'{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{db_name}'
            print(self.db_engine_url)
        elif self.db_engine_type.lower() == 'sqllite':
            self.db_engine_url = f'sqllite://{self.db_host}/{self.db_name}'
        elif self.db_engine_type.lower() == 'oracle':
            self.db_engine_url = f'oracle+cx_oracle://' \
                                 f'{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{db_name}'
        elif self.db_engine_type.lower() == 'mssql':
            self.db_engine_url = f'mssql+pyodbc://' \
                                 f'{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{db_name}'

    def create_engine(self):
        self.db_engine = create_engine(self.db_engine_url)

    def set_admin_credentials(self, db_user, db_password):
        self.db_user = db_user
        self.db_password = db_password

        os.environ['db_user'] = self.db_user
        os.environ['db_password'] = self.db_password

    def create_session(self):
        db_session = sessionmaker(autocommit=False,
                                  autoflush=False,
                                  bind=self.db_engine)

        return db_session()

    def get_db(self):
        db_session = self.create_session()
        try:
            yield db_session
        finally:
            db_session.close()


