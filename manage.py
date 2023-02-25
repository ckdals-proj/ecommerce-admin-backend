from app.main import app

import os
import sys
import uvicorn
from typing import Optional
import json
from glob import glob

def run_server(host: Optional[str] = None, port: Optional[int] = None) -> None:
    host = host or "127.0.0.1"
    port = port or 8000
    uvicorn.run(app, host=host, port=port)

def sql_makemigrations():
    with open('migrations/sql/migrate.json') as f: migrate = json.load(f)
    with open('migrations/sql/makemigrations.json') as f: migration = json.load(f)
    if not(migrate.get('is_migrated')): raise Exception("please migrate")

    version = str(len(migration) + 1)
    length = 5 - len(version)
    name = length*"0"+version
    os.system('alembic revision --autogenerate -m '+name)

    revision = glob('migrations/sql/versions/'+name+"*")[0]
    revision = revision.split("migrations/sql/versions/")[1].split("_")

    migrate['is_migrated'] = False
    migration[revision[0]] = revision[1]

    with open('migrations/sql/migrate.json', "w") as f: json.dump(migrate, f)
    with open('migrations/sql/makemigrations.json', "w") as f: json.dump(migration, f)

def sql_migrate():
    os.system("alembic upgrade head")
    migrate = {"is_migrated":True}
    with open('migrations/sql/migrate.json', "w") as f: json.dump(migrate, f)

def main():
    input_ = sys.argv
    
    #runserver
    if input_[1] == "runserver": run_server()

    #sql
    elif str(" ".join(input_[1:])) == 'sql makemigrations': sql_makemigrations()
    elif str(" ".join(input_[1:])) == 'sql migrate': sql_migrate()

    #nosql
    elif input_[1] == "nosql": pass

    #other
    else: raise Exception('Not Command')


if __name__=="__main__":
    main()
