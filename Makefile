ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)
MAKEFLAGS += --silent
RUN = docker-compose run --rm -w /code booksales
EXEC = docker-compose exec booksales

# HELP COMMANDS
help: ## show this help
	@echo 'usage: make [target] [option]'
	@echo ''
	@echo 'Common sequence of commands:'
	@echo '- make build [nocache]'
	@echo '- make init'
	@echo '- make run'
	@echo '- make test'
	@echo '- make lint'
	@echo '- make migrate'
	@echo '- make shell'
	@echo ''
	@echo 'targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'


.PHONY : build
build: ## build application containers
ifeq ($(ARGS), nocache)
	@ docker-compose build --no-cache
else
	@ docker-compose build
endif

.PHONY: init
init: ## build containers and run fixtures
	@ make run
	@ make migrate

.PHONY: populate
populate: init ## Populate the database
	@ $(EXEC) python fixtures/create_entities.py

.PHONY : run
run: ## start the application
	@ docker-compose up -d

.PHONY: migrate
migrate: run ## Execute migrations
	@ $(EXEC) alembic upgrade head

.PHONY : test
test: ## run the application tests
	@ $(EXEC) py.test

.PHONY: lint
lint: ## run linters over the code
	@ $(RUN) /bin/sh -c "isort . && black . && flake8"

.PHONY: attach
attach: ## attach to container stdout
	@ docker attach booksales

.PHONY: shell
shell: run ## run application's shell
	@ $(EXEC) python
