from core.domain.ticket import Ticket
from core.interfaces.adapters.repositories.i_ticket_repository import \
    ITicketRepository
from core.interfaces.infra.tools.i_logger import ILogger


class CreateTicketUseCase:
    def __init__(self, ticket_repository: ITicketRepository, logger: ILogger):
        self._ticket_repository = ticket_repository
        self._logger = logger

    async def execute(self, theme: str, description: str) -> Ticket:
        self._logger.info(f"Executando caso de uso para criar ticket com tema: {theme}")

        # Aqui a lógica de negócio orquestrada
        ticket = Ticket()
        # Poderíamos ter mais lógica aqui antes de salvar

        return await self._ticket_repository.create(ticket)
