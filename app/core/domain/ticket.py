from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

from core.domain.enums.ticket_status import TicketStatus


class Ticket(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    status: TicketStatus = Field(default=TicketStatus.PENDING)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    is_deleted: bool = False

    attributes: List["TicketAttribute"] = Relationship(back_populates="ticket")


class TicketAttribute(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    ticket_id: UUID = Field(foreign_key="ticket.id")
    key: str
    value: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_deleted: bool = False

    ticket: Optional[Ticket] = Relationship(back_populates="attributes")
