from dependency_injector import containers, providers

from app.services.module import (
    CategoryService,
)

from app.repositories.module import (
    CategoryRepository,
)

from app.db.database import DataBase

import os


class Container(containers.DeclarativeContainer):

    # wiring_config = containers.WiringConfiguration(modules=["app.controllers.base"])

    # config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(DataBase,db_url=os.environ.get('DB_SESSION'))

    category_repository = providers.Factory(
        CategoryRepository,
        session_factory=db.provided.session,
    )

    category_service = providers.Singleton(
        CategoryService,
        category_repository=category_repository
    )