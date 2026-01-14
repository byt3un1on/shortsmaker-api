from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from core.application.use_cases.create_ticket import CreateTicketUseCase
from core.domain.ticket import Ticket
from infra.config.container import Container

router = APIRouter(tags=["Tickets"])


class CreateTicketRequest(BaseModel):
    theme: str
    description: str


@router.post("/tickets", response_model=Ticket)
@inject
async def create_ticket(
    request: CreateTicketRequest,
    use_case: CreateTicketUseCase = Depends(
        Provide[Container.create_ticket_use_case]),
):
    return await use_case.execute(theme=request.theme, description=request.description)
