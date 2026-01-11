# ShortsMaker API

API principal para o sistema ShortsMaker, desenvolvida com FastAPI.

## Estrutura do Projeto

O projeto segue os princípios de **Clean Architecture**:

- `app/core`: Entidades de domínio e casos de uso.
- `app/adapter`: Controladores (routers), repositórios e interfaces.
- `app/infra`: Implementações técnicas como banco de dados, storage e logs.

## Desenvolvimento

Para iniciar o desenvolvimento, abra este projeto no **VS Code DevContainer**.

### Comandos Úteis

- `make install`: Instala as dependências.
- `make run`: Inicia a API localmente.
- `make test`: Executa os testes unitários.
- `make lint`: Executa a análise estática de código.
- `make format`: Formata o código conforme as regras do projeto.

## Referência

Este projeto foi baseado no padrão do repositório `canal-de-cortes/agent-operator`.
