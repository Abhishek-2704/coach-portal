import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_coach_portal.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)

#grok prompt
    #Continue my Django Basketball Coach Portal with login, registration, Excel/PDF reports, and clean design

#run commands
    #cd C:\Users\dell\Downloads\Abhishek\PP\the_coach_portal
    #.venv .venv\Scripts\activate
    #python manage.py runserver
    