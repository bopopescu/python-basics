# Setup virtual env
python3 -m venv dev
source virt/bin/activate

# Configuration with Setup.py
https://setuptools.readthedocs.io/en/latest/setuptools.html

python3 setup.py install
OR
python3 setup.py develop


# Setup Alembic
pip install alembic
alembic init alembic
// update /alembic.ini with database url
// in /alembic/env.py, update target_metadata to be able to use auto-generate
from myapp.mymodel import BaseModel
target_metadata = BaseModel.metadata
// Don't forget to import all the models as well

// autogemerate
alembic revision --autogenerate -m "init"
// create migration
alembic revision -m "migration name"
// run migration 
alembic upgrade head
// undo last migration
alembic downgrade -1


# Start service
python3 app.py


# Questions:
