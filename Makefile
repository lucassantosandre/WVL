.PHONY: help build run stop restart clean logs shell

# Variáveis
APP_NAME = training-calc
DOCKER_COMPOSE = docker compose
DOCKER_IMAGE = $(APP_NAME):latest

help: ## Mostra a lista de comandos disponíveis
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## Constrói a imagem Docker
	docker build -t $(DOCKER_IMAGE) .

run: build ## Constrói e executa o contêiner com hot-reload
	$(DOCKER_COMPOSE) up --build

stop: ## Para o contêiner
	$(DOCKER_COMPOSE) down

restart: stop run ## Reinicia o contêiner

clean: ## Remove imagens e contêineres não utilizados
	docker system prune -f

logs: ## Exibe os logs do contêiner
	$(DOCKER_COMPOSE) logs -f app

shell: ## Acessa o shell do contêiner
	$(DOCKER_COMPOSE) exec app sh
