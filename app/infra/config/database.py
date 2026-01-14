import os

from alembic import command
from alembic.config import Config
from sqlmodel import Session, create_engine

from .settings import settings

engine = create_engine(settings.database_url, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def run_migrations():
    """Aplica as migrations do Alembic programaticamente."""
    # O arquivo alembic.ini está na raiz da pasta app/
    # __file__ está em app/infra/config/database.py
    base_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    ini_path = os.path.join(base_dir, "alembic.ini")

    alembic_cfg = Config(ini_path)
    # Garante que o script_location aponte para a pasta migrations correta
    alembic_cfg.set_main_option("script_location", os.path.join(base_dir, "migrations"))

    command.upgrade(alembic_cfg, "head")
