from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from core.domain.enums.ticket_status import TicketStatus
from core.domain.ticket import Ticket


class ITicketRepository(ABC):
    @abstractmethod
    async def create(self, ticket: Ticket) -> Ticket:
        pass

    @abstractmethod
    async def get_by_id(self, ticket_id: UUID) -> Optional[Ticket]:
        pass

    @abstractmethod
    async def list_pending(self) -> List[Ticket]:
        pass

    @abstractmethod
    async def update_status(self, ticket_id: UUID, status: TicketStatus) -> None:
        pass
