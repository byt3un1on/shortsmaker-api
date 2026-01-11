import uvicorn
from fastapi import FastAPI, Request
from sqlmodel import Session

from adapter.controllers.ticket_controller import router as ticket_router
from infra.config.container import Container
from infra.config.context import db_session_context


def create_app() -> FastAPI:
    container = Container()

    # Wire the container to the modules that use DI
    container.wire(modules=["adapter.controllers.ticket_controller"])

    app = FastAPI(
        title="Shortsmaker API",
        description="API para gerenciar a criação de vídeos curtos",
        version="1.0.0",
    )

    app.container = container  # type: ignore

    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
        engine = container.engine()
        with Session(engine) as session:
            token = db_session_context.set(session)
            try:
                response = await call_next(request)
                return response
            finally:
                db_session_context.reset(token)

    app.include_router(ticket_router, prefix="/api/v1")

    @app.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "UP"}

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
