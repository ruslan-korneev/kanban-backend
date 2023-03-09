# Backend for Kanban Board on Django

# Description
Managing Projects, Tasks, Developing a big systems using this Kanban Board

# Installation and Running
## Using docker
```bash
cat env_sample > .env  # change variables values if you need
docker compose up -d
```

## Without docker for development
```zsh
python -m venv .venv
. .venv/bin/activate
cat env_sample > .env  # change variables values if you need, e.g. DJANGO_SETTINGS_MODULE=src.settings.local

poetry install
pre-commit install
dj migrate
dj runserver
```
