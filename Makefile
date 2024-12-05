# Determine the correct docker compose command
DOCKER_COMPOSE=docker compose

# Default target
.PHONY: all
all: help

# Help target
.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  help              Show this help"
	@echo "  up                Build and execute App"
	@echo "  shell             Open a shell in the app container"

.PHONY: up
# Build and execute app
up:
	$(DOCKER_COMPOSE) up --build --force-recreate --remove-orphans
	@echo "App running"

.PHONY: shell
# Execute shell
shell:
	$(DOCKER_COMPOSE) run --rm --remove-orphans app bash
	@echo "Shell opened in app container"