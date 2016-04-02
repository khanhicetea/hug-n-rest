import os
from command import Manager, migrate_command

env = os.getenv('APP_ENV', 'development')

manager = Manager()
manager.register_command('db', migrate_command)

if __name__ == "__main__":
    manager.run()