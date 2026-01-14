# Shortsmaker API Documentation

Esta pasta contém a documentação da API do Shortsmaker, incluindo collections do Postman e ambientes.

## Arquivos

- `shortsmaker_collection.json` - Collection completa do Postman com todos os endpoints
- `shortsmaker_dev.json` - Ambiente de desenvolvimento
- `shortsmaker_homolog.json` - Ambiente de homologação
- `shortsmaker_prod.json` - Ambiente de produção

## Como usar

1. Importe a collection `shortsmaker_collection.json` no Postman
2. Importe os ambientes correspondentes
3. Selecione o ambiente apropriado (dev/homolog/prod)
4. Execute as requests

## Endpoints disponíveis

### Health
- `GET /health` - Verificação de saúde da API

### Tickets
- `POST /api/v1/tickets` - Criar um novo ticket para geração de shorts
  - Body: `{"theme": "string", "description": "string"}`

## Variáveis da Collection

- `ticketId` - ID do ticket criado (preenchido automaticamente após criação)