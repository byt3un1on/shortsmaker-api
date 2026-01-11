from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from core.application.use_cases.create_ticket import CreateTicketUseCase
from core.domain.ticket import Ticket
from infra.config.container import Container

router = APIRouter()


@router.post("/tickets", response_model=Ticket)
@inject
async def create_ticket(
    theme: str,
    description: str,
    use_case: CreateTicketUseCase = Depends(Provide[Container.create_ticket_use_case]),
):
    return await use_case.execute(theme=theme, description=description)


@router.get("/health")
async def health():
    return {"status": "UP"}
