from dependency_injector import containers, providers
from sqlmodel import Session, create_engine

from adapter.repositories.ticket_repository import TicketRepository
from core.application.use_cases.create_ticket import CreateTicketUseCase
from infra.config.context import db_session_context
from infra.config.settings import settings
from infra.tools.logger import Logger


def get_db_session(engine):
    session = db_session_context.get()
    if session is None:
        return Session(bind=engine)
    return session


class Container(containers.DeclarativeContainer):
    settings = providers.Object(settings)

    # Database
    engine = providers.Singleton(create_engine, url=settings.provided.database_url)

    db_session = providers.Callable(get_db_session, engine=engine)

    # Tools
    logger = providers.Singleton(Logger)

    # Repositories
    ticket_repository = providers.Factory(TicketRepository, session=db_session)

    # Use Cases
    create_ticket_use_case = providers.Factory(
        CreateTicketUseCase,
        ticket_repository=ticket_repository,
        logger=logger,
    )
