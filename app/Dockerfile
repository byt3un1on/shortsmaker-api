FROM python:3.11-slim

# Evita que o Python gere arquivos .pyc e que o output do log seja bufferizado
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Dependências do sistema (necessárias para o psycopg2 se não for o binary)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala as dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Cria um usuário não-root para segurança
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Expõe a porta que a API usará
EXPOSE 8000

# Comando para iniciar a aplicação
# Nota: Alembic migrations costumam ser rodadas antes do start em produção
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
