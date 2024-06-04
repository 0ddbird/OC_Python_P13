# Run django command
@django *command:
    python3 manage.py {{ command }}

@s:
    python3 manage.py runserver

@clean *path:
    ruff check --fix {{ path }}
    isort {{ path }}
    ruff format {{ path }}
    black {{ path }}