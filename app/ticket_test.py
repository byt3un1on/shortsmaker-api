from uuid import uuid4

import pytest
from dependency_injector import providers
from fastapi.testclient import TestClient

from api import app
from core.domain.enums.ticket_status import TicketStatus
from core.domain.ticket import Ticket
from infra.tools.logger import Logger

client = TestClient(app)


@pytest.fixture(autouse=True)
def override_db(test_engine):
    app.container.engine.override(providers.Object(test_engine))
    yield
    app.container.engine.reset_override()


def test_create_ticket():
    response = client.post(
        "/api/v1/tickets",
        params={"theme": "Tecnologia", "description": "Vídeo sobre IA"},
    )
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["status"] == "PENDING"


def test_root_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}


def test_logger_methods():
    logger = Logger()
    logger.debug("Debug message")
    logger.info("Info message")
    logger.success("Success message")
    logger.warn("Warning message")
    logger.error("Error message")


def test_repository_methods(test_engine):
    repo = app.container.ticket_repository()

    # Test Create
    ticket = Ticket(status=TicketStatus.PENDING)

    # Run async methods
    import asyncio

    created = asyncio.run(repo.create(ticket))
    assert created.id is not None

    # Test Get by ID
    found = asyncio.run(repo.get_by_id(created.id))
    assert found.id == created.id

    # Test List Pending
    pending = asyncio.run(repo.list_pending())
    assert len(pending) >= 1

    # Test Update Status
    asyncio.run(repo.update_status(created.id, TicketStatus.COMPLETED))
    updated = asyncio.run(repo.get_by_id(created.id))
    assert updated.status == TicketStatus.COMPLETED

    # Test Update Status for non-existent
    asyncio.run(repo.update_status(uuid4(), TicketStatus.FAILED))
