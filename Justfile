# Run django command
@django *command:
    python3 manage.py {{ command }}

@s:
    python3 manage.py runserver