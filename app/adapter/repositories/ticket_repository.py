from typing import List, Optional
from uuid import UUID

from sqlmodel import Session, select

from core.domain.enums.ticket_status import TicketStatus
from core.domain.ticket import Ticket
from core.interfaces.adapters.repositories.i_ticket_repository import ITicketRepository
from core.interfaces.infra.tools.i_logger import ILogger


class TicketRepository(ITicketRepository):
    def __init__(self, session: Session, logger: ILogger):
        self.session = session
        self.logger = logger

    async def create(self, ticket: Ticket) -> Ticket:
        self.logger.info(
            f"Creating ticket with id {ticket.id}, attributes: {len(ticket.attributes)}")
        for attr in ticket.attributes:
            self.logger.info(
                f"Attribute: {attr.key} = {attr.value}, ticket_id: {getattr(attr, 'ticket_id', None)}")
            self.session.add(attr)
        self.session.add(ticket)
        self.session.commit()
        self.logger.info("Committed ticket")
        self.session.refresh(ticket)
        self.logger.info(
            f"Refreshed ticket with {len(ticket.attributes)} attributes")
        return ticket

    async def get_by_id(self, ticket_id: UUID) -> Optional[Ticket]:
        statement = select(Ticket).where(Ticket.id == ticket_id)
        results = self.session.exec(statement)
        return results.first()

    async def list_pending(self) -> List[Ticket]:
        statement = select(Ticket).where(Ticket.status == TicketStatus.PENDING)
        results = self.session.exec(statement)
        return list(results.all())

    async def update_status(self, ticket_id: UUID, status: TicketStatus) -> None:
        ticket = await self.get_by_id(ticket_id)
        if ticket:
            ticket.status = status
            self.session.add(ticket)
            self.session.commit()
