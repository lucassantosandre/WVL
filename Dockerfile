# Imagem base
FROM python:3.10-slim

# Labels informativos
LABEL maintainer="seuemail@exemplo.com"
LABEL version="1.0"
LABEL description="Aplicação para calcular volume e intensidade de treinos."

# Diretório de trabalho
WORKDIR /app

# Copiar dependências do Python
COPY requirements.txt .

# Instalar dependências do sistema e do Python
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install watchdog

# Copiar o código do aplicativo
COPY . .

# Expor a porta do servidor
EXPOSE 8000

# Comando padrão
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
