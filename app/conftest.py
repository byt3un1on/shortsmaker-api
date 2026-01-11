import os
import sys

import pytest
from dependency_injector import providers
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from core.domain.ticket import Ticket, TicketAttribute  # noqa: F401
from infra.config.container import Container

# Add app to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture(scope="session")
def test_engine():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture
def test_session(test_engine):
    with Session(test_engine) as session:
        yield session


@pytest.fixture
def test_container(test_engine):
    container = Container()
    container.engine.override(providers.Object(test_engine))
    return container


@pytest.fixture
def api_url():
    return "http://localhost:8001"
