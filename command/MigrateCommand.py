import sys
from alembic.config import main


def migrate_command():
    """Migration commands - read more at https://alembic.readthedocs.org/en/latest/index.html"""
    import app.models

    argv = sys.argv[2:]
    main(argv=argv)